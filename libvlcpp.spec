%global date 20180206

Name:           libvlcpp
Version:        0.1.0
Release:        2.%{?date}git%{?dist}
Summary:        C++ bindings for libvlc

License:        LGPLv2+
URL:            https://code.videolan.org/videolan/libvlcpp
Source0:        libvlcpp-%{date}.tar.xz
Source9:        libvlcpp-snapshot.sh
Patch0:         libvlcpp-%{version}-pkgconfig.patch

BuildArch: noarch

BuildRequires: libtool


%description
C++ bindings for libvlc.

%package        devel
Summary:        Development files for %{name}

%description    devel
C++ bindings for libvlc.


%prep
%autosetup -p1 -n %{name}-%{date}
./bootstrap


%build
%configure
%make_build


%install
%make_install INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'



%files devel
%doc AUTHORS NEWS
%license COPYING
%{_includedir}/vlcpp/
%{_datadir}/pkgconfig/libvlcpp.pc


%changelog
* Tue Feb 06 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-2.20180206git
- Update snapshot

* Mon Sep 04 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-1
- Initial spec file
