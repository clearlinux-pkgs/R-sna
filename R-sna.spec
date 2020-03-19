#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sna
Version  : 2.5
Release  : 25
URL      : https://cran.r-project.org/src/contrib/sna_2.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sna_2.5.tar.gz
Summary  : Tools for Social Network Analysis
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-sna-lib = %{version}-%{release}
Requires: R-network
Requires: R-rgl
Requires: R-statnet.common
BuildRequires : R-network
BuildRequires : R-rgl
BuildRequires : R-statnet.common
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-sna package.
Group: Libraries

%description lib
lib components for the R-sna package.


%prep
%setup -q -c -n sna

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575999959

%install
export SOURCE_DATE_EPOCH=1575999959
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sna
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sna
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sna
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc sna || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sna/DESCRIPTION
/usr/lib64/R/library/sna/INDEX
/usr/lib64/R/library/sna/Meta/Rd.rds
/usr/lib64/R/library/sna/Meta/data.rds
/usr/lib64/R/library/sna/Meta/features.rds
/usr/lib64/R/library/sna/Meta/hsearch.rds
/usr/lib64/R/library/sna/Meta/links.rds
/usr/lib64/R/library/sna/Meta/nsInfo.rds
/usr/lib64/R/library/sna/Meta/package.rds
/usr/lib64/R/library/sna/NAMESPACE
/usr/lib64/R/library/sna/R/sna
/usr/lib64/R/library/sna/R/sna.rdb
/usr/lib64/R/library/sna/R/sna.rdx
/usr/lib64/R/library/sna/data/coleman.RData
/usr/lib64/R/library/sna/help/AnIndex
/usr/lib64/R/library/sna/help/aliases.rds
/usr/lib64/R/library/sna/help/paths.rds
/usr/lib64/R/library/sna/help/sna.rdb
/usr/lib64/R/library/sna/help/sna.rdx
/usr/lib64/R/library/sna/html/00Index.html
/usr/lib64/R/library/sna/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sna/libs/sna.so
/usr/lib64/R/library/sna/libs/sna.so.avx2
/usr/lib64/R/library/sna/libs/sna.so.avx512
