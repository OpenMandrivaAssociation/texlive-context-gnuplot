Name:		texlive-context-gnuplot
Version:	20060827
Release:	1
Summary:	Inclusion of Gnuplot graphs in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-gnuplot
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-gnuplot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-gnuplot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-context
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Requires(post):	texlive-context.bin

%description
Enables simple creation and inclusion of graphs with Gnuplot.
The package writes a script into temporary file, runs Gnuplot
and includes the resulting graphic directly into the document.
See the ConTeXt Garden package page for further details.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mtxrun_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/context/third/gnuplot/mp-gnuplot.mp
%{_texmfdistdir}/tex/context/third/gnuplot/t-gnuplot.tex
%doc %{_texmfdistdir}/doc/context/third/gnuplot/examples/example.plt
%doc %{_texmfdistdir}/doc/context/third/gnuplot/examples/fullpage-example.pdf
%doc %{_texmfdistdir}/doc/context/third/gnuplot/examples/fullpage-example.tex
%doc %{_texmfdistdir}/doc/context/third/gnuplot/gnuplot-context-doc.pdf
%doc %{_texmfdistdir}/doc/context/third/gnuplot/gnuplot-context-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost tex doc %{buildroot}%{_texmfdistdir}
