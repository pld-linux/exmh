Summary:	The exmh mail handling system.
Summary(es):	Interface gr�fica para el programa de mail MH
Summary(de):	EXMH-Mail-Programm
Summary(fr):	Programme de courrier EXMH
Summary(pt_BR):	Interface gr�fica para o programa de mail MH
Summary(ru):	�������� ��������� EXMH
Summary(tr):	e-posta yaz�l�m�
Name:		exmh
Version:	2.5
Release:	1
License:	Freeware
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplica��es/Correio Eletr�nico
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
exmh ist eine grafische Oberfl�che f�r das MH-Mail-System. Zu den
Funktionen geh�ren MIME-Unterst�tzung, Faces, Glimpse-Indexing,
farbiges Markieren, PGP-Schnittstelle usw. Erfordert sox (oder play)
f�r Sound-Unterst�tzung.

%description -l es
exmh es una interface gr�fica para el sistema de mail MH. Incluye
soporte para MINE, cuadros, indexaci�n r�pida, realce de colores,
interface PGP, y m�s.

%description -l fr
exmh est uen interface graphique au syst�me de courrier MH. Il g�re
MIME, les aspects, l'indexation glimpse, la mise en valeur par
couleurs, PGP, et autres. Il faut sox (ou play) pour g�r�r le son.

%description -l pl
Dzi�ki exmh otrzymujemy interfejs do bogatego w funkcje systemu
obs�ugi poczty MH/nmh. Exmh obs�uguje prawie wszystkie funkcje MH:
przegl�danie wiadomo�ci w katalogu, czytanie/usuwanie/kolejkowanie
wiadomo�ci oraz sortowanie poczty przychodz�cej do r�nych katalog�w.
Exmh pod�wietla foldery z nowymi wiadomo�ciami i wskazuje te, kt�re
nie zosta�y jeszcze przeczytane, dzi�ki czemu nie traci si�
posortowanych, nieprzeczytanych wiadomo�ci.

%description -l pt_BR
exmh � uma interface gr�fica para o sistema de mail MH. Ela inclui
suporte para MIME, quadros, indexa��o r�pida, destacamento de cores,
interface PGP, e mais.

%description -l ru
exmh - ��� ����������� ��������� � �������� ������� MH. �� ��������
��������� MIME, faces, glimpse indexing, color highlighting, ���������
PGP � ������ ������. ��� ��������� ����� ��������� sox.

%description -l tr
exmh, yayg�n olarak kullan�lan mh paketi i�in X11 aray�z�d�r. MIME
deste�i, PGP deste�i, faces, glimpse yard�m�yla dizin olu�turma gibi
yetenekleri vard�r. Ses deste�i i�in sox (ya da play) gerekir.

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
