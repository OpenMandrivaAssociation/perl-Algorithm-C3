%define upstream_name	 Algorithm-C3
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

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
