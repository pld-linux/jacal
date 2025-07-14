Summary:	Jacal - symbolic mathematics system written in Scheme
Summary(pl.UTF-8):	Jacal - system matematyki symbolicznej napisany w Scheme
Name:		jacal
Version:	1c7
Release:	1
License:	GPL v3+
Group:		Development/Languages/Scheme
Source0:	http://groups.csail.mit.edu/mac/ftpdir/scm/%{name}-%{version}.zip
# Source0-md5:	72d6bb0f029e436407b67a662729e38b
Patch0:		%{name}-info.patch
URL:		http://people.csail.mit.edu/jaffer/JACAL
BuildRequires:	slib
BuildRequires:	texinfo
Requires:	scm
Requires:	slib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jacal is a symbolic mathematics system written in the programming
language Scheme.

%description -l pl.UTF-8
Jacal to system matematyki symbolicznej napisany w języku
programowania Scheme.

%prep
%setup -q -n jacal
%patch -P0 -p1

%build
# not autoconf-generated
sh ./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/jacal/Makefile

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ANNOUNCE ChangeLog README DOC/{algdenom,grammar,history,lambda,ratint.pdf}
%attr(755,root,root) %{_bindir}/jacal
%dir %{_libdir}/jacal
%{_libdir}/jacal/*.scm
%{_libdir}/jacal/jacalcat
%{_libdir}/jacal/COPYING
%{_libdir}/jacal/HELP
%{_mandir}/man1/jacal.1*
%{_infodir}/jacal.info*
