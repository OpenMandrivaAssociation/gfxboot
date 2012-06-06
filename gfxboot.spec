Name:		gfxboot
Version:	4.5.0
Release:	1
Summary:	Tools to create graphical boot logos
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://en.opensuse.org/Gfxboot
BuildRequires:	nasm
BuildRequires:	xmlto
BuildRequires:	lynx
BuildRequires:	docbook-dtd412-xml
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(freetype2)
ExclusiveArch:	%{ix86} x86_64
Patch0:		gfxboot-4.3.8-mandriva.patch
Patch1:		gfxboot-4.3.8-link.patch

%description
gfxboot provides tools to create graphical boot logos, for grub, lilo
and syslinux. It supports arch-specific boot menus, advanced help
menus, multiple keymaps, animated images, and more graphical pretty
things.

%package	devel
License:	GPLv2+
Summary:	Tools for creating a graphical boot logo
Group:		System/Kernel and hardware
Requires:	gfxboot = %{EVRD}
%if "%{distepoch}" >= "2011.0"
Requires:	master-boot-code
%endif
Requires:	qemu

%description devel
Here you find the necessary programs to create your own graphical boot
logo. The logo can be used with grub, lilo or syslinux.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%make CFLAGS="%{optflags} %{ldflags}"
%make doc

%install
%makeinstall_std THEMES=""
install -m644 doc/gfxboot.8 -D %{buildroot}%{_mandir}/man8/gfxboot.8

# add adddir and keymapchars since they are used in mandriva-gfxboot-theme
# build system
install -m755 bin/adddir -D %{buildroot}%{_bindir}/gfxboot-adddir
install -m755 bin/keymapchars -D %{buildroot}%{_bindir}/gfxboot-keymapchars
# gfxboot-compile is used to build as non-root, move it out of /usr/sbin
mv %{buildroot}%{_sbindir}/gfxboot-compile %{buildroot}%{_bindir}/gfxboot-compile
mv %{buildroot}%{_sbindir}/gfxboot-font %{buildroot}%{_bindir}/gfxboot-font

%files
%{_sbindir}/gfxboot
%{_sbindir}/gfxtest
%{_mandir}/man8/*

%files devel
%doc doc/gfxboot.html doc/gfxboot.txt
%{_bindir}/gfxboot-compile
%{_bindir}/gfxboot-font
%{_bindir}/gfxboot-adddir
%{_bindir}/gfxboot-keymapchars
