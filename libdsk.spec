#
# Conditional build:
%bcond_without	static_libs	# static library
%bcond_without	java		# Java binding
#
Summary:	libdsk library
Summary(pl.UTF-8):	Biblioteka libdsk
Name:		libdsk
# note: 1.4.x is stable, 1.5.x development version
Version:	1.4.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.seasip.info/Unix/LibDsk/%{name}-%{version}.tar.gz
# Source0-md5:	9e1128a423069528c90a647f69284792
Patch0:		%{name}-am.patch
Patch1:		%{name}-java.patch
URL:		http://www.seasip.info/Unix/LibDsk/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bzip2-devel
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libtool >= 2:2
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package -n java-libdsk
Summary:	Java interface to libdsk library
Summary(pl.UTF-8):	Interfejs Javy do biblioteki libdsk
Group:		Libraries/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jre

%description -n java-libdsk
Java interface to libdsk library.

%description -n java-libdsk -l pl.UTF-8
Interfejs Javy do biblioteki libdsk.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e 's,/usr/local/share,%{_datadir},' man/libdskrc.5

# avoid lyx BR
touch -r doc/libdsk.lyx doc/libdsk.txt

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# - ac_cv_prog_uudecode_base64=no is a workaround to enforce
#   Test.class recompilation (included version doesn't work with JDK 1.6);
# - check needs . in CLASSPATH
# - we redefine --datadir because global config file is %{_datadir}/LibDsk/libdskrc
export CLASSPATH=.
%configure \
	ac_cv_prog_uudecode_base64=no \
	--datadir=%{_sysconfdir} \
	%{!?with_static_libs:--disable-static} \
	%{?with_java:--with-jni}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D doc/libdskrc.sample $RPM_BUILD_ROOT%{_sysconfdir}/LibDsk/libdskrc

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
%dir %{_sysconfdir}/LibDsk
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/LibDsk/libdskrc
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

%if %{with java}
%files -n java-libdsk
%defattr(644,root,root,755)
%{_javadir}/libdsk.jar
%endif
