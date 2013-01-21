%define name	gfxboot
%define version	4.1.19
%define release	%mkrel 8

Summary:	Tools to create graphical boot logos
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		gfxboot-3.3.18-mdv.patch
Patch1:		gfxboot-4.1.19-link.patch
Patch2:		gfxboot-4.1.19-preview-mandriva-defaults.patch
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://en.opensuse.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	nasm
BuildRequires:	xmlto
BuildRequires:	lynx
BuildRequires:  docbook-dtd412-xml
BuildRequires:	libx11-devel
BuildRequires:	pkgconfig(freetype2)
ExclusiveArch:	%{ix86} x86_64

%description
gfxboot provides tools to create graphical boot logos, for grub, lilo
and syslinux. It supports arch-specific boot menus, advanced help
menus, multiple keymaps, animated images, and more graphical pretty
things.

%package        devel
License:        GPLv2+
Summary:        Tools for creating a graphical boot logo
Group:          System/Kernel and hardware
Requires:	gfxboot = %version-%release
%if %mdkversion >= 201100
Requires:	master-boot-code
%endif
Requires:	qemu

%description devel
Here you find the necessary programs to create your own graphical boot
logo. The logo can be used with grub, lilo or syslinux.

%prep
%setup -q
%patch0 -p1 -b .mdv
%patch1 -p0 -b .link
%patch2 -p1

%build
%make CC="cc %optflags %ldflags"
%make doc

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std THEMES=""
install -d -m 755 %{buildroot}%{_mandir}/man8
install -m 644 doc/gfxboot.8 %{buildroot}%{_mandir}/man8

# gfxboot-compile is used to build as non-root, move it out of /usr/sbin
install -d %{buildroot}%{_bindir}
# add adddir and keymapchars since they are used in mandriva-gfxboot-theme
# build system
cp %{_builddir}/%{name}-%{version}/bin/adddir %{buildroot}%{_bindir}/gfxboot-adddir
cp %{_builddir}/%{name}-%{version}/bin/keymapchars %{buildroot}%{_bindir}/gfxboot-keymapchars
mv %{buildroot}%{_sbindir}/gfxboot-compile %{buildroot}%{_bindir}/gfxboot-compile
mv %{buildroot}%{_sbindir}/gfxboot-font %{buildroot}%{_bindir}/gfxboot-font

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sbindir}/gfxboot
%{_mandir}/man8/*

%files devel
%defattr(-,root,root)
%{_bindir}/gfxboot-compile
%{_bindir}/gfxboot-font
%{_bindir}/gfxboot-adddir
%{_bindir}/gfxboot-keymapchars
%doc doc/gfxboot.html
%doc doc/gfxboot.txt


%changelog
* Wed Jun 08 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.1.19-8mdv2011.0
+ Revision: 683308
- Make debugging of gfxboot images simpler

* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 4.1.19-7
+ Revision: 672414
- add br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Mon Dec 20 2010 Funda Wang <fwang@mandriva.org> 4.1.19-6mdv2011.0
+ Revision: 623263
- fix linkage

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1.19-5mdv2010.1
+ Revision: 522725
- rebuilt for 2010.1

* Thu Sep 24 2009 Olivier Blin <oblin@mandriva.com> 4.1.19-4mdv2010.0
+ Revision: 448382
- build gfxboot on x86 only (from Arnaud Patard)

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.1.19-3mdv2010.0
+ Revision: 428508
- add missing BuildRequires
- rebuild
- add 2 binaries that were build but not installed, they are used by mandriva-gfxboot-theme build system

* Tue Jan 27 2009 Pixel <pixel@mandriva.com> 4.1.19-2mdv2009.1
+ Revision: 334055
- add require from gfxboot-devel on gfxboot (same version)

* Thu Jan 22 2009 Pixel <pixel@mandriva.com> 4.1.19-1mdv2009.1
+ Revision: 332569
- 4.1.19
- adapt spec (inspiration: SuSE's spec)

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 3.3.18-4mdv2009.0
+ Revision: 219552
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 20 2007 Adam Williamson <awilliamson@mandriva.org> 3.3.18-2mdv2008.0
+ Revision: 91249
- rebuild for 2008
- new license policy
- slight spec clean


* Tue Dec 05 2006 Pixel <pixel@mandriva.com> 3.3.18-1mdv2007.0
+ Revision: 90945
- add BuildRequires freetype2-devel
- update mdv patch
- new release: 3.3.20
- update mdv patch
- getx11font is now mkblfont
- Import gfxboot

* Fri Jun 23 2006 Olivier Blin <oblin@mandriva.com> 3.2.27-2mdv2007.0
- Source1: add Suse theme as reference (from openSUSE package)
- Patch0: use "Mandriva Linux" as default product in help2txt
- use "Mandriva Linux <release>" as default product when building packaged theme

* Fri Jun 23 2006 Olivier Blin <oblin@mandriva.com> 3.2.27-1mdv2007.0
- initial Mandriva release

