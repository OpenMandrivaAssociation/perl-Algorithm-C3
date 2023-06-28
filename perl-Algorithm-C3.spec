%define upstream_name	 Algorithm-C3
%define upstream_version 0.11

Summary:	A module for merging hierarchies using the C3 algorithm

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Algorithm::C3
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch

BuildRequires:	perl(Carp) >= 0.01
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl-devel

%description
This module implements the C3 algorithm. Most of the uses for C3
revolve around class building and metamodels, but it could also be
used for things like dependency resolution as well since it tends to
do such a nice job of preserving local precendence orderings.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor destdir=%{buildroot}
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Algorithm
%{_mandir}/man*/*
