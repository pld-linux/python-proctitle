%include	/usr/lib/rpm/macros.python

Summary:	Python module to manipulate the raw 'argv[]' contents of a python process.
Summary(pl):	Modu³ jêzyka Python do manipulacji argv[] (w tym nazwy procesu)
Name:		python-procitle
Version:	0.0.1
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://ftp.psychosis.com/python/proctitle-%{version}.tar.gz

BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
BuildRequires:	kernel-headers
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module to manipulate the raw 'argv[]' contents of a python process.
Allows to change process name during runtime.

%description -l pl
Modu³ jêzyka Python do manipulacji argv[] (w tym tak¿e widocznej w np. w top nazwy procesu)

%prep
%setup -q -n proctitle-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir}
export PYTHONPATH

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/proctitle/*.py[oc]
%{py_sitedir}/proctitle/*.so


%clean
rm -rf $RPM_BUILD_ROOT
