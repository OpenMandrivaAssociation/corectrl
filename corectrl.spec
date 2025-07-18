Name:           corectrl
Version:        1.5.1
Release:        1
Summary:        Hardware control tools with nice GUI for Linux
License:        GPLv3+
URL:            https://gitlab.com/corectrl/corectrl
Source0:        https://gitlab.com/corectrl/corectrl/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
#Patch0:		corectrl-v1.0.5-makeinstall.patch

#Qt stack
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickTemplates2)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(VulkanHeaders)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(botan-2)
BuildRequires:  pkgconfig(quazip1-qt6)
BuildRequires:  pkgconfig(x11)
BuildRequires:  atomic-devel
BuildRequires:  stdc++-static-devel
BuildRequires:  desktop-file-utils

%ifarch %{ix86}
BuildRequires:  atomic-devel
%endif

Requires:       dbus
Requires:       hicolor-icon-theme
Requires:       polkit
Requires:	    qt6-qtdeclarative
#Requires:       qt5-qtquickcontrols2
# For pidof (???)
Requires:       procps-ng
Requires:       sysvinit-tools
# For pci.ids
Requires:       hwdata

Recommends:     glxinfo
Recommends:     mesa-demos
# For lscpu
Recommends:     util-linux
Recommends:    vulkan-tools

%description
CoreCtrl is a linux application that allows you to control 
with ease your computer hardware using application profiles.
The default settings are defined on a global profile. 
You can also create as many custom profiles as you want, each of them defining its own settings. 
Each custom profile is associated to one program executable. 
When the associated program is launched, the settings of the profile will be applied automatically. 
Later on, when the program ends, the previous settings are restored.
You can choose which elements of the system will be controlled by a profile, 
even for the global profile. In this way, some parts of the system will be left untouched when the profile is applied. 
This will allow you to control those parts using other applications 
or define a global behavior for a part while controlling other parts with custom profiles. 
See How profiles works for more info on this topic.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build

# Build on i686 with lld linker gives error "has non-ABS relocation R_386_GOTOFF against symbol '.LC12'"
# So for i686 we switch to gold linker and to GCC (angry)
%ifarch %{ix86}
export CC=gcc
export CXX=g++
%global ldflags %{ldflags} -fuse-ld=gold
%endif

%cmake  \
      -DCMAKE_BUILD_TYPE=Release \
      -DBUILD_TESTING=OFF \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -G Ninja
%ninja_build

sed -i -- 's/\/usr/${CMAKE_INSTALL_PREFIX}/g' src/helper/cmake_install.cmake

%install
%ninja_install -C build

%files
%{_bindir}/corectrl
%{_libdir}/libcorectrl.so
%{_prefix}/libexec/corectrl/corectrl_helper
%{_prefix}/libexec/corectrl/corectrl_helperkiller
%{_datadir}/applications/org.corectrl.CoreCtrl.desktop
%{_datadir}/dbus-1/system-services/org.corectrl.helper.service
%{_datadir}/dbus-1/system-services/org.corectrl.helperkiller.service
%{_datadir}/dbus-1/system.d/org.corectrl.helper.conf
%{_datadir}/dbus-1/system.d/org.corectrl.helperkiller.conf
%{_datadir}/icons/*/*/apps/corectrl.*
%{_datadir}/metainfo/org.corectrl.CoreCtrl.appdata.xml
%{_datadir}/polkit-1/actions/org.corectrl.helper.policy
%{_datadir}/polkit-1/actions/org.corectrl.helperkiller.policy
