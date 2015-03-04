%define codemirror_ver 4.7.0

Summary:	A Linux clone of Notepad++
Name:		notepadqq
Version:	0.45.1
Release:	2
License:	GPLv3
Group:		Editors
URL:		http://notepadqq.altervista.org/wp/
Source0:	https://github.com/notepadqq/notepadqq/archive/%{name}-%{version}.tar.gz
Source1:	https://github.com/notepadqq/CodeMirror/archive/CodeMirror-%{codemirror_ver}.tar.gz
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	qmake5

%description
Notepadqq is a Notepad++-like editor for the Linux desktop.

%prep
%setup -q -a 1

# (tpg) install CodeMirror
mv -f CodeMirror-%{codemirror_ver}/* src/editor/libs/codemirror

# (tpg) fix libdir
sed -i -e "s/lib/%{_lib}/g" src/ui/ui.pro

%build
%qmake_qt5 PREFIX=%{_prefix} *.pro

%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%doc README.md CONTRIBUTORS.md
%{_bindir}/notepadqq
%{_libdir}/notepadqq/notepadqq-bin
%{_datadir}/applications/notepadqq.desktop
%{_iconsdir}/hicolor/*/apps/notepadqq.*g
%{_datadir}/notepadqq
