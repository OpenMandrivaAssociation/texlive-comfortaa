Name:		texlive-comfortaa
Version:	54512
Release:	2
Summary:	Sans serif font, with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/comfortaa
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comfortaa.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comfortaa.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Comfortaa is a sans-serif font, comfortable in every aspect,
designed by Johan Aakerlund. The font, which includes three
weights (thin, regular and bold), is available on Johan's
deviantArt web page as TrueType files under the Open Font
License version 1.1. This package provides support for this
font in LaTeX, and includes both the TrueType fonts, and
conversions to Adobe Type 1 format.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/comfortaa
%{_texmfdistdir}/fonts/map/dvips/comfortaa
%{_texmfdistdir}/fonts/tfm/aajohan/comfortaa
%{_texmfdistdir}/fonts/truetype/aajohan/comfortaa
%{_texmfdistdir}/fonts/type1/aajohan/comfortaa
%{_texmfdistdir}/fonts/vf/aajohan/comfortaa
%{_texmfdistdir}/tex/latex/comfortaa
%doc %{_texmfdistdir}/doc/fonts/comfortaa

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
