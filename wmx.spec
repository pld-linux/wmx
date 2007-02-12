Summary:	Another window manager
Summary(pl.UTF-8):	Jeszcze jeden zarządca okien
Name:		wmx
Version:	6
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.all-day-breakfast.com/%{name}-%{version}.tar.gz
# Source0-md5:	d4dd5ed28b7aa103f462d4a024c7bb03
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-compile_fix.patch
Patch1:		%{name}-config.patch
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/%{name}

%define		_gcc_ver	%(%{__cc} -dumpversion | cut -b 1)
%if %{_gcc_ver} == 2
%define		__cxx		"%{__cc}"
%endif

%description
wmx is another window manager for X. It is based on wm2 and provides
a similarly unusual style of window decoration; but in place of wm2's
minimal functionality, it offers many of the features of more
conventional managers in the most simplistic implementations
imaginable.  wmx is, however, still barely configurable except by
editing the source and recompiling the code.

%description -l pl.UTF-8
wmx jest jeszcze jednym zarządcą okien dla X. Oparty na kodzie wm2
dostarcza podobnego niezwykłego stylu dekoracji okien; ale zamiast
minimalnej funkcjonalności wm2, wmx oferuje wiele właściwości bardziej
konwencjonalnych zarządców okien w najbardziej uproszczonej
implementacji. wmx nie da się konfigurować, chyba że poprzez edycję
źródeł i rekompilację.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xsessions}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.contrib UPDATES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xsessions/%{name}.desktop
