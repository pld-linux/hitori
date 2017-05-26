Summary:	Hitori puzzle game for GNOME
Summary(pl.UTF-8):	Hitori - układanka logiczna dla GNOME
Name:		hitori
Version:	3.22.3
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/hitori/3.22/%{name}-%{version}.tar.xz
# Source0-md5:	291a3576f8842102ee52f4e421f98cef
URL:		https://wiki.gnome.org/Apps/Hitori
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.4
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+3-devel >= 3.15.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.32.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.15.0
Requires:	hicolor-icon-theme >= 0.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hitori is a small application written to allow one to play the
eponymous puzzle game, which is similar in theme to more popular
puzzles such as Sudoku.

%description -l pl.UTF-8
Hitori to mała aplikacja pozwalająca na grę w tytułową układankę
logiczną - bardzo podobną tematycznie do bardziej popularnych, takich
jak Sudoku.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/hitori
%{_datadir}/appdata/org.gnome.Hitori.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.hitori.gschema.xml
%{_desktopdir}/org.gnome.Hitori.desktop
%{_iconsdir}/hicolor/*/apps/org.gnome.Hitori.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Hitori-symbolic.svg
