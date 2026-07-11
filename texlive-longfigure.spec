%global tl_name longfigure
%global tl_revision 34302

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Provides a figure-like environment that break over pages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/longfigure
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/longfigure.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/longfigure.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/longfigure.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The longfigure package uses and relabels components of the well-known
longtable package, written by David Carlisle, to provide a table-like
environment that can display a stream of figures as a single figure that
can break across pages.

