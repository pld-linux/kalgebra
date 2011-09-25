%define		_state		stable
%define		orgname		kalgebra

Summary:	K Desktop Environment - Mathematical calculator
Name:		kalgebra
Version:	4.7.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	c9ed66f8727afa1945767fd8800c6495
URL:		http://www.kde.org/
BuildRequires:	OpenGL-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	readline-devel
Obsoletes:	kde4-kdeedu-kalgebra < 4.6.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAlgebra is a mathematical calculator based on MathML content markup
language.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libanalitza.so.?
%attr(755,root,root) %{_libdir}/libanalitza.so.*.*.*
%attr(755,root,root) %{_libdir}/libanalitzagui.so.?
%attr(755,root,root) %{_libdir}/libanalitzagui.so.*.*.*
%attr(755,root,root) %{_bindir}/kalgebra
%attr(755,root,root) %{_bindir}/kalgebramobile
%{_desktopdir}/kde4/kalgebra.desktop
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_kalgebra.so
%{_datadir}/kde4/services/kalgebraplasmoid.desktop
%{_iconsdir}/hicolor/*x*/apps/kalgebra.png
%{_datadir}/apps/katepart/syntax/kalgebra.xml
%attr(755,root,root) %{_bindir}/calgebra
%{_datadir}/kde4/servicetypes/kalgebrascript.desktop
%{_desktopdir}/kde4/kalgebramobile.desktop
%{_datadir}/apps/kalgebra
