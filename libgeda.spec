Summary:	Libraries for the gEDA project
Summary(pl):	Biblioteki projektu gEDA
Name:		libgeda
Version:	20030901
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	01f973c45b98c75d8d0620f4dd4dc33c
URL:		http://www.geda.seul.org/
BuildRequires:	XFree86-devel
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	guile-devel >= 1.4
BuildRequires:	libgdgeda-devel >= 2.0.15
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Electronic Design Automation library.

%description -l pl
Biblioteka Systemu Zautomatyzowanego Projektowania Uk³adów
Elektronicznych GNU.

%package devel
Summary:	Header files and develpment documentation for libgeda
Summary(pl):	Pliki nag³ówkowe i dokumetacja do libgeda
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib2-devel >= 2.2.0
Requires:	guile-devel
Requires:	libgdgeda-devel >= 2.0.15

%description devel
Header files and develpment documentation for libgeda.

%description devel -l pl
Pliki nag³ówkowe i dokumetacja do libgeda.

%package static
Summary:	Static libgeda library
Summary(pl):	Biblioteka statyczna libgeda
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libgeda library.

%description static -l pl
Biblioteka statyczna libgeda.

%prep
%setup -q

%build
LDFLAGS="-L%{_libdir} %{rpmcflags}"; export LDFLAGS
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

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/libgeda.pc
%{_infodir}/libgedadoc*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
