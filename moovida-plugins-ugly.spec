%define		module_name	elisa
Summary:	"Ugly" plugins for Moovida
Summary(pl.UTF-8):	"Brzydkie" wtyczki dla Moovidy
Name:		moovida-plugins-ugly
Version:	1.0.7
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://www.moovida.com/media/public/%{name}-%{version}.tar.gz
# Source0-md5:	268255619580bd340616c4074750f846
URL:		http://www.moovida.com/
BuildRequires:	moovida = %{version}
Requires:	twill
Provides:	moovida-plugins = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Ugly" plugins for Moovida

%description -l pl.UTF-8
"Brzydkie" wtyczki dla Moovidy

%prep
%setup -q -n elisa-plugins-ugly-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

#py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/*.pth
%{py_sitescriptdir}/%{module_name}/plugins/*
