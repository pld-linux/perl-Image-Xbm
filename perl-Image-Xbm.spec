%include	/usr/lib/rpm/macros.perl
%define	pdir	Image
%define	pnam	Xbm
Summary:	Image::Xbm perl module
Summary(pl):	Modu³ perla Image::Xbm
Name:		perl-Image-Xbm
Version:	1.08
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Image::Xbm - Load, create, manipulate and save xbm image files.

%description -l pl
Modu³ Image::Xbm - pozwalaj±cy wczytywaæ, tworzyæ, modyfikowaæ oraz
zapisywaæ pliki obrazków xbm.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Image/*
%{_mandir}/man[3]/*
