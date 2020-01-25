#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Pod
%define		pnam	POM-View-Restructured
Summary:	Pod::POM::View::Restructured - View for Pod::POM that outputs reStructuredText
Summary(pl.UTF-8):	Pod::POM::View::Restructured - widok dla Pod::POM z wyjściem w formacie reStructuredText
Name:		perl-Pod-POM-View-Restructured
Version:	1.000002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Pod/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	638084b3c8df3361d523a6f50bf58db9
URL:		https://metacpan.org/release/Pod-POM-View-Restructured/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Pod-POM
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module outputs reStructuredText that is expected to be used with
Sphinx. Verbatim sections (indented paragraphs) in the POD will be
output with syntax highlighting for Perl code by default.

%description -l pl.UTF-8
Ten moduł produkuje wyjście w formacie reStructuredText, przeznaczonym
do użytku ze Sphinksem. Sekcje maszynowe (akapity z wcięciem) w POD są
wypisywane z domyślbym podświetlaniem składni dla kodu w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README
%attr(755,root,root) %{_bindir}/pod2rst
%{perl_vendorlib}/Pod/POM/View/Restructured.pm
%{_mandir}/man1/pod2rst.1p*
%{_mandir}/man3/Pod::POM::View::Restructured.3pm*
