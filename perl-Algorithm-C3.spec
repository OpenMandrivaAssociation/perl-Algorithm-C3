%define upstream_name	 Algorithm-C3
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	A module for merging hierarchies using the C3 algorithm
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Carp) >= 0.01
BuildRequires:  perl(Module::Build)
BuildRequires:	perl(Test::More) >= 0.47
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements the C3 algorithm. Most of the uses for C3
revolve around class building and metamodels, but it could also be
used for things like dependency resolution as well since it tends to
do such a nice job of preserving local precendence orderings.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Algorithm
%{_mandir}/man*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-4mdv2012.0
+ Revision: 765047
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-2
+ Revision: 667022
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 406254
- rebuild using %%perl_convert_version

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-3mdv2010.0
+ Revision: 383470
- update to new version 0.08

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.07-3mdv2009.0
+ Revision: 241143
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2008.0
+ Revision: 46309
- update to new version 0.07

* Mon Apr 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.06-1mdv2008.0
+ Revision: 17417
- New version 0.06


* Sat Aug 26 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-26 14:35:38 (58185)
- Version 0.05

* Thu Aug 10 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-10 03:21:46 (55292)
Version 0.04

* Wed Aug 09 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-09 15:01:22 (54773)
Version 0.03

* Fri Aug 04 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-04 22:13:46 (53023)
Version 0.02

* Fri Aug 04 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-04 21:35:02 (52989)
import perl-Algorithm-C3-0.01-1mdk

* Mon May 22 2006 Scott Karns <scottk@mandriva.org> 0.01-1mdk
- First mandriva package

