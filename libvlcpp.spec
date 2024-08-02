%global commit0 d76fe0678e92ada5897eac975e14edc9981130e8
%global gitdate 20230527
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           libvlcpp
Version:        0.1.0
Release:        17.%{gitdate}git%{shortcommit0}%{?dist}
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


%build
./bootstrap
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
* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.0-17.20230527gitd76fe06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.0-16.20230527gitd76fe06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 23 2023 Sérgio Basto <sergio@serjux.com> - 0.1.0-15.20230527gitd76fe06
- Try build it without the hack

* Thu Aug 03 2023 Sérgio Basto <sergio@serjux.com> - 0.1.0-14.20230527gitd76fe06
- Update to current snapshot

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.0-13.e81b9f0git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.0-12.e81b9f0git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

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
