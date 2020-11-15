%global debug_package %{nil}
# Global variables for github repository
%global commit0 2d390fa7a916fc04fcc65d245b6f594ae1344d7b
%global gittag0 3.6
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: scream
Version: 3.6
Release: 1%{?dist}
Summary: Scream audio receiver using Pulseaudio, ALSA or stdout as audio output.

License: MS-PL
URL: https://github.com/duncanthrax/scream/tree/master/Receivers/unix
Source0: https://github.com/duncanthrax/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake pulseaudio-libs-devel alsa-lib-devel
Requires: pulseaudio

%description
Scream audio receiver using Pulseaudio, ALSA or stdout as audio output.

%prep
%autosetup

%build
cd Receivers/unix
mkdir build
cd build
cmake ..
make

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 Receivers/unix/build/%{name} %{buildroot}/%{_bindir}/

%files
%{_bindir}/scream

%changelog
* Sat Nov 14 2020 Drew DeVore <drew@devorcula.com> - 3.6-1
- Initial build