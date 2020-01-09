%define ver 1.3.1

Name: libcxgb3
Version: 1.3.1
Release: 1%{?dist}
Summary: Chelsio T3 RNIC Open Fabrics Userspace Library

Group: System Environment/Libraries
License: GPL/BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/cxgb3/%{name}-%{ver}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libibverbs-devel

%description
libcxgb3 provides a device-specific userspace driver for Chelsio RNICs
for use with the libibverbs library.

%package devel
Summary: Development files for the libcxgb3 driver
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Static version of libcxgb3 that may be linked directly to an
application, which may be useful for debugging.

%prep
%setup -q -n %{name}-%{ver}

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/libcxgb3*.so
%doc AUTHORS COPYING ChangeLog README
%config %{_sysconfdir}/libibverbs.d/cxgb3.driver

%files devel
%defattr(-,root,root,-)
%{_libdir}/libcxgb3*.a

%changelog
