Summary:	Hitori puzzle game for GNOME
Summary(pl.UTF-8):	Hitori - układanka logiczna dla GNOME
Name:		hitori
Version:	3.38.3
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/hitori/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	2d5a56504639be4e12ae6606b7ba4e96
URL:		https://wiki.gnome.org/Apps/Hitori
BuildRequires:	appstream-glib
BuildRequires:	cairo-devel >= 1.4
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-tools >= 0.19.8
# -std=gnu11
BuildRequires:	gcc >= 6:4.7
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	meson >= 0.48.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.32.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.22.0
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%doc AUTHORS MAINTAINERS NEWS README.md
%attr(755,root,root) %{_bindir}/hitori
%{_datadir}/glib-2.0/schemas/org.gnome.hitori.gschema.xml
%{_datadir}/metainfo/org.gnome.Hitori.appdata.xml
%{_desktopdir}/org.gnome.Hitori.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Hitori.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Hitori-symbolic.svg
