Summary:	Libraries for the gEDA project
Summary(pl):	Biblioteki projektu gEDA
Name:		libgeda
Version:	20061020
Release:	0.1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3caf1aeee5627706b9abe54f6601a7dc
URL:		http://www.geda.seul.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	guile-devel >= 1.4
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Electronic Design Automation library.

%description -l pl
Biblioteka Systemu Zautomatyzowanego Projektowania Uk³adów
Elektronicznych GNU.

%package devel
Summary:	Header files and develpment documentation for libgeda
Summary(pl):	Pliki nag³ówkowe i dokumentacja do libgeda
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.2.0
Requires:	guile-devel

%description devel
Header files and develpment documentation for libgeda.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do libgeda.

%package static
Summary:	Static libgeda library
Summary(pl):	Biblioteka statyczna libgeda
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgeda library.

%description static -l pl
Biblioteka statyczna libgeda.

%prep
%setup -q

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
install -d $RPM_BUILD_ROOT%{_datadir}/gEDA/scheme

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
%dir %{_datadir}/gEDA
%dir %{_datadir}/gEDA/scheme

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/libgeda.pc
#%{_infodir}/libgedadoc*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
