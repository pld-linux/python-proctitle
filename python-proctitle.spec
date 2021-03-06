%define	module	proctitle

Summary:	Python module to manipulate the raw 'argv[]' contents of a python process
Summary(pl.UTF-8):	Moduł języka Python do manipulacji argv[] (w tym nazwy procesu)
Name:		python-%{module}
Version:	0.0.2
Release:	8
License:	GPL
Group:		Libraries/Python
Source0:	http://ftp.psychosis.com/python/%{module}-%{version}.tar.gz
# Source0-md5:	0d726d625b2be76458e0600fa79fed78
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module to manipulate the raw 'argv[]' contents of a python
process. Allows to change process name during runtime.

%description -l pl.UTF-8
Moduł języka Python do manipulacji argv[] (w tym także widocznej w np.
w top nazwy procesu).

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir}
export PYTHONPATH

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/proctitle
%{py_sitedir}/proctitle/*.py[co]
%attr(755,root,root) %{py_sitedir}/proctitle/*.so
