Summary:	libraries for the gEDA project
Summary(pl):	Biblioteki projektu gEDA
Name:		libgeda
Version:	20010304
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/%{version}/%{name}-%{version}.tar.gz
URL:		http://www.geda.seul.org/
BuildRequires:	guile-devel >= 1.4
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel >= 1.2.8
BuildRequires:	glib-devel >= 1.2.8
BuildRequires:	libstroke-devel >= 0.4
BuildRequires:	libgdgeda-devel >= 1.7
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
%setup -q -n %{name}

%build
LDFLAGS="-L%{_libdir} %{rpmcflags}"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS ChangeLog README TODO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
