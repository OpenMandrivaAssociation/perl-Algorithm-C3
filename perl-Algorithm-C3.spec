%define module	Algorithm-C3
%define name	perl-%{module}
%define	modprefix Algorithm

%define version 0.07

%define	rel	1
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	A module for merging hierarchies using the C3 algorithm
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Carp) >= 0.01
BuildRequires:  perl(Module::Build)
BuildRequires:	perl(Test::More) >= 0.47
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module implements the C3 algorithm. Most of the uses for C3
revolve around class building and metamodels, but it could also be
used for things like dependency resolution as well since it tends to
do such a nice job of preserving local precendence orderings.

%prep
%setup -q -n %{module}-%{version}

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
%{perl_vendorlib}/%{modprefix}
%{_mandir}/man*/*

