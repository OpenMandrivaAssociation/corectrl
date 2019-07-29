

Name:           corectrl
Version:        1.0.5
Release:        1
Summary:        Hardware control tools with nice GUI for Linux
License:        GPLv3+
URL:            https://gitlab.com/corectrl/corectrl
Source0:        https://gitlab.com/corectrl/corectrl/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

#Qt stack
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Charts)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5QuickTemplates2)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(botan-2)
BuildRequires:  pkgconfig(x11)

BuildRequires:  desktop-file-utils
