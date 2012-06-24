Summary:	GNU Project's replacement for SCCS
Summary(pl):	Pochodz�cy z projektu GNU zamiennik SCCS
Name:		CSSC
Version:	0.16alpha.pl0
Release:	1
License:	GPL
Group:		Development/Version Control
Source0:	http://dl.sourceforge.net/cssc/%{name}-%{version}.tar.gz
# Source0-md5:	b46a0ab08cd2ab6d3c6c24a7c882cea4
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

%description -l pl
CSSC to pochodz�cy z projektu GNU zamiennik SCCS. SCCS to w�asno�ciowy
zestaw narz�dzi udost�pnianych z wi�kszo�ci� komercyjnych wersji
Uniksa. Celem CSSC jest dostarczenie narz�dzi dzia�aj�cych podobnie do
SCCS, kt�rych mo�na u�ywa� na wolnodost�pnych wersjach Uniksa. SCCS
by� jedyn� wa�niejsz� form� kontroli kodu �r�d�owego na platformach
uniksowych przez wiele lat, do czasu wej�cia RCS. SCCS by� efektywny
dla ma�ych projekt�w, ale teraz jest mniej popularny, szczeg�lnie dla
projekt�w zawieraj�cych du�� liczb� plik�w. Znaczna cz�� starego
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

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README docs/{BUGS,CREDITS,FIXED,TODO}
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/cssc
%attr(755,root,root) %{_libdir}/cssc/*
%{_mandir}/man?/*
%{_infodir}/cssc*
