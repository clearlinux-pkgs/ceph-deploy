#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ceph-deploy
Version  : 2.1.0
Release  : 32
URL      : https://github.com/ceph/ceph-deploy/archive/refs/tags/v2.1.0.tar.gz
Source0  : https://github.com/ceph/ceph-deploy/archive/refs/tags/v2.1.0.tar.gz
Summary  : Deploy Ceph with minimal infrastructure
Group    : Development/Tools
License  : LGPL-2.1 MIT
Requires: ceph-deploy-bin = %{version}-%{release}
Requires: ceph-deploy-license = %{version}-%{release}
Requires: ceph-deploy-python = %{version}-%{release}
Requires: ceph-deploy-python3 = %{version}-%{release}
Requires: python-remoto
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-remoto
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
An easy to use admin tool for deploy ceph storage clusters.

%package bin
Summary: bin components for the ceph-deploy package.
Group: Binaries
Requires: ceph-deploy-license = %{version}-%{release}

%description bin
bin components for the ceph-deploy package.


%package license
Summary: license components for the ceph-deploy package.
Group: Default

%description license
license components for the ceph-deploy package.


%package python
Summary: python components for the ceph-deploy package.
Group: Default
Requires: ceph-deploy-python3 = %{version}-%{release}

%description python
python components for the ceph-deploy package.


%package python3
Summary: python3 components for the ceph-deploy package.
Group: Default
Requires: python3-core
Provides: pypi(ceph_deploy)
Requires: pypi(setuptools)

%description python3
python3 components for the ceph-deploy package.


%prep
%setup -q -n ceph-deploy-2.1.0
cd %{_builddir}/ceph-deploy-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632956229
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ceph-deploy
cp %{_builddir}/ceph-deploy-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/ceph-deploy/7174c56a9bb92796eca0a69ec7a41531c23a275a
cp %{_builddir}/ceph-deploy-2.1.0/debian/copyright %{buildroot}/usr/share/package-licenses/ceph-deploy/8a409a62006175e5dffea6d0840cec86ddac12c0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ceph-deploy

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ceph-deploy/7174c56a9bb92796eca0a69ec7a41531c23a275a
/usr/share/package-licenses/ceph-deploy/8a409a62006175e5dffea6d0840cec86ddac12c0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
