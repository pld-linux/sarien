Summary:	Interpreter for early Sierra adventures
Summary(pl):	Interpreter dla starych gier przygodowych firmy Sierra
Name:		sarien
Version:	0.7.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://prdownloads.sourceforge.net/sarien/%{name}-%{version}.tar.gz
URL:		http://sarien.sourceforge.net/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This package allows you to play AGI adventures as manufactured by
Sierra for, among others, MS-DOS systems in an X window. King's Quest
I through IV, Leisure Suit Larry, Space Quest and Police Quest are
some of the games that can be played. Run sarien in the directory
containing the adventure files. Please make sure that all file names
are lower-case.

%description -l pl
Ten pakiet pozwala graæ pod X Window w gry przygodowe AGI wydane przez
firmê Sierra pod systemy m.in. MS-DOS. King's Quest I do IV, Leisure
Suit Larry, Space Quest i Police Quest to tylko niektóre z tych gier.
Uruchom sarien w katalogu zawieraj±cym pliki z gry. Upewnij siê, ¿e
wszystkie nazwy plików s± ma³ymi literami.

%prep
%setup -q 

%build
rm -f config.cache
autoconf
%configure --with-x
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
install bin/sarien $RPM_BUILD_ROOT/%{_bindir}

gzip -9nf doc/{AUTHORS,BUGS,Changelog,README.*,TODO}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz
%attr(755,root,root) %{_bindir}/sarien
