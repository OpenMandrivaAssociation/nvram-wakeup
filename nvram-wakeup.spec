Name:		nvram-wakeup
URL:		http://sourceforge.net/projects/nvram-wakeup
Summary:	Reads and writes the WakeUp time in the BIOS
Version:	1.1
Release:	1
License:	GNU General Public License (GPL)
Group:		System/Base
Source:		http://downloads.sourceforge.net/project/nvram-wakeup/nvram-wakup-%{version}.tar.gz
Source1:	COPYING

%description
This is a (small) program  that can read and write  the WakeUp time in
the  BIOS  (via /dev/nvram on kernels >= 2.4.6 or via direct I/O).  On
this  WakeUp  time  the computer will be powered on automatically from
the soft-off state.

---- WARNING: --------------------------------------------------------
This program  writes into the  NVRAM  (used by	BIOS to store the CMOS
settings). This is  DANGEROUS.	Do it at  your own  risk.  Neither the
author	of  this program  (nvram-wakeup)  nor anyone else  can be made
responsible to any damage made by this program in any way. (The worst
case  happened to me is that on reboot the BIOS noticed the illegal 
contents of  the nvram and  set everything to default values. But this
doesn't mean that you can't destroy even your whole computer.) YOU HAVE
BEEN WARNED.

%prep
%setup -q -n nvram-wakup-%{version}

%build
%make

%install

#% makeinstall_std

mkdir -p %buildroot/%{_sbindir}
mkdir -p %buildroot/%{_mandir}/man8
gzip *.8
cp %{SOURCE1} .
install -m 0755 biosinfo cat_nvram guess-helper guess \
	set_timer time nvram-wakeup rtc %buildroot/%{_sbindir}
install -m 0644 *.8.* %buildroot/%{_mandir}/man8

%files
%doc HISTORY README.*  COPYING
%{_sbindir}/*
%{_mandir}/man8/*.8.*


%changelog
* Fri Dec 02 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.1-1
+ Revision: 737233
- imported package nvram-wakeup

