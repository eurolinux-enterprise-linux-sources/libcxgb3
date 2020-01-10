Name: libcxgb3
Version: 1.3.1
Release: 5%{?dist}
Summary: Chelsio T3 iWARP HCA Userspace Driver
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/cxgb3/%{name}-%{version}.tar.gz
Source1: libcxgb3-modprobe.conf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libibverbs-devel > 1.1.4, libtool
%ifnarch ia64 %{sparc} %{arm}
BuildRequires: valgrind-devel
%endif
Obsoletes: %{name}-devel
ExcludeArch: s390 s390x
Provides: libibverbs-driver.%{_arch}
%description
Userspace hardware driver for use with the libibverbs InfiniBand/iWARP verbs
library.  This driver enables Chelsio iWARP capable ethernet devices.

%package static
Summary: Static version of the libcxgb3 driver
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
%description static
Static version of libcxgb3 that may be linked directly to an application.

%prep
%setup -q

%build
%ifnarch ia64 %{sparc} %{arm}
%configure --with-valgrind
%else
%configure
%endif
%{__make} %{?_smp_mflags}

%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
install -p -m 644 -D %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/modprobe.d/libcxgb3.conf
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_sysconfdir}/libibverbs.d/*.driver
%{_sysconfdir}/modprobe.d/libcxgb3.conf
%doc AUTHORS COPYING README

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%changelog
* Mon Mar 03 2014 Doug Ledford <dledford@redhat.com> - 1.3.1-5
- Bump and rebuild against updated libibverbs
- Related: bz1062281

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.3.1-4
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 03 2012 Doug Ledford <dledford@redhat.com> - 1.3.1-1
- Update to latest upstream release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 11 2010 Doug Ledford <dledford@redhat.com> - 1.2.5-4
- ExcludeArch s390(x) as the hardware doesn't exist there

* Fri Nov 06 2009 Doug Ledford <dledford@redhat.com> - 1.2.5-3
- Update BuildRequires to reflect the necessary libibverbs release for the
  new verbs API change

* Fri Nov 06 2009 Doug Ledford <dledford@redhat.com> - 1.2.5-2
- Update to libibverbs-1.1.3 API

* Wed Oct 28 2009 Doug Ledford <dledford@redhat.com> - 1.2.5-1
- Update to latest version
- Add provides of libibverbs-driver

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 12 2008 Doug Ledford <dledford@redhat.com> - 1.2.1-1
- Update to latest upstream version
- Submit package to Fedora review process

* Tue Apr 01 2008 Doug Ledford <dledford@redhat.com> - 1.1.4-1
- Update to 1.1.4 to match OFED 1.3
- Add a modprobe conf file in /etc/modprobe.d so that the iw_cxgb3 module
  will always be loaded after the cxgb3 net module
- Related: bz428197

* Thu Feb 14 2008 Doug Ledford <dledford@redhat.com> - 1.1.2-2
- Obsolete the old -devel package (which really was just a static
  lib, no real devel environment, hence the name change to -static)
- Resolves: bz432769

* Fri Jan 25 2008 Doug Ledford <dledford@redhat.com> - 1.1.2-1
- Build against latest libibverbs
- Related: bz428197

* Tue Jan 15 2008 Doug Ledford <dledford@redhat.com> - 1.1.2-0.1
- Initial driver import

