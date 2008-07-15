%define module File-Find-Iterator
%define name perl-%{module}
%define version 0.4
%define release %mkrel 1

Summary: 	Iterator interface for search files
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/T/TE/TEXMEC/%{module}-%{version}.tar.gz
Url: 		http://search.cpan.org/dist/%{module}
BuildRequires: perl-devel
BuildRequires: perl(Class::Iterator)
BuildRoot: 	%{_tmppath}/%{name}-buildroot/
BuildArch: noarch

%description
Find::File::Iterator is an iterator object for searching through
directory trees. You can easily run filter on each file name. You 
can easily save the search state when you want to stop the search
and continue the same search later.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/*

