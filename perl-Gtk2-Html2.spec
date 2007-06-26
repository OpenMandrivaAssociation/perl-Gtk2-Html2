%define module Gtk2-Html2
%define fmodule Html2

Summary: Perl module for the gtkhtml2 library
Name:    perl-%module
Version: 0.04
Release: %mkrel 8
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  %module-%version.tar.bz2
Patch0:  Gtk2-Html2-0.04-fix-example.patch
URL: http://gtk2-perl.sf.net/
BuildRequires: gtkhtml2-devel => 2.4, perl-devel perl-ExtUtils-Depends perl-Gtk2 >= 1.083-2mdk
BuildRequires: perl-ExtUtils-PkgConfig
Requires: perl-Gtk2 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package adds perl support for GtkHTML2.


%prep
%setup -q -n %module-%version
%patch0 -p0
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc examples/*
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*


