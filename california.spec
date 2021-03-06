Summary:	California - GNOME 3 Calendar
Summary(pl.UTF-8):	California - kalendarz dla GNOME 3
Name:		california
Version:	0.4.0
Release:	7
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/california/0.4/%{name}-%{version}.tar.xz
# Source0-md5:	cd8fa9cc399ee918e55b051e3b9f3124
Patch0:		evolution-data-server-3.14.patch
Patch1:		vala.patch
URL:		https://wiki.gnome.org/Apps/California
BuildRequires:	evolution-data-server-devel >= 3.8.5
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gnome-online-accounts-devel >= 3.8.3
BuildRequires:	gobject-introspection-devel >= 1.38.0
BuildRequires:	gtk+3-devel >= 3.12.2
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgdata-devel >= 0.14.0
BuildRequires:	libgee-devel >= 0.10.5
BuildRequires:	libsoup-devel >= 2.44
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	vala-evolution-data-server >= 3.8.5
BuildRequires:	vala-libgee
# because of broken test XDG_EMAIL passing doesn't suffice
BuildRequires:	xdg-utils
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.38.0
# requires e-d-s (not just -libs) to start
Requires:	evolution-data-server >= 3.8.5
Requires:	glib2 >= 1:2.38.0
Requires:	gnome-online-accounts-libs >= 3.8.3
Requires:	gtk+3 >= 3.12.2
Requires:	libsoup >= 2.44
Requires:	xdg-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
California is a calendar built for GNOME 3. It allows you to view and
manage your online calendars with a simple and modern interface.

%description -l pl.UTF-8
California to kalendarz napisany dla GNOME 3. Pozwala na przeglądanie
i zarządzanie kalendarzami online poprzez prosty i nowoczesny
interfejs.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure 
# cannot pass because it's not equal "yes" (see xdg-utils BR note above)
#	XDG_EMAIL=/usr/bin/xdg-email

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/california

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_bindir}/california
%{_datadir}/appdata/california.appdata.xml
%{_datadir}/california
%{_datadir}/glib-2.0/schemas/org.yorba.california.gschema.xml
%{_desktopdir}/california.desktop
