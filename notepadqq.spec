Summary:	A Linux clone of Notepad++
Name:		notepadqq
Version:	0.45.1
Release:	1
License:	GPLv3
Group:		System/Libraries
URL:		http://notepadqq.altervista.org/wp/
Source0:	https://github.com/notepadqq/notepadqq/archive/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	qmake5

%description
Notepadqq is a Notepad++-like editor for the Linux desktop.

%prep
%setup -q

%build
%qmake_qt5 *.pro

%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%doc README.md CONTRIBUTORS.md
