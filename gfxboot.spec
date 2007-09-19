%define name	gfxboot
%define version	3.3.18
%define release	%mkrel 2

Summary:	Tools to create graphical boot logos
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source1:	SuSE.tar.bz2
Patch0:		gfxboot-3.3.18-mdv.patch
License:	GPL+
Group:		System/Kernel and hardware
URL:		http://en.opensuse.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	nasm
BuildRequires:	xmlto
BuildRequires:	libx11-devel
BuildRequires:	freetype2-devel

%description
gfxboot provides tools to create graphical boot logos, for grub, lilo
and syslinux. It supports arch-specific boot menus, advanced help
menus, multiple keymaps, animated images, and more graphical pretty
things.

%prep
%setup -q -a 1
%patch0 -p1 -b .mdv

%build
%make PRODUCT="Mandriva Linux %mandriva_release"
%make doc

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/gfxboot.html doc/gfxboot.txt
%{_sbindir}/mkblfont
%{_sbindir}/help2txt
%{_sbindir}/mkbootmsg
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/bin/
%{_datadir}/%{name}/themes/

