%define	module	proctitle

Summary:	Python module to manipulate the raw 'argv[]' contents of a python process
Summary(pl):	Modu³ jêzyka Python do manipulacji argv[] (w tym nazwy procesu)
Name:		python-%{module}
Version:	0.0.2
Release:	5
License:	GPL
Group:		Libraries/Python
Source0:	http://ftp.psychosis.com/python/%{module}-%{version}.tar.gz
# Source0-md5:	0d726d625b2be76458e0600fa79fed78
BuildRequires:	python-devel >= 2.2.1
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module to manipulate the raw 'argv[]' contents of a python
process. Allows to change process name during runtime.

%description -l pl
Modu³ jêzyka Python do manipulacji argv[] (w tym tak¿e widocznej w np.
w top nazwy procesu).

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir}
export PYTHONPATH

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/proctitle
%{py_sitedir}/proctitle/*.py[co]
%attr(755,root,root) %{py_sitedir}/proctitle/*.so
