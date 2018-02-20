%define codemirror_ver 5.18.2

Summary:	A Linux clone of Notepad++
Name:		notepadqq
Version:	1.2.0
Release:	2
License:	GPLv3
Group:		Editors
URL:		http://notepadqq.altervista.org/wp/
Source0:	https://github.com/notepadqq/notepadqq/archive/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	qmake5
BuildRequires:  qt5-qttools
BuildRequires:  qtchooser
BuildRequires:  qt5-qtchooser

%description
Notepadqq is a Notepad++-like editor for the Linux desktop.

%prep
%setup -q

mkdir -p src/editor/libs/codemirror/mode/m4

# (tpg) fix libdir
sed -i -e "s/lib/%{_lib}/g" src/ui/ui.pro

%build
%qmake_qt5 PREFIX=%{_prefix} *.pro

%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

# (tpg) bug #1136
ln -sf %{_libdir}/notepadqq/notepadqq-bin %{buildroot}%{_bindir}/notepadqq-bin

%files
%doc README.md CONTRIBUTORS.md
%{_bindir}/notepadqq*
%{_libdir}/notepadqq/notepadqq-bin
%{_datadir}/applications/notepadqq.desktop
%{_iconsdir}/hicolor/*/apps/notepadqq.*g
%{_datadir}/notepadqq
