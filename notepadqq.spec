%define codemirror_ver 5.18.2
%define beta beta
%undefine _debugsource_packages

Summary:	A Linux clone of Notepad++
Name:		notepadqq
Version:	2.0.0
Release:	%{?beta:0.%{beta}.}2
License:	GPLv3
Group:		Editors
URL:		https://github.com/notepadqq/notepadqq/
Source0:	https://github.com/notepadqq/notepadqq/archive/refs/tags/v%{version}%{?beta:-%{beta}}.tar.gz
Patch:		https://github.com/notepadqq/notepadqq/commit/c7b02f1d75bfe247ec377c86f950cd88f9df8288.patch
Patch1:		notepadqq-qt6.patch
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6WebSockets)
BuildRequires:	pkgconfig(Qt6WebEngineCore)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(uchardet)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	qmake-qt6
BuildRequires:	qt6-qttools

%description
Notepadqq is a Notepad++-like editor for the Linux desktop.

%prep
%autosetup -p1 -n %{name}-%{version}%{?beta:-%{beta}}
# (tpg) fix libdir
sed -i -e "s/lib$/%{_lib}/g;s|lib/|%{_lib}/|g" src/ui/ui.pro

./configure --qmake=%{_libdir}/qt6/bin/qmake --lrelease=%{_libdir}/qt6/bin/lrelease --prefix=%{_prefix}

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
