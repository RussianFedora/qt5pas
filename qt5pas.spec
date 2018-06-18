Name:           qt5pas
Version:        1.2.6
Release:        1%{?dist}
Summary:        Qt 5 bindings for pascal

License:        LGPLv3+
URL:            https://github.com/graemeg/lazarus/tree/upstream/lcl/interfaces/qt5/cbindings
Source0:        http://downloads.sourceforge.net/project/lazarus/Lazarus%20Zip%20_%20GZip/Lazarus%20%{version}/lazarus-1.8.0.tar.gz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

ExclusiveArch:  %{fpc_arches}


%description
Qt 5 bindings for pascal from Lazarus.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n lazarus


%build
pushd lcl/interfaces/qt5/cbindings/
    %{qmake_qt5}
    %make_build
popd


%install
pushd lcl/interfaces/qt5/cbindings/
    %make_install INSTALL_ROOT=%{buildroot}
popd


%files
%license lcl/interfaces/qt5/cbindings/COPYING.TXT
%doc lcl/interfaces/qt5/cbindings/README.TXT
%{_libdir}/libQt5Pas.so.*

%files devel
%{_libdir}/libQt5Pas.so


%changelog
* Mon Feb 26 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.6-1
- Initial package
