Summary:	The exmh mail handling system.
Name:		exmh
Version:	2.0.2
Release:	8
Requires:	mh metamail
Copyright:	freeware
Group:		Applications/Mail
Url:		http://www.beedub.com/exmh/
Source0:	ftp://ftp.sunlabs.com/exmh-2.0.2.tar.Z
Source1:	exmh.wmconfig
Patch1:		exmh-2.0.2-conf.patch
Patch2:		exmh-2.0.2-smproxy.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArchitectures: noarch

%description
Exmh provides an X interface for MH/nmh mail, a feature-rich email
handling system.  Exmh supports almost all (but not all) of MH's
features: viewing the messages in a folder, reading/deleting/refiling
messages, and sorting arriving mail into different folders before the
messages are read. Exmh highlights which folders have new mail, and
indicates which messages have not been read (so you don't lose the sorted,
unread mail).

If you like MH/nmh mail, you should install exmh, because it makes the
MH/nmh mail system much more user friendly.  You may also want to use
exmh if you prefer a graphical user interface for your mail client.  Note
that you will also have to install the nmh package.

%description -l pl
Dzi�ki exmh otrzymujemy interfejs do bogatego w funkcje systemu obs�ugi poczty
MH/nmh. Exmh obs�uguje prawie wszystkie funkcje MH: przegl�danie wiadomo�ci
w katalogu, czytanie/usuwanie/kolejkowanie wiadomo�ci oraz sortowanie poczty
przychodz�cej do r�nych katalog�w. Exmh pod�wietla foldery z nowymi 
wiadomo�ciami i wskazuje te, kt�re nie zosta�y jeszcze przeczytane, dzi�ki
czemu nie traci si� posortowanych, nieprzeczytanych wiadomo�ci.

%prep
%setup -q
for i in *.MASTER; do
	cp $i ${i%%.MASTER}
done
%patch1 -p1
%patch2 -p1
find . -name "*.orig" -exec rm {} \;

%build
echo 'auto_mkindex ./lib *.tcl' | tclsh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/exmh-%{version}}

for i in exmh exmh-bg exmh-async ftp.expect; do
	install $i $RPM_BUILD_ROOT%{_bindir}
done

for i in *.l; do
	install $i $RPM_BUILD_ROOT%{_mandir}/man1/${i%%.l}.1
done

cp -ar lib/* $RPM_BUILD_ROOT/usr/lib/exmh-%{version}

install $RPM_SOURCE_DIR/exmh.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/exmh

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	COPYRIGHT exmh.CHANGES exmh.COLORS exmh.README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {COPYRIGHT,exmh.CHANGES,exmh.COLORS,exmh.README}.gz
%config /etc/X11/wmconfig/exmh
%attr(755,root,root) %{_bindir}/exmh
%attr(755,root,root) %{_bindir}/exmh-bg
%attr(755,root,root) %{_bindir}/exmh-async
%attr(755,root,root) %{_bindir}/ftp.expect
%{_libdir}/exmh-%{version}
%{_mandir}/man1/exmh.1.gz