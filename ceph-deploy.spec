#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ceph-deploy
Version  : 2.0.1
Release  : 17
URL      : https://files.pythonhosted.org/packages/1f/15/8dcbd2054670a8761d6484e588739cac5681e5661e9379862d121188b545/ceph-deploy-2.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/1f/15/8dcbd2054670a8761d6484e588739cac5681e5661e9379862d121188b545/ceph-deploy-2.0.1.tar.gz
Summary  : Deploy Ceph with minimal infrastructure
Group    : Development/Tools
License  : MIT
Requires: ceph-deploy-bin = %{version}-%{release}
Requires: ceph-deploy-license = %{version}-%{release}
Requires: ceph-deploy-python = %{version}-%{release}
Requires: ceph-deploy-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
ceph-deploy -- Deploy Ceph with minimal infrastructure
        ========================================================
        
        ``ceph-deploy`` is a way to deploy Ceph relying on just SSH access to
        the servers, ``sudo``, and some Python. It runs fully on your
        workstation, requiring no servers, databases, or anything like that.
        
        If you set up and tear down Ceph clusters a lot, and want minimal
        extra bureaucracy, this is for you.
        
        This ``README`` provides a brief overview of ceph-deploy, for thorough

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

%description python3
python3 components for the ceph-deploy package.


%prep
%setup -q -n ceph-deploy-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545875138
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ceph-deploy
cp LICENSE %{buildroot}/usr/share/package-licenses/ceph-deploy/LICENSE
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
/usr/share/package-licenses/ceph-deploy/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
