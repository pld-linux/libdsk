#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	libdsk library
Summary(pl.UTF-8):	Biblioteka libdsk
Name:		libdsk
Version:	1.3.3
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.seasip.info/Unix/LibDsk/%{name}-%{version}.tar.gz
# Source0-md5:	2cce41b4b1325d697183e34afcae2a9c
URL:		http://www.seasip.demon.co.uk/Unix/LibDsk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# global config file is %{_datadir}/LibDsk/libdskrc
%define		_datadir	%{_sysconfdir}

%description
LibDsk is a library intended to give transparent access to floppy
drives and to the "disc image files" used by emulators to represent
floppy drives.

%description -l pl.UTF-8
LibDsk jest biblioteką, która w sposób przezroczysty daje dostęp do
"obrazów dysków" używanych przez emulatory do reprezentowania dysków
elastycznych.

%package devel
Summary:	libdsk library - development files
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libdsk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel
Requires:	zlib-devel

%description devel
The libdsk-devel package contains the header files and documentation
needed to develop applications with libdsk.

%description devel -l pl.UTF-8
Pakiet libdsk-devel zawiera pliki nagłówkowe i dokumentację potrzebne
do kompilowania aplikacji korzystających z libdsk.

%package static
Summary:	libdsk static library
Summary(pl.UTF-8):	Statyczna biblioteka libdsk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static libdsk library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libdsk.

%prep
%setup -q

%{__perl} -pi -e 's,/usr/local/share,%{_datadir},' man/libdskrc.5

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_bindir}/apriboot
%attr(755,root,root) %{_bindir}/dsk*
%attr(755,root,root) %{_bindir}/md3serial
%attr(755,root,root) %{_libdir}/libdsk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdsk.so.3
%{_mandir}/man1/apriboot.1*
%{_mandir}/man1/dsk*.1*
%{_mandir}/man1/md3serial.1*
%{_mandir}/man5/libdskrc.5*

%files devel
%defattr(644,root,root,755)
%doc doc/{libdsk.txt,cfi.html,TODO}
%attr(755,root,root) %{_libdir}/libdsk.so
%{_libdir}/libdsk.la
%{_includedir}/libdsk.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdsk.a
%endif
