%global debug_package %{nil}
# Global variables for github repository
%global commit0 76710ef20120432a4a9aab1949fde71c0de93781
%global gittag0 B2
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commit1 2a1477550cc122dcac8af7016ac5f15dec2e139a
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})
%global commit2 4ca2b08d007c0cd17665f6f19fb160a3c111024b
%global shortcommit2 %(c=%{commit2}; echo ${c:0:7})

Name: looking-glass-client
Version: B2
Release: 2%{?dist}
Summary: VGA PCI Pass-through receiver leveraging IVSHMEM

License: GPL-2.0
URL: https://looking-glass.io/
Source0: https://github.com/gnif/LookingGlass/archive/%{commit0}.tar.gz#/LookingGlass-%{commit0}.tar.gz
Source1: https://github.com/gnif/LGMP/archive/%{commit1}.tar.gz
Source2: https://github.com/gnif/PureSpice/archive/%{commit2}.tar.gz

BuildRequires: make gcc cmake binutils-devel SDL2-devel SDL2_ttf-devel nettle-devel spice-protocol fontconfig-devel libX11-devel egl-wayland-devel wayland-devel mesa-libGLU-devel mesa-libGLES-devel mesa-libGL-devel mesa-libEGL-devel libXfixes-devel libXi-devel

%description
VGA PCI Pass-through receiver leveraging IVSHMEM

%prep
%setup -n LookingGlass-%{commit0} -a1 -a2
rm -rf repos/{LGMP,PureSpice}
mv LGMP-%{commit1} repos/LGMP
mv PureSpice-%{commit2} repos/PureSpice

%build
mkdir -p client/build
cd client/build
cmake ../
make

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 client/build/%{name} %{buildroot}/%{_bindir}/

%files
%{_bindir}/%{name}
%license

%changelog
* Sat Nov 14 2020 Drew DeVore <drew@devorcula.com> - 3.6-1
- Initial build
