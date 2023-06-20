%define codemirror_ver 5.18.2
%define beta beta

Summary:	A Linux clone of Notepad++
Name:		notepadqq
Version:	2.0.0
Release:	%{?beta:0.%{beta}.}1
License:	GPLv3
Group:		Editors
URL:		https://github.com/notepadqq/notepadqq/
Source0:	https://github.com/notepadqq/notepadqq/archive/refs/tags/v%{version}%{?beta:-%{beta}}.tar.gz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5WebSockets)
BuildRequires:	pkgconfig(Qt5WebEngineCore)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	qmake5
BuildRequires:	qt5-qttools
BuildRequires:	qt5-qtbase-devel

%description
Notepadqq is a Notepad++-like editor for the Linux desktop.

%prep
%autosetup -p1 -n %{name}-%{version}%{?beta:-%{beta}}
# (tpg) fix libdir
sed -i -e "s/lib$/%{_lib}/g;s|lib/|%{_lib}/|g" src/ui/ui.pro

./configure --qmake=%{_libdir}/qt5/bin/qmake --lrelease=%{_libdir}/qt5/bin/lrelease --prefix=%{_prefix}

%build
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
ln -sf %{_libdir}/notepadqq/notepadqq-bin %{buildroot}%{_bindir}/notepadqq-bin

%files
%doc README.md
%{_bindir}/notepadqq*
%{_libdir}/notepadqq
%{_datadir}/applications/notepadqq.desktop
%{_iconsdir}/hicolor/*/apps/notepadqq.*g
%{_datadir}/notepadqq
%{_datadir}/metainfo/*.xml
