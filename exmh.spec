Summary:	The exmh mail handling system.
Summary(es):	Interface gráfica para el programa de mail MH
Summary(de):	EXMH-Mail-Programm
Summary(fr):	Programme de courrier EXMH
Summary(pt_BR):	Interface gráfica para o programa de mail MH
Summary(ru):	ğÏŞÔÏ×ÁÑ ĞÒÏÇÒÁÍÍÁ EXMH
Summary(tr):	e-posta yazılımı
Name:		exmh
Version:	2.5
Release:	1
License:	Freeware
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Url:		http://www.beedub.com/exmh/
Source0:	http://prdownloads.sourceforge.net/exmh/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-conf.patch
Requires:	mh metamail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Exmh provides an X interface for MH/nmh mail, a feature-rich email
handling system. Exmh supports almost all (but not all) of MH's
features: viewing the messages in a folder, reading/deleting/refiling
messages, and sorting arriving mail into different folders before the
messages are read. Exmh highlights which folders have new mail, and
indicates which messages have not been read (so you don't lose the
sorted, unread mail).

If you like MH/nmh mail, you should install exmh, because it makes the
MH/nmh mail system much more user friendly. You may also want to use
exmh if you prefer a graphical user interface for your mail client.
Note that you will also have to install the nmh package.

%description -l de
exmh ist eine grafische Oberfläche für das MH-Mail-System. Zu den
Funktionen gehören MIME-Unterstützung, Faces, Glimpse-Indexing,
farbiges Markieren, PGP-Schnittstelle usw. Erfordert sox (oder play)
für Sound-Unterstützung.

%description -l es
exmh es una interface gráfica para el sistema de mail MH. Incluye
soporte para MINE, cuadros, indexación rápida, realce de colores,
interface PGP, y más.

%description -l fr
exmh est uen interface graphique au système de courrier MH. Il gère
MIME, les aspects, l'indexation glimpse, la mise en valeur par
couleurs, PGP, et autres. Il faut sox (ou play) pour gérér le son.

%description -l pl
Dziêki exmh otrzymujemy interfejs do bogatego w funkcje systemu
obs³ugi poczty MH/nmh. Exmh obs³uguje prawie wszystkie funkcje MH:
przegl±danie wiadomo¶ci w katalogu, czytanie/usuwanie/kolejkowanie
wiadomo¶ci oraz sortowanie poczty przychodz±cej do ró¿nych katalogów.
Exmh pod¶wietla foldery z nowymi wiadomo¶ciami i wskazuje te, które
nie zosta³y jeszcze przeczytane, dziêki czemu nie traci siê
posortowanych, nieprzeczytanych wiadomo¶ci.

%description -l pt_BR
exmh é uma interface gráfica para o sistema de mail MH. Ela inclui
suporte para MIME, quadros, indexação rápida, destacamento de cores,
interface PGP, e mais.

%description -l ru
exmh - ÜÔÏ ÇÒÁÆÉŞÅÓËÉÊ ÉÎÔÅÒÆÅÊÓ Ë ĞÏŞÔÏ×ÏÊ ÓÉÓÔÅÍÅ MH. ïÎ ×ËÌÀŞÁÅÔ
ĞÏÄÄÅÒÖËÕ MIME, faces, glimpse indexing, color highlighting, ÉÎÔÅÒÆÅÊÓ
PGP É ÍÎÏÇÏÅ ÄÒÕÇÏÅ. äÌÑ ĞÏÄÄÅÒÖËÉ Ú×ÕËÁ ÔÒÅÂÕÅÔÓÑ sox.

%description -l tr
exmh, yaygın olarak kullanılan mh paketi için X11 arayüzüdür. MIME
desteği, PGP desteği, faces, glimpse yardımıyla dizin oluşturma gibi
yetenekleri vardır. Ses desteği için sox (ya da play) gerekir.

%prep
%setup -q
for i in *.MASTER; do
	cp -f $i ${i%%.MASTER}
done
%patch -p1

%build
echo 'auto_mkindex ./lib *.tcl' | tclsh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Networking/Mail \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/exmh-%{version}}

for i in exmh exmh-bg exmh-async ftp.expect; do
	install $i $RPM_BUILD_ROOT%{_bindir}
done

for i in *.l; do
	install $i $RPM_BUILD_ROOT%{_mandir}/man1/${i%%.l}.1
done

cp -ar lib/* $RPM_BUILD_ROOT%{_libdir}/exmh-%{version}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Networking/Mail/

gzip -9nf COPYRIGHT exmh.CHANGES exmh.README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {COPYRIGHT,exmh.CHANGES,exmh.README}.gz
%{_applnkdir}/Networking/Mail/exmh.desktop
%attr(755,root,root) %{_bindir}/exmh
%attr(755,root,root) %{_bindir}/exmh-bg
%attr(755,root,root) %{_bindir}/exmh-async
%attr(755,root,root) %{_bindir}/ftp.expect
%{_libdir}/exmh-%{version}
%{_mandir}/man1/exmh.1*
