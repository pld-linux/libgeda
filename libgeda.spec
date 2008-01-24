Summary:	Libraries for the gEDA project
Summary(pl.UTF-8):	Biblioteki projektu gEDA
Name:		libgeda
Version:	1.2.0
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.geda.seul.org/pub/geda/release/v1.2/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	43f2b2daabee59ffeae84fe13c10c51d
URL:		http://www.geda.seul.org/
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

%description -l pl.UTF-8
Biblioteka Systemu Zautomatyzowanego Projektowania Układów
Elektronicznych GNU.

%package devel
Summary:	Header files and develpment documentation for libgeda
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do libgeda
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.2.0
Requires:	guile-devel

%description devel
Header files and develpment documentation for libgeda.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libgeda.

%package static
Summary:	Static libgeda library
Summary(pl.UTF-8):	Biblioteka statyczna libgeda
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgeda library.

%description static -l pl.UTF-8
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

install -d $RPM_BUILD_ROOT%{_docdir}/geda-doc/man
install -d $RPM_BUILD_ROOT%{_docdir}/geda-doc/readmes

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/gEDA
%{_datadir}/gEDA/scheme
%{_docdir}/geda-doc


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
