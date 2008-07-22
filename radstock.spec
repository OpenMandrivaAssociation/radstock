%define	name	radstock
%define	version	0.66
%define	release	%mkrel 7

Summary:	Radstock Radius Analyser
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://sourceforge.net/projects/radstock/
License:	GPL
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-misc_fixes.patch
# P0 originates from http://www.cse.fau.edu/~valankar/radstock_password_patch/radstock-0.66.password.patch-1.2.tar.gz
Patch1:		%{name}-%{version}-password.patch
Patch2:		radstock-0.66-pcap_headers.diff
Group:		System/Servers
BuildRequires:	libpcap-devel >= 0.8.3
BuildRequires:	libavlmap-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	automake1.7
BuildRequires:	autoconf2.5
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Radstock is a tool to analyse RADIUS traffic on high volume radius
servers. It has the ability to fully decode each packet, and also
has extensive filters capabilities to allow you to selectively
match radius packets.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force && aclocal-1.7 && autoconf --force

%configure2_5x

%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%config(noreplace) %attr(0755,root,root) %{_sysconfdir}/raddb/dictionary-%{name}
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/%{name}.1*

