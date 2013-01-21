Summary:	Ready-to-use GTK+ dialog boxes
Name:		gtkdialogs
Version:	2.2
Release:	10
License:	GPL
Group:		System/Configuration/Packaging
Source:		%{name}-%{version}.tar.bz2
Patch0:		gtkdialogs-2.2-fix-str-fmt.patch
Patch1:		gtkdialogs-2.2-no-strip.patch
Provides:	gchooser = %{version}-%{release}
Provides:	gmessage = %{version}-%{release}
Provides:	xtest = %{version}-%{release}
BuildRequires:	pkgconfig(gtk+-2.0)

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
%patch1 -p1

%build
make clean
%make CFLAGS="%{optflags} %{?ldflags}"

%install
make prefix=%{buildroot} install

%files
%{_bindir}/*

