%define project_name GateIn
%define project_version 3.0.0-Beta05

Summary: 	The Best of eXo and JBoss Portal platform!
Name: 		gatein
Version: 	3.0.0.Beta05
Release: 	1
License: 	LGPL
BuildArch: 	noarch
Group: 		Web/Portlet
Source:		http://downloads.sourceforge.net/project/jboss/%{project_name}/Portal/%{project_version}/%{project_name}-%{project_version}-jbossas.tar.gz
URL: 		http://www.jboss.org/gatein
Vendor: 	RedHat, eXo platform.
Packager: 	Luca Stancapiano <jedim@vige.it>
Requires:       java-1.6.0-openjdk
Requires:       shadow-utils
BuildRoot:      %{_tmppath}/%{name}-3.0.0-Beta05-%{release}-root-%(%{__id_u} -n)

%description
GateIn is a set of projects revolving aroung the main project called "GateIn Portal".

GateIn portal is a merge of two mature projects that have been around for a while,
JBoss Portal and eXo Portal. It takes the best of both into a single new project.
The aim is to provide both an intuitive portal to use as-is and a portal framework to build upon depending on your needs.

%define runuser %{name}
%define __jar_repack %{nil}

%prep
%setup -n %{project_name}-%{project_version}

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT/opt/%{name}-%{version}
cp -R . $RPM_BUILD_ROOT/opt/%{name}-%{version}

install -d -m 755 $RPM_BUILD_ROOT/etc/sysconfig
 
echo "GATEIN_VERSION=%{version}"              > $RPM_BUILD_ROOT/etc/sysconfig/%{name}
echo "GATEIN_HOME=/opt/%{name}-%{version}"   >> $RPM_BUILD_ROOT/etc/sysconfig/%{name}

%pre
/usr/sbin/groupadd -r %{name} 2>/dev/null || :
/usr/sbin/useradd -c "%{name}" -r -s /bin/bash -d /opt/%{name}-%{version} -g %{name} %{name} 2>/dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,%{name},%{name})
/

%changelog
* Mon Feb 15 2010 Luca Stancapiano 3.0.0.Beta-05
- Initial release
