%global debug_package %{nil}
# Global variables for github repository
%global commit0 2973319bff80bf1531265bdbec6707bdda3f40eb
%global gittag0 B3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commit1 8ddc0da9ddbfb8c7c91553c939055582da86abfc
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})
%global commit2 00961e8f43c55356df847d6f5753560d12158165
%global shortcommit2 %(c=%{commit2}; echo ${c:0:7})

Name: looking-glass-client
Version: B3
Release: 1%{?dist}
Summary: VGA PCI Pass-through receiver leveraging IVSHMEM

License: GPL-2.0
URL: https://looking-glass.io/
Source0: https://github.com/gnif/LookingGlass/archive/%{commit0}.tar.gz#/LookingGlass-%{commit0}.tar.gz
Source1: https://github.com/gnif/LGMP/archive/%{commit1}.tar.gz
Source2: https://github.com/gnif/PureSpice/archive/%{commit2}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: cmake
BuildRequires: binutils-devel
BuildRequires: SDL2-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: nettle-devel
BuildRequires: spice-protocol
BuildRequires: fontconfig-devel
BuildRequires: libX11-devel
BuildRequires: egl-wayland-devel
BuildRequires: wayland-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: mesa-libGLES-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libEGL-devel
BuildRequires: libXfixes-devel
BuildRequires: libXi-devel
BuildRequires: libXScrnSaver-devel

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
* Sat Apr 17 2021 Drew DeVore <drew@devorcula.com> - B3
- Update to latest version

* Sat Nov 14 2020 Drew DeVore <drew@devorcula.com> - B2
- Initial build
