# Restore old style debuginfo creation for rpm >= 4.14.
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# -*- rpm-spec -*-
BuildRoot:      %_topdir/solverapp-0.1.1-Linux
Summary:        Solves quadratic equations, yo
Name:           solverapp
Version:        0.1.1
Release:        1
License:        unknown
Group:          unknown
Vendor:         SodAcetate















Prefix: /usr





%define _rpmdir %_topdir/RPMS
%define _srcrpmdir %_topdir/SRPMS
%define _rpmfilename solverapp-0.1.1-Linux.rpm
%define _unpackaged_files_terminate_build 0




%description


# This is a shortcutted spec file generated by CMake RPM generator
# we skip _install step because CPack does that for us.
# We do only save CPack installed tree in _prepr
# and then restore it in build.
%prep
mv $RPM_BUILD_ROOT %_topdir/tmpBBroot

%install
if [ -e $RPM_BUILD_ROOT ];
then
  rm -rf $RPM_BUILD_ROOT
fi
mv %_topdir/tmpBBroot $RPM_BUILD_ROOT



%clean

%post



%postun


%pre


%preun


%files
%defattr(-,root,root,-)
"/usr/bin/solver"




%changelog
* Sun Jul 4 2010 Eric Noulard <eric.noulard@gmail.com> - 0.1.1-1
  Generated by CPack RPM (no Changelog file were provided)


