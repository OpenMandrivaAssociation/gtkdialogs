Name:		gtkdialogs
Version:	2.2
Release:	%mkrel 4
Source:		%name-%version.tar.bz2
Patch0:		gtkdialogs-2.2-fix-str-fmt.patch
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Summary:	Ready-to-use GTK+ dialog boxes
Provides:	gchooser gmessage xtest
Group:		System/Configuration/Packaging
BuildRequires:	gtk+2-devel

%description
Ready-to-use GTK+ dialog boxes:
- xtest lets you test if X is running or not
- gmessage show a message and some buttons, it returns with the number of the
  pressed button
- gchooser presents a list of entries from which the user can choose
- gfilechooser helps choosing a filename or dirname

%prep
%setup -n %{name} -q
%patch0 -p0

%build
make clean
%make CFLAGS="%{optflags} %{?ldflags}"

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*


