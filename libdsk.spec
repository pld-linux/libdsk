Summary:	libdsk library
Summary(pl):	Biblioteka libdsk
Name:		libdsk
Version:	1.1.3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.seasip.demon.co.uk/Unix/LibDsk/%{name}-%{version}.tar.gz
# Source0-md5:	8e5f039b04e9d7122e7e849934305798
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

%description -l pl
LibDsk jest bibliotek±, która w sposób przezroczysty daje dostêp do
"obrazów dysków" u¿ywanych przez emulatory do reprezentowania dysków
elastycznych.

%package devel
Summary:	libdsk library - development files
Summary(pl):	Pliki programistyczne biblioteki libdsk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel
Requires:	zlib-devel

%description devel
The libdsk-devel package contains the header files and documentation
needed to develop applications with libdsk.

%description devel -l pl
Pakiet libdsk-devel zawiera pliki nag³ówkowe i dokumentacjê potrzebne
do kompilowania aplikacji korzystaj±cych z libdsk.

%package static
Summary:	libdsk static library
Summary(pl):	Statyczna biblioteka libdsk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static libdsk library.

%description static -l pl
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
%configure
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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libdsk.so.*.*.*
%{_mandir}/man1/*
%{_mandir}/man5/libdskrc.5*

%files devel
%defattr(644,root,root,755)
%doc doc/{libdsk.txt,cfi.html,TODO}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libdsk.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
