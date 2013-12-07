%define	modname	Gtk2-Html2

Summary:	Perl module for the gtkhtml2 library
Name:		perl-%{modname}
Version:	0.04
Release:	22
License:	GPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	%{modname}-%{version}.tar.bz2
Patch0:		Gtk2-Html2-0.04-fix-example.patch
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-Gtk2
BuildRequires:	pkgconfig(libgtkhtml-2.0)
Requires:	perl-Gtk2 

%description
This package adds perl support for GtkHTML2.

%prep
%setup -qn %{modname}-%{version}
%patch0 -p0

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test || :

%install
%makeinstall_std

%files
%doc examples/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*
%{_mandir}/man3/*

