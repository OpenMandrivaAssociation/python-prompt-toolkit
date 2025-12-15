%global srcname prompt_toolkit
%global pypi_name prompt-toolkit

%bcond_without tests

Name:           python-%{pypi_name}
Version:        3.0.52
Release:        1
Summary:        Library for building powerful interactive command lines in Python
Group:          Development/Python
License:        BSD-3-Clause
URL:            https://github.com/jonathanslenders/python-prompt-toolkit
Source0:        https://files.pythonhosted.org/packages/source/p/prompt_toolkit/prompt_toolkit-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python%{pyver}dist(setuptools)
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif
BuildSystem:    python

%description
Python Prompt Toolkit is a library for building powerful interactive command
line applications in Python.

Please notice that this is prompt_toolkit 2.0. It is incompatible with the
1.0 branch, but much better in many regards.


%files
%license LICENSE
%doc README.rst
