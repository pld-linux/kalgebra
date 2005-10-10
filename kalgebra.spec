%define		_snap	20051006
Summary:	Math-ML based graph calculator
Summary(pl):	Oparty na Math-ML kalkulator wykresów
Name:		kalgebra
Version:	0.%{_snap}.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://download.berlios.de/kalgebra/%{name}.%{_snap}.tar.bz2
# Source0-md5:	69d1b5d1bb8a4c89d4b2e30f16fd73ca
URL:		http://kalgebra.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAlgebra is a MathML-based graph calculator, thought to bring to the
user its power by solving expressions written in MathML or calculating
converted common equations to MathML.

%description -l pl
KAlgebra to oparty na MathML-u kalkulator wykresów, wymy¶lony, aby
dostarczyæ u¿ytkownikom swoj± moc poprzez rozwi±zywanie równañ
napisanych w MathML-u lub obliczanie przekszta³conych do MathML-a
popularnych wyra¿eñ.

%prep
%setup -q -n %{name}.kdevelop

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

mv -f $RPM_BUILD_ROOT{/usr/share/applnk/Utilities/kalgebra.desktop,%{_desktopdir}}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/apps/%{name}
