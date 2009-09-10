Summary:	Radstock Radius Analyser
Name:		radstock
Version:	0.66
Release:	%mkrel 10
Group:		System/Servers
License:	GPL
URL:		http://sourceforge.net/projects/radstock/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-misc_fixes.patch
# P0 originates from http://www.cse.fau.edu/~valankar/radstock_password_patch/radstock-0.66.password.patch-1.2.tar.gz
Patch1:		%{name}-%{version}-password.patch
Patch2:		radstock-0.66-pcap_headers.diff
Patch3:		radstock-LDFLAGS.diff
BuildRequires:	libpcap-devel >= 0.8.3
BuildRequires:	libavlmap-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Radstock is a tool to analyse RADIUS traffic on high volume radius servers. It
has the ability to fully decode each packet, and also has extensive filters
capabilities to allow you to selectively match radius packets.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

echo "#define VERSION \"%{version}\"" > version.h

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal; autoconf --force

export CFLAGS="%{optflags} -I%{_includedir}/avlmap -I%{_includedir}/pcap"

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%config(noreplace) %attr(0755,root,root) %{_sysconfdir}/raddb/dictionary-%{name}
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/%{name}.1*
