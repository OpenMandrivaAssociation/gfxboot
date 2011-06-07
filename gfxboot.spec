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
BuildRequires:	freetype2-devel
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
