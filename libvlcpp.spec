%global commit0 e81b9f06493becabeec794e351bb357a90af264a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           libvlcpp
Version:        0.1.0
Release:        11.%{?shortcommit0}git%{?dist}
Summary:        C++ bindings for libvlc

License:        LGPLv2+
URL:            https://code.videolan.org/videolan/libvlcpp
Source0:        %{url}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:         libvlcpp-%{version}-pkgconfig.patch

BuildArch: noarch

BuildRequires: libtool
BuildRequires: gcc-c++

%description
C++ bindings for libvlc.

%package        devel
Summary:        Development files for %{name}

%description    devel
C++ bindings for libvlc.


%prep
%autosetup -p1 -n %{name}-%{commit0}
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
* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-11.e81b9f0git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-10.e81b9f0git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-9.e81b9f0git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-8.e81b9f0git
- Update to current snapshot

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-7.20180206git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-6.20180206git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-5.20180206git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.0-4.20180206git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.0-3.20180206git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-2.20180206git
- Update snapshot

* Mon Sep 04 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-1
- Initial spec file
