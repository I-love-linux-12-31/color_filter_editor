%define _topdir %(pwd)/rpmbuild
%define debug_package %{nil}
Name:           color-filter-editor
Version:        1.2.6
Release:        1%{?dist}
Summary:        Color Filter Editor GUI Application

License:        BSD-2-Clause license
URL:            https://github.com/I-love-linux-12-31/color_filter_editor
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3
Requires:       python3-psutil
Requires:       python3-pyqt6

%description
This program allows you to change the brightness of the display and the intensity of individual colors in systems with the X11 graphics server for each video output separately.

%prep
%setup -q -c

%build
# None

%install
rm -rf %{buildroot}
install -d %{buildroot}/opt/%{name}/cfe
install -d %{buildroot}%{_datadir}/applications

cp -r cfe %{buildroot}/opt/%{name}/
install -m 755 run_cfe.sh %{buildroot}/opt/%{name}/
install -m 644 LICENSE.md README.md %{buildroot}/opt/%{name}/
install -m 755 cfe.desktop %{buildroot}%{_datadir}/applications/


%files
/opt/%{name}
/opt/%{name}/run_cfe.sh
/opt/%{name}/LICENSE.md
/opt/%{name}/README.md
%{_datadir}/applications/cfe.desktop


%post
chmod 755 /opt/%{name}
chmod 755 /opt/%{name}/run_cfe.sh
chmod 755 /opt/%{name}/cfe
chmod 755 /opt/%{name}/cfe/*

%changelog
* Wed Oct 23 2024 Yaroslav Kuznetsov <yaroslav.12.31.dev@gmail.com>  - 1.2.6
- Initial RPM release