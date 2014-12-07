# revision 34302
# category Package
# catalog-ctan /macros/latex/contrib/longfigure
# catalog-date 2014-06-13 11:14:52 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-longfigure
Version:	1.0
Release:	3
Summary:	Provides a figure-like environment that break over pages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/longfigure
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/longfigure.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/longfigure.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/longfigure.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The longfigure package uses and relabels components of the
well-known longtable package, written by David Carlisle, to
provide a table-like environment that can display a stream of
figures as a single figure that can break across pages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/longfigure/longfigure.sty
%doc %{_texmfdistdir}/doc/latex/longfigure/README
%doc %{_texmfdistdir}/doc/latex/longfigure/longfigure.pdf
#- source
%doc %{_texmfdistdir}/source/latex/longfigure/longfigure.dtx
%doc %{_texmfdistdir}/source/latex/longfigure/longfigure.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
