%define upstream_name	 Algorithm-C3
%define upstream_version 0.08

Summary:	A module for merging hierarchies using the C3 algorithm
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.bz2
BuildArch:	noarch

BuildRequires:	perl(Carp) >= 0.01
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::More) >= 0.47

%description
This module implements the C3 algorithm. Most of the uses for C3
revolve around class building and metamodels, but it could also be
used for things like dependency resolution as well since it tends to
do such a nice job of preserving local precendence orderings.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
./Build test

%install
./Build install

%files
%doc Changes README
%{perl_vendorlib}/Algorithm
%{_mandir}/man*/*

