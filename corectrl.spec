

Name:           corectrl
Version:        1.0.5
Release:        1
Summary:        Hardware control tools with nice GUI for Linux
License:        GPLv3+
URL:            https://gitlab.com/corectrl/corectrl
Source0:        https://gitlab.com/corectrl/corectrl/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

#Qt stack
BuildRequires:  cmake
cmake(Qt5Core)
cmake(Qt5DBus)
cmake(Qt5Charts)
cmake(Qt5Widgets)
cmake(Qt5Network)

#Qt QML stack
