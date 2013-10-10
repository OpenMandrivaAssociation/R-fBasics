%global packname  fBasics
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3010.86
Release:          1
Summary:          Rmetrics - Markets and Basic Statistics
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-MASS R-methods R-timeDate R-timeSeries 
Requires:         R-akima R-spatial R-RUnit R-tcltk 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-MASS R-methods R-timeDate R-timeSeries
BuildRequires:    R-akima R-spatial R-RUnit R-tcltk 
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Environment for teaching "Financial Engineering and Computational Finance"
NOTE: SEVERAL PARTS ARE STILL PRELIMINARY AND MAY BE CHANGED IN THE
FUTURE. THIS TYPICALLY INCLUDES FUNCTION AND ARGUMENT NAMES, AS WELL AS
DEFAULTS FOR ARGUMENTS AND RETURN VALUES. Please donate, www.rmetrics.org,
to support future activities of the Rmetrics association.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/COPYRIGHT.html
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/unitTests

