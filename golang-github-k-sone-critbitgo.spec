# Run tests in check section
%bcond_without check

%global goipath         github.com/k-sone/critbitgo
Version:                1.2.0

%global common_description %{expand:
Crit-bit trees in golang and its applications.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Crit-bit trees in golang and its applications
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc CHANGES.md README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- First package for Fedora

