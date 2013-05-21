%define	modname	Gtk2-Html2

Summary:	Perl module for the gtkhtml2 library
Name:		perl-%{modname}
Version:	0.04
Release:	19
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
Source0:	%{modname}-%{version}.tar.bz2
Patch0:		Gtk2-Html2-0.04-fix-example.patch
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtkhtml2-devel => 2.4 perl-devel perl-ExtUtils-Depends perl-Gtk2 >= 1.083-2mdk
BuildRequires:	perl-ExtUtils-PkgConfig
Requires:	perl-Gtk2 

%description
This package adds perl support for GtkHTML2.

%prep
%setup -q -n %{modname}-%{version}
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
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*

%changelog
* Sat Dec 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.04-18
- rebuild for new perl-5.16.2
- cleanups

* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.04-17
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.04-14
+ Revision: 702777
- rebuilt against libpng-1.5.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.04-13
+ Revision: 667185
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.04-12mdv2011.0
+ Revision: 564483
- rebuild for perl 5.12.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.04-11mdv2011.0
+ Revision: 426470
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.04-10mdv2009.0
+ Revision: 223779
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.04-9mdv2008.1
+ Revision: 152106
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 0.04-8mdv2008.0
+ Revision: 44605
- fix wrong name (really was not compressed
- rebuild


* Thu Mar 29 2007 Frederic Crozat <fcrozat@mandriva.com> 0.04-7mdv2007.1
+ Revision: 149326
- Rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Gtk2-Html2

* Thu Aug 25 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.04-6mdk
- rebuild with new gtk+

* Thu Mar 10 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.04-5mdk
- add BuildRequires: perl-ExtUtils-PkgConfig

* Thu Feb 24 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-4mdk
- patch 0: enable file:/// URI in example

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-3mdk
- rebuild for new perl

* Sat Aug 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-2mdk
- rebuild for perl-5.8.5

* Tue May 11 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-1mdk
- new release

* Sat Apr 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.02-1mdk
- initial release

