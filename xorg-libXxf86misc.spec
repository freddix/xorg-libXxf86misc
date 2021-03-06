Summary:	Xxf86misc library
Name:		xorg-libXxf86misc
Version:	1.0.3
Release:	6
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86misc-%{version}.tar.bz2
# Source0-md5:	6bc0bf78909fd71021c466c793d4385c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xxf86misc library.

%package devel
Summary:	Header files for libXxf86misc library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Xxf86misc library.

This package contains the header files needed to develop programs that
use libXxf86misc.

%prep
%setup -qn libXxf86misc-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXxf86misc.so.?
%attr(755,root,root) %{_libdir}/libXxf86misc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXxf86misc.so
%{_pkgconfigdir}/xxf86misc.pc
%{_mandir}/man3/*.3x*

