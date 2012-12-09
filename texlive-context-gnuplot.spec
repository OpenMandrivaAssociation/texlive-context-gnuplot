# revision 27068
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-gnuplot
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-gnuplot
Version:	20060827
Release:	5
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
%{_texmfdistdir}/tex/context/third/gnuplot/t-gnuplot.tex
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


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20060827-5
+ Revision: 812149
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20060827-4
+ Revision: 804540
- Update to latest release.

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 20060827-3
+ Revision: 762595
- Update to latest upstream package

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20060827-2
+ Revision: 750499
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20060827-1
+ Revision: 718134
- texlive-context-gnuplot
- texlive-context-gnuplot
- texlive-context-gnuplot
- texlive-context-gnuplot

