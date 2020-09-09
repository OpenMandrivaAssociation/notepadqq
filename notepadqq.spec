%define codemirror_ver 5.18.2

Summary:	A Linux clone of Notepad++
Name:		notepadqq
Version:	1.4.8
Release:	1
License:	GPLv3
Group:		Editors
URL:		http://notepadqq.altervista.org/wp/
Source0:	https://github.com/notepadqq/notepadqq/archive/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	qmake5
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qtbase-devel

%description
Notepadqq is a Notepad++-like editor for the Linux desktop.

%prep
%setup -q
# (tpg) fix libdir
sed -i -e "s/lib/%{_lib}/g" src/ui/ui.pro

./configure --qmake=%{_libdir}/qt5/bin/qmake --lrelease=%{_libdir}/qt5/bin/lrelease --prefix=%{_prefix}

%build
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
ln -sf %{_libdir}/notepadqq/notepadqq-bin %{buildroot}%{_bindir}/notepadqq-bin

%files
%doc README.md
%{_bindir}/notepadqq*
%{_libdir}/notepadqq/notepadqq-bin
%{_datadir}/applications/notepadqq.desktop
%{_iconsdir}/hicolor/*/apps/notepadqq.*g
%{_datadir}/notepadqq
%{_datadir}/metainfo/*.xml
