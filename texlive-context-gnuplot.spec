# revision 30380
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-gnuplot
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-gnuplot
Version:	20060827
Release:	11
Summary:	Inclusion of Gnuplot graphs in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-gnuplot
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-gnuplot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-gnuplot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
Enables simple creation and inclusion of graphs with Gnuplot.
The package writes a script into temporary file, runs Gnuplot
and includes the resulting graphic directly into the document.
See the ConTeXt Garden package page for further details.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/context/third/gnuplot/mp-gnuplot.mp
%{_texmfdistdir}/tex/context/third/gnuplot/t-gnuplot.mkii
%{_texmfdistdir}/tex/context/third/gnuplot/t-gnuplot.mkiv
%doc %{_texmfdistdir}/doc/context/third/gnuplot/example.plt
%doc %{_texmfdistdir}/doc/context/third/gnuplot/fullpage-example.pdf
%doc %{_texmfdistdir}/doc/context/third/gnuplot/fullpage-example.tex
%doc %{_texmfdistdir}/doc/context/third/gnuplot/gnuplot-context-doc.pdf
%doc %{_texmfdistdir}/doc/context/third/gnuplot/gnuplot-context-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost tex doc %{buildroot}%{_texmfdistdir}
