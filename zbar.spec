%define	hgtag	38e78368283d

%define	major	0
%define	libname	%mklibname %{name} %{major}
%define	libgtk	%mklibname %{name}gtk %{major}
%define	libqt	%mklibname %{name}qt %{major}
%define	devname	%mklibname -d %{name}

Name:		zbar
Summary:	Bar Code Reader software suite for reading bar codes from various sources
Version:	0.10
Release:	2.20121014.4
License:	GPLv2+
Group:		Graphics
URL:		http://sourceforge.net/projects/%{name}/
Source0:	http://zbar.hg.sourceforge.net/hgweb/zbar/zbar/archive/%{hgtag}.tar.bz2
Patch0:		zbar-automake-1.2.patch
BuildRequires:	git
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(QtCore) pkgconfig(QtGui)
BuildRequires:	xmlto
BuildRequires:	pkgconfig(GraphicsMagick++)
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
%setup -qn %{name}-%{hgtag}
%patch0 -p1 -b .aytomake~
autoreconf -fi

%build
%configure2_5x	--without-java
%make

%install
%makeinstall_std 

%files
%{_bindir}/zbarcam
%{_bindir}/zbarimg
%doc %{_datadir}/doc/%{name}/*
%{_mandir}/man1/zbarcam.1*
%{_mandir}/man1/zbarimg.1*

%files -n %{libname}
%{_libdir}/libzbar.so.%{major}*

%files -n %{libgtk}
%{_libdir}/libzbargtk.so.%{major}*

%files -n %{libqt}
%{_libdir}/libzbarqt.so.%{major}*

%files -n python-%{name}
%{py_platsitedir}/zbar.so
%{py_platsitedir}/zbarpygtk.so

%files -n %{devname}
%{_includedir}/zbar.h
%dir %{_includedir}/zbar
%{_includedir}/zbar/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libzbar.so
%{_libdir}/libzbargtk.so
%{_libdir}/libzbarqt.so
