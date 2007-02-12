Summary:	The exmh mail handling system
Summary(de.UTF-8):   EXMH-Mail-Programm
Summary(es.UTF-8):   Interface gráfica para el programa de mail MH
Summary(fr.UTF-8):   Programme de courrier EXMH
Summary(pl.UTF-8):   System obsługi poczty exmh
Summary(pt_BR.UTF-8):   Interface gráfica para o programa de mail MH
Summary(ru.UTF-8):   Почтовая программа EXMH
Summary(sv.UTF-8):   E-postläsare som kan hantera e-postmappar av mh-typ
Summary(tr.UTF-8):   e-posta yazılımı
Name:		exmh
Version:	2.7.2
Release:	1
License:	Freeware
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/exmh/%{name}-%{version}.tar.gz
# Source0-md5:	fdb7c6ff26d0429ea950590a36f1369f
Source1:	%{name}.desktop
Patch0:		%{name}-conf.patch
Patch1:		%{name}-smproxy.patch
URL:		http://www.beedub.com/exmh/
BuildRequires:	tcl
Requires:	metamail
Requires:	mh
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l de.UTF-8
exmh ist eine grafische Oberfläche für das MH-Mail-System. Zu den
Funktionen gehören MIME-Unterstützung, Faces, Glimpse-Indexing,
farbiges Markieren, PGP-Schnittstelle usw. Erfordert sox (oder play)
für Sound-Unterstützung.

%description -l es.UTF-8
exmh es una interface gráfica para el sistema de mail MH. Incluye
soporte para MINE, cuadros, indexación rápida, realce de colores,
interface PGP, y más.

%description -l fr.UTF-8
exmh est uen interface graphique au système de courrier MH. Il gère
MIME, les aspects, l'indexation glimpse, la mise en valeur par
couleurs, PGP, et autres. Il faut sox (ou play) pour gérér le son.

%description -l pl.UTF-8
Dzięki exmh otrzymujemy interfejs do bogatego w funkcje systemu
obsługi poczty MH/nmh. Exmh obsługuje prawie wszystkie funkcje MH:
przeglądanie wiadomości w katalogu, czytanie/usuwanie/kolejkowanie
wiadomości oraz sortowanie poczty przychodzącej do różnych katalogów.
Exmh podświetla foldery z nowymi wiadomościami i wskazuje te, które
nie zostały jeszcze przeczytane, dzięki czemu nie traci się
posortowanych, nieprzeczytanych wiadomości.

%description -l pt_BR.UTF-8
exmh é uma interface gráfica para o sistema de mail MH. Ela inclui
suporte para MIME, quadros, indexação rápida, destacamento de cores,
interface PGP, e mais.

%description -l ru.UTF-8
exmh - это графический интерфейс к почтовой системе MH. Он включает
поддержку MIME, faces, glimpse indexing, color highlighting, интерфейс
PGP и многое другое. Для поддержки звука требуется sox.

%description -l tr.UTF-8
exmh, yaygın olarak kullanılan mh paketi için X11 arayüzüdür. MIME
desteği, PGP desteği, faces, glimpse yardımıyla dizin oluşturma gibi
yetenekleri vardır. Ses desteği için sox (ya da play) gerekir.

%prep
%setup -q
for i in *.MASTER; do
	cp -f $i ${i%%.MASTER}
done
%patch0 -p1
%patch1 -p1

%build
echo 'auto_mkindex ./lib *.tcl' | tclsh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/exmh-%{version}}

for i in exmh exmh-bg exmh-async ftp.expect; do
	install $i $RPM_BUILD_ROOT%{_bindir}
done

for i in *.l; do
	install $i $RPM_BUILD_ROOT%{_mandir}/man1/${i%%.l}.1
done

cp -a lib/* $RPM_BUILD_ROOT%{_libdir}/exmh-%{version}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT exmh.CHANGES exmh.README
%{_desktopdir}/exmh.desktop
%attr(755,root,root) %{_bindir}/exmh
%attr(755,root,root) %{_bindir}/exmh-bg
%attr(755,root,root) %{_bindir}/exmh-async
%attr(755,root,root) %{_bindir}/ftp.expect
%{_libdir}/exmh-%{version}
%{_mandir}/man1/exmh.1*
