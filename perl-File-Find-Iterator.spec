%define module File-Find-Iterator
%define upstream_version 0.4

Summary: 	Iterator interface for search files
Name: 		perl-%{module}
Version: 	%perl_convert_version 0.4
Release: 	4
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/T/TE/TEXMEC/File-Find-Iterator-0.4.tar.gz
Url: 		http://search.cpan.org/dist/%{module}
BuildRequires: perl-devel
BuildRequires: perl(Class::Iterator)
BuildArch: noarch

%description
Find::File::Iterator is an iterator object for searching through
directory trees. You can easily run filter on each file name. You 
can easily save the search state when you want to stop the search
and continue the same search later.

%prep
%setup -q -n %{module}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/*



%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.4-3mdv2011.0
+ Revision: 654186
- rebuild for updated spec-helper

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.4-2mdv2011.0
+ Revision: 430454
- rebuild

* Tue Jul 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.4-1mdv2009.0
+ Revision: 235777
- update to new version 0.4

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.3-5mdv2008.1
+ Revision: 152075
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-3mdv2008.0
+ Revision: 86399
- rebuild


* Fri Aug 11 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/11/06 12:54:15 (55647)
- rebuild

* Fri Aug 11 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/11/06 12:49:52 (55646)
Import perl-File-Find-Iterator

* Thu Jun 16 2005 Olivier Thauvin <nanardon@mandriva.org> 0.3-1mdk
- first mdk release


