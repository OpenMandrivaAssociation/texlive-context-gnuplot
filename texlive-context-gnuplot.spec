Name:		texlive-context-gnuplot
Version:	47085
Release:	2
Summary:	Inclusion of Gnuplot graphs in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-gnuplot
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-gnuplot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-gnuplot.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/metapost/context/third/gnuplot
%{_texmfdistdir}/tex/context/third/gnuplot
%doc %{_texmfdistdir}/doc/context/third/gnuplot

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost tex doc %{buildroot}%{_texmfdistdir}
