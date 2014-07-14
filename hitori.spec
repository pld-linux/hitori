Summary:	Hitori puzzle game for GNOME
Summary(pl.UTF-8):	Hitori - układanka logiczna dla GNOME
Name:		hitori
Version:	0.4.5
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/hitori/0.4/%{name}-%{version}.tar.xz
# Source0-md5:	9a5c0536d76235dd62b194396aa0cccf
URL:		https://wiki.gnome.org/Apps/Hitori
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.4
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hitori is a small application written to allow one to play the
eponymous puzzle game, which is similar in theme to more popular
puzzles such as Sudoku.

%description -l pl.UTF-8
Hitori to mała aplikacja pozwalająca na grę w tytułową układankę
logiczną - bardzo podobną tematycznie do bardziej popularnych,
takich jak Sudoku.

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
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/hitori
%{_datadir}/hitori
%{_datadir}/appdata/hitori.appdata.xml
%{_desktopdir}/hitori.desktop
%{_iconsdir}/hicolor/*/apps/hitori.png
