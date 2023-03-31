%define	hgtag	38e78368283d5afe34bbc0cedb36d4540cda3a30

%define	major	0
%define	libname	%mklibname %{name} %{major}
%define	libgtk	%mklibname %{name}gtk %{major}
%define	libqt	%mklibname %{name}qt %{major}
%define	devname	%mklibname -d %{name}

Name:		zbar
Summary:	Bar Code Reader software suite for reading bar codes from various sources
Version:	0.23.92
Release:	3
License:	GPLv2+
Group:		Graphics
# See also https://linuxtv.org/downloads/zbar
URL:		https://github.com/mchehab/zbar
Source0:	https://github.com/mchehab/zbar/archive/refs/tags/%{version}.tar.gz
#Patch1:		zbar-qt5.patch
BuildRequires:	git
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(Qt5Core) pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets) pkgconfig(Qt5X11Extras)
BuildRequires:	xmlto
BuildRequires:	pkgconfig(MagickWand)
Requires:	graphicsmagick

%description
ZBar Bar Code Reader is an open source software suite for reading bar
codes from various sources, such as video streams, image files and raw
intensity sensors. It supports EAN-13/UPC-A, UPC-E, EAN-8, Code 128,
Code 39, Interleaved 2 of 5 and QR Code.  Included with the library
are basic applications for decoding captured bar code images and using
a video device (eg, webcam) as a bar code scanner.  For application
developers, language bindings are included for C, C++, Python and Perl
as well as GUI widgets for Qt, GTK and PyGTK.

%package qt
Summary:	Qt frontend for the ZBar barcode reader
Group:		Graphics

%description qt
Qt frontend for the ZBar barcode reader

%package gtk
Summary:	Gtk frontend for the ZBar barcode reader
Group:		Graphics

%description gtk
Gtk frontend for the ZBar barcode reader

%package -n	%{libname}
Summary:	ZBAR Libraries
Group:		System/Libraries
	
%description -n	%{libname}
Libraries for the ZBar Bar Code Reader

%package -n	%{libgtk}
Summary:	ZBAR Libraries
Group:		System/Libraries

%description -n	%{libgtk}
Libraries for the ZBar Bar Code Reader

%package -n	%{libqt}
Summary:	ZBAR Libraries
Group:		System/Libraries

%description -n	%{libqt}
Libraries for the ZBar Bar Code Reader

%package -n	%{devname}
Summary:	ZBAR Development headers and libraries
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	%{libgtk} = %{version}
Requires:	%{libqt} = %{version}

%description -n	%{devname}
Development headers and libraries for the ZBar Bar Code Reader

%package -n	python-%{name}
Summary:	Python bindings for ZBAR
Group:		Development/Python
	
%description -n	python-%{name}
Python bindings for the ZBar Bar Code Reader


#--------------------------------------------------------------------

%prep
%autosetup -p1
autoreconf -fi

%build
# --without-python because python 2.x needs to die
# and 3.x isn't supported yet
%configure	\
	--with-imagemagick \
	--without-java \
	--without-python
%make_build

%install
%makeinstall_std 
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/zbarcam
%{_bindir}/zbarimg
%{_sysconfdir}/dbus-1/system.d/org.linuxtv.Zbar.conf
%doc %{_datadir}/doc/%{name}/*
%{_mandir}/man1/zbarcam.1*
%{_mandir}/man1/zbarimg.1*

%files qt
%{_bindir}/zbarcam-qt

%files gtk
%{_bindir}/zbarcam-gtk

%files -n %{libname}
%{_libdir}/libzbar.so.%{major}*

%files -n %{libgtk}
%{_libdir}/libzbargtk.so.%{major}*
%{_libdir}/girepository-1.0/ZBar-1.0.typelib
%{_datadir}/gir-1.0/ZBar-1.0.gir

%files -n %{libqt}
%{_libdir}/libzbarqt.so.%{major}*

%files -n %{devname}
%{_includedir}/zbar.h
%dir %{_includedir}/zbar
%{_includedir}/zbar/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libzbar.so
%{_libdir}/libzbargtk.so
%{_libdir}/libzbarqt.so
