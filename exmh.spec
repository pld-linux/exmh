Summary: The exmh mail handling system.
Name: exmh
Version: 2.0.2
Release: 7
Requires: mh metamail
Copyright: freeware
Group: Applications/Internet
BuildArchitectures: noarch
Source0: ftp://ftp.sunlabs.com/exmh-2.0.2.tar.Z
Url: http://www.beedub.com/exmh/
Source1: exmh.wmconfig
Patch1: exmh-2.0.2-conf.patch
Patch2: exmh-2.0.2-smproxy.patch
BuildRoot: /var/tmp/exmh-root

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

%prep
%setup -q -n exmh-%{PACKAGE_VERSION}
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
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}
mkdir -p $RPM_BUILD_ROOT/usr/lib/exmh-%{PACKAGE_VERSION}

for i in exmh exmh-bg exmh-async ftp.expect; do
	install -m755 $i $RPM_BUILD_ROOT/usr/bin
done
for i in *.l; do
	install -m644 $i $RPM_BUILD_ROOT/usr/man/man1/${i%%.l}.1
done

cp -ar lib/* $RPM_BUILD_ROOT/usr/lib/exmh-%{PACKAGE_VERSION}

install -m644 $RPM_SOURCE_DIR/exmh.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/exmh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYRIGHT exmh.CHANGES exmh.COLORS exmh.README
%config /etc/X11/wmconfig/exmh
/usr/bin/exmh
/usr/bin/exmh-bg
/usr/bin/exmh-async
/usr/bin/ftp.expect
/usr/lib/exmh-%{PACKAGE_VERSION}
/usr/man/man1/exmh.1
