Summary:	Interpreter for early Sierra adventures
Summary(pl.UTF-8):	Interpreter dla starych gier przygodowych firmy Sierra
Name:		sarien
Version:	0.7.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/sarien/%{name}-%{version}.tar.gz
# Source0-md5:	76db53d1bdcecd37913c95af9d47820c
URL:		http://sarien.sourceforge.net/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows you to play AGI adventures as manufactured by
Sierra for, among others, MS-DOS systems in an X window. King's Quest
I through IV, Leisure Suit Larry, Space Quest and Police Quest are
some of the games that can be played. Run sarien in the directory
containing the adventure files. Please make sure that all file names
are lower-case.

%description -l pl.UTF-8
Ten pakiet pozwala grać pod X Window w gry przygodowe AGI wydane przez
firmę Sierra pod systemy m.in. MS-DOS. King's Quest I do IV, Leisure
Suit Larry, Space Quest i Police Quest to tylko niektóre z tych gier.
Uruchom sarien w katalogu zawierającym pliki z gry. Upewnij się, że
wszystkie nazwy plików są małymi literami.

%prep
%setup -q

%build
rm -f config.cache
%{__autoconf}
%configure --with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bin/sarien $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,BUGS,Changelog,README.*,TODO}
%attr(755,root,root) %{_bindir}/sarien
