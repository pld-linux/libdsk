Summary:	libdsk library
Summary(pl):	Biblioteka libdsk
Name:		libdsk
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://www.seasip.demon.co.uk/Unix/LibDsk/%{name}-%{version}.tar.gz
URL:		http://www.seasip.demon.co.uk/Unix/LibDsk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibDsk is a library intended to give transparent access to floppy
drives and to the "disc image files" used by emulators to represent
floppy drives.

%description -l pl
LibDsk jest bibliotek±, która w sposób przezroczysty daje dostêp do
"obrazów dysków" u¿ywanych przez emulatory do reprezentowania dysków
elastycznych.

%package devel
Summary:	libdsk library - development
Summary(pl):	Czê¶æ dla programistów u¿ywaj±cych biblioteki libdsk
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The libdsk-devel package contains the header files and documentation
needed to develop applications with libdsk.

%description devel -l pl
Pakiet libdsk-devel zawiera pliki nag³ówkowe i dokumentacjê potrzebne
do kompilowania aplikacji korzystaj±cych z libdsk.

%package static
Summary:	libdsk static library
Summary(pl):	Statyczna biblioteka libspectrum
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
The libdsk-static package contains the static libraries of libdsk.

%description static -l pl
Statyczna wersja biblioteki libdsk.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdsk.so.*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*

%files devel
%defattr(644,root,root,755)
%doc doc/{libdsk.txt,TODO}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libdsk.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
