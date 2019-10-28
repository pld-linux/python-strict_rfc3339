#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

Summary:	Strict, simple, lightweight RFC3339 functions for Python 2
Summary(pl.UTF-8):	Ścisłe, proste, lekkie funkcje RFC3339 dla Pythona 2
Name:		python-strict_rfc3339
Version:	0.7
Release:	3
License:	GPL v3+
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/strict-rfc3339/
Source0:	https://files.pythonhosted.org/packages/source/s/strict-rfc3339/strict-rfc3339-%{version}.tar.gz
# Source0-md5:	4d9b635b4df885bc37bc1189d66c9abc
URL:		https://pypi.python.org/pypi/strict-rfc3339/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Strict, simple, lightweight RFC3339 functions for Python 2.

%description -l pl.UTF-8
Ścisłe, proste, lekkie funkcje RFC3339 dla Pythona 2.

%package -n python3-strict_rfc3339
Summary:	Strict, simple, lightweight RFC3339 functions for Python 3
Summary(pl.UTF-8):	Ścisłe, proste, lekkie funkcje RFC3339 dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-strict_rfc3339
Strict, simple, lightweight RFC3339 functions for Python 3.

%description -n python3-strict_rfc3339 -l pl.UTF-8
Ścisłe, proste, lekkie funkcje RFC3339 dla Pythona 3.

%prep
%setup -q -n strict-rfc3339-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%{py_sitescriptdir}/strict_rfc3339.py[co]
%{py_sitescriptdir}/strict_rfc3339-%{version}-py*.egg-info

%files -n python3-strict_rfc3339
%defattr(644,root,root,755)
%doc AUTHORS README.md
%{py3_sitescriptdir}/strict_rfc3339.py
%{py3_sitescriptdir}/__pycache__/strict_rfc3339.cpython-*.py[co]
%{py3_sitescriptdir}/strict_rfc3339-%{version}-py*.egg-info
