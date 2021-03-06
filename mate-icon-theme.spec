# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.16

# Settings used for build from snapshots.
%{!?rel_build:%global commit cdb0d70862035cd1b65c4deb495ea1016ea2d206}
%{!?rel_build:%global commit_date 20150530}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           mate-icon-theme
Version:        %{branch}.0
%if 0%{?rel_build}
Release:        1%{?dist}
%else
Release:        0.6%{?git_rel}%{?dist}
%endif
Summary:        Icon theme for MATE Desktop
License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-icon-theme.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildArch:      noarch

BuildRequires:  mate-common 
BuildRequires:  icon-naming-utils

Obsoletes: mate-icon-theme-devel

%description
Icon theme for MATE Desktop


%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# for snapshots
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
%configure  --enable-icon-mapping

make %{?_smp_mflags} V=1


%install
%{make_install}

%post
/bin/touch --no-create %{_datadir}/icons/mate &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/menta &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/mate &> /dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/mate &> /dev/null || :
    /bin/touch --no-create %{_datadir}/icons/menta &> /dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/menta &> /dev/null || :

fi

%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/mate &> /dev/null || :
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/menta &> /dev/null || :

%files
%doc AUTHORS COPYING README
%{_datadir}/icons/mate
%{_datadir}/icons/menta


%changelog
* Wed Sep 21 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release

* Tue Apr 05 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0 release

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Wed Oct 21 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.0-1
- update to 1.11.0 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-1
- update to 1.10.1 release

* Sat May 30 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-0.5.git201500530.cdb0d70
- update to latest git snapshot from 2015-05-30

* Tue May 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-0.3.git201500505.c6e5c6c
- update to latest git snapshot from 2015-05-05

* Thu Apr 23 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-0.2.git20150423.375037b
- update to latest git snapshot from 2015-04-23

* Mon Apr 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0 release

* Wed Feb 25 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90.1
- update to 1.9.90 release

* Tue Jan 20 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-1
- update to 1.9.1 release

* Wed Dec 31 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-0.1.git20141231.96d5cf2
- update to latest git snapshot from 2014.12.31
- add missing symbolic icons

* Sat Jul 12 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-1
- update to 1.9.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Sun Feb 16 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90 release

* Sun Feb 09 2014 Dan Mashal <dan.mashal@fedoraproject.org>  1.7.1-1
- Update to 1.7.1

* Sat Jan 4 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.1-0.1.git20140101.19719ce
- update to latest git snapshot
- make Maintainers life easier and use better git snapshot usage
- use modern 'make install' macro
- do not own /usr/share/pkgconfig

* Thu Oct 24 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.3-0.2.git48f9063
- update to latest git version
- symbolic icons are removed from menta. already in mate icon-theme
- Menta, fix Inherits in index.theme

* Fri Sep 13 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.3-0.1.git3159523
- update to latest git version
- add icons for bluedevil

* Tue Sep 03 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.2-1
- update to 1.6.2
- remove pkgdir patch, fixed in upstream

* Mon Aug 26 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.6.2-0.2.git26ccf0d
- drop -devel subpkg (for just a pkgconfig file)
- move pkgconfig back to datadir

* Sun Aug 25 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.2-0.1.git26ccf0d
- update to latest git version
- add sympolic icons to mate icon theme
- fix pkgconfig dir

* Mon Aug 05 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-2
- fix package for f20 mass rebuild
- remove NOCONFIGURE=1 ./autogen.sh
- remove needless provides

* Tue Jun 11 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-1
- Update to latest 1.6.1 stable release
- added symbolic icon-theme,fix #965358

* Wed Apr 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-1
- Update to latest 1.6.0 stable release.

* Mon Mar 25 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-1
- Update to latest upstream release
- Drop obsoletes tag
- Own icons/mate dir 

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 30 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-1
- update to 1.5.0 release

* Mon Aug 13 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.4.0-6
- add obsolete mate-icon-theme-legacy
- bump version to 1.4.0-6 for updating external repo

* Sun Aug 12 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-3
- Make the scriptlets reference mate instead of hicolor

* Sun Aug 12 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-2
- Add macros for icon cache, move autogen to prep section

* Fri Aug 10 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-1
- Initial release
