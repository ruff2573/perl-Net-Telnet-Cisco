#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Net
%define		pnam	Telnet-Cisco
Summary:	Net::Telnet::Cisco Perl module
Summary(cs.UTF-8):	Modul Net::Telnet::Cisco pro Perl
Summary(da.UTF-8):	Perlmodul Net::Telnet::Cisco
Summary(de.UTF-8):	Net::Telnet::Cisco Perl Modul
Summary(es.UTF-8):	Módulo de Perl Net::Telnet::Cisco
Summary(fr.UTF-8):	Module Perl Net::Telnet::Cisco
Summary(it.UTF-8):	Modulo di Perl Net::Telnet::Cisco
Summary(ja.UTF-8):	Net::Telnet::Cisco Perl モジュール
Summary(ko.UTF-8):	Net::Telnet::Cisco 펄 모줄
Summary(nb.UTF-8):	Perlmodul Net::Telnet::Cisco
Summary(pl.UTF-8):	Moduł Perla Net::Telnet::Cisco
Summary(pt.UTF-8):	Módulo de Perl Net::Telnet::Cisco
Summary(pt_BR.UTF-8):	Módulo Perl Net::Telnet::Cisco
Summary(ru.UTF-8):	Модуль для Perl Net::Telnet::Cisco
Summary(sv.UTF-8):	Net::Telnet::Cisco Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Net::Telnet::Cisco
Summary(zh_CN.UTF-8):	Net::Telnet::Cisco Perl 模块
Name:		perl-Net-Telnet-Cisco
Version:	1.10
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a25845350be369cb8354e0ddc55708f9
URL:		http://search.cpan.org/dist/Net-Telnet-Cisco/
BuildRequires:	perl-Net-Telnet
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Telnet::Cisco - interact with TELNET port on Cisco routers.

%description -l pl.UTF-8
Net::Telnet::Cisco - wsparcie dla protokołu TELNET na urządzeniach
Cisco.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test </dev/null}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Net/Telnet
%dir %{perl_vendorlib}/auto/Net/Telnet
# empty autosplit.ix, but needed.
%dir %{perl_vendorlib}/auto/Net/Telnet/Cisco
%{perl_vendorlib}/auto/Net/Telnet/Cisco/autosplit.ix
%{_mandir}/man3/*
