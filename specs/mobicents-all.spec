%define project_build 1005131726
%define jboss_version jboss-jdk6-5.1.0.GA

Summary: 	    Mobicents Sip Servlets and Mobicents Media Server
Name: 		    mobicents-all
Version: 	    1.3
Release: 	    1
License: 	    LGPL
BuildArch: 	    noarch
Group: 		    Web/Telco
Source0:	    http://downloads.sourceforge.net/project/mobicents/Mobicents%20Sip%20Servlets/Mobicents%20Sip%20Servlets%20%{version}/mss-%{version}-%{jboss_version}-%{project_build}.zip
Source1:        mobicents/mobicents-sip-servlets.init
Source2:        mobicents/mobicents-media-server.init
URL: 		    http://www.mobicents.org
Vendor: 	    Red Hat
Requires:       java-1.6.0-openjdk
Requires:       initscripts
Requires(post): /sbin/chkconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Mobicents Sip Servlets delivers a consistent, open platform on which to develop and deploy portable and distributable SIP and Converged JEE services.  It is the first open source certified implementation of the SIP Servlet v1.1 (JSR 289 Spec) on top of Tomcat & JBoss containers and strive to feature best performances, security, foster innovation and develop interoperability standards between Sip Servlets and JSLEE so that applications may exploit the strengths of both. The JAIN-SIP Reference implementation  is leveraged as the SIP stack and Mobicents JAIN SLEE  is used as the SLEE implementation.

%define runuser %{name}
%define __jar_repack %{nil}

%prep
rm -rf mss-%{version}-%{jboss_version}
unzip -q %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT/opt/%{name}-%{version}
cp -R mss-%{version}-%{jboss_version}/* $RPM_BUILD_ROOT/opt/%{name}-%{version}

install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/mobicents-sip-servlets
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_initrddir}/mobicents-media-server

install -d -m 755 $RPM_BUILD_ROOT/etc/sysconfig
 
echo "MOBICENTS_ALL=%{version}"              > $RPM_BUILD_ROOT/etc/sysconfig/%{name}
echo "MOBICENTS_ALL_HOME=/opt/%{name}-%{version}"   >> $RPM_BUILD_ROOT/etc/sysconfig/%{name}

%post
/sbin/chkconfig --add mobicents-sip-servlets
/sbin/chkconfig mobicents-sip-servlets on
/sbin/chkconfig --add mobicents-media-server
/sbin/chkconfig mobicents-media-server on

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/

%changelog
* Fri Jun 11 2010 Marek Goldmann <marek.goldmann@gmail.com> 1.3-1
- Initial release
