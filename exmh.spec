Summary:	The exmh mail handling system.
Name:		exmh
Version:	2.2
Release:	1
Copyright:	freeware
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Url:		http://www.beedub.com/exmh/
Source0:	ftp://ftp.scriptics.com/pub/tcl/exmh/%{name}-%{version}.tar.gz
Source1:	exmh.desktop
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

%description -l pl
Dziêki exmh otrzymujemy interfejs do bogatego w funkcje systemu
obs³ugi poczty MH/nmh. Exmh obs³uguje prawie wszystkie funkcje MH:
przegl±danie wiadomo¶ci w katalogu, czytanie/usuwanie/kolejkowanie
wiadomo¶ci oraz sortowanie poczty przychodz±cej do ró¿nych katalogów.
Exmh pod¶wietla foldery z nowymi wiadomo¶ciami i wskazuje te, które
nie zosta³y jeszcze przeczytane, dziêki czemu nie traci siê
posortowanych, nieprzeczytanych wiadomo¶ci.

%prep
%setup -q
for i in *.MASTER; do
	cp $i ${i%%.MASTER}
done

%build
echo 'auto_mkindex ./lib *.tcl' | tclsh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT %{_applnkdir}/Networking/Mail/
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/exmh-%{version}}

for i in exmh exmh-bg exmh-async ftp.expect; do
	install $i $RPM_BUILD_ROOT%{_bindir}
done

for i in *.l; do
	install $i $RPM_BUILD_ROOT%{_mandir}/man1/${i%%.l}.1
done

cp -ar lib/* $RPM_BUILD_ROOT%{_libdir}/exmh-%{version}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Networking/Mail/

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	COPYRIGHT exmh.CHANGES exmh.COLORS exmh.README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {COPYRIGHT,exmh.CHANGES,exmh.COLORS,exmh.README}.gz
%{_applnkdir}/Networking/Mail/exmh.desktop
%attr(755,root,root) %{_bindir}/exmh
%attr(755,root,root) %{_bindir}/exmh-bg
%attr(755,root,root) %{_bindir}/exmh-async
%attr(755,root,root) %{_bindir}/ftp.expect
%{_libdir}/exmh-%{version}
%{_mandir}/man1/exmh.1.gz
