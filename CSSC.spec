Summary:	GNU Project's replacement for SCCS
Summary(pl.UTF-8):	Pochodzący z projektu GNU zamiennik SCCS
Name:		CSSC
Version:	1.0.1
Release:	1
License:	GPL
Group:		Development/Version Control
Source0:	http://dl.sourceforge.net/cssc/%{name}-%{version}.tar.gz
# Source0-md5:	5e1ebff620aea1295ac5de906d0dc279
URL:		http://cssc.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CSSC is the GNU Project's replacement for SCCS. SCCS is a proprietary
suite of tools which is provided with most commercial versions of
Unix. The purpose behind CSSC is to provide a work-alike for SCCS
which can be used on the various Free versions of Unix. SCCS was the
only major form of source code control on Unix platforms for many
years, until RCS came along. SCCS was an effective method for small
projects, but these days is less popular, particularly for projects
involving large numbers of files. A fair amount of old software is
still in SCCS form, and CSSC is designed to retrieve that software.

%description -l pl.UTF-8
CSSC to pochodzący z projektu GNU zamiennik SCCS. SCCS to własnościowy
zestaw narzędzi udostępnianych z większością komercyjnych wersji
Uniksa. Celem CSSC jest dostarczenie narzędzi działających podobnie do
SCCS, których można używać na wolnodostępnych wersjach Uniksa. SCCS
był jedyną ważniejszą formą kontroli kodu źródłowego na platformach
uniksowych przez wiele lat, do czasu wejścia RCS. SCCS był efektywny
dla małych projektów, ale teraz jest mniej popularny, szczególnie dla
projektów zawierających dużą liczbę plików. Znaczna część starego
oprogramowania jest nadal w postaci SCCS, a CSSC stworzono w celu
odzyskania tego oprogramowania.

%prep
%setup -q

%build
%configure \
	--enable-binary

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README docs/{BUGS,CREDITS,FIXED,TODO}
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/cssc
%attr(755,root,root) %{_libdir}/cssc/*
%{_mandir}/man?/*
%{_infodir}/cssc*
