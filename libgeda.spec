#
# TODO:
# - package mime info files
# - package icons
# or drop this spec and package new geda
Summary:	Libraries for the gEDA project
Summary(pl.UTF-8):	Biblioteki projektu gEDA
Name:		libgeda
Version:	1.4.2
Release:	4
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.geda.seul.org/pub/geda/release/v1.4/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e22e28cf3684efcf42f6591995fe943b
Patch0:		%{name}-guile.patch
URL:		http://www.geda.seul.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	guile-devel >= 5:1.6
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	intltool >= 0.35
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_check_so 1

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
Requires:	glib2-devel >= 1:2.2.0
Requires:	gtk+2-devel >= 2:2.4.0
Requires:	guile-devel >= 5:1.6

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
%patch -P0 -p1

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

# on TI i have that locales under different names mv worked fine for me
mv $RPM_BUILD_ROOT%{_localedir}/{nl_NL,nl}
mv $RPM_BUILD_ROOT%{_localedir}/{de_DE,de}
mv $RPM_BUILD_ROOT%{_localedir}/{es_ES,es}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgeda.la

%find_lang %{name}33

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}33.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libgeda.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgeda.so.33
%{_datadir}/gEDA
%{_datadir}/gEDA/scheme
%{_docdir}/geda-doc

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgeda.so
%{_includedir}/%{name}
%{_pkgconfigdir}/libgeda.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgeda.a
