#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Image
%define		pnam	Xbm
Summary:	Image::Xbm - load, create, manipulate and save xbm image files
Summary(pl.UTF-8):	Image::Xbm - wczytywanie, tworzenie, modyfikacja i zapis obrazków w formacie xbm
Name:		perl-Image-Xbm
Version:	1.08
Release:	6
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3a6cde06d6de70ee98fb1849ba18b385
URL:		http://search.cpan.org/dist/Image-Xbm/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Image-Base >= 1.06
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class module provides basic load, manipulate and save
functionality for the xbm file format. It inherits from Image::Base
which provides additional manipulation functionality, e.g.
new_from_image().

%description -l pl.UTF-8
Image::Xbm dostarcza prostej funkcjonalności do wczytywania,
manipulacji i zapisywania obrazów w formacie xbm. Dziedziczy po
Image::Base, dostarczającym dodatkowych funkcji manipulacyjnych; np.
new_from_image().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Image/*
%{_mandir}/man3/*
