# revision 25090
# category Package
# catalog-ctan /fonts/comfortaa
# catalog-date 2012-01-10 07:43:57 +0100
# catalog-license lppl1.3
# catalog-version 2.2
Name:		texlive-comfortaa
Version:	2.2
Release:	1
Summary:	Sans serif font, with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/comfortaa
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comfortaa.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comfortaa.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comfortaa.source.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/comfortaa/Comfortaa-Bold-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/comfortaa/Comfortaa-Bold.afm
%{_texmfdistdir}/fonts/afm/public/comfortaa/Comfortaa-Light-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/comfortaa/Comfortaa-Light.afm
%{_texmfdistdir}/fonts/afm/public/comfortaa/Comfortaa-Regular-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/comfortaa/Comfortaa-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/comfortaa/comfortaa-01.enc
%{_texmfdistdir}/fonts/enc/dvips/comfortaa/comfortaa-02.enc
%{_texmfdistdir}/fonts/enc/dvips/comfortaa/comfortaa-03.enc
%{_texmfdistdir}/fonts/enc/dvips/comfortaa/comfortaa-dotlessj.enc
%{_texmfdistdir}/fonts/map/dvips/comfortaa/comfortaa.map
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-01.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-02.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-03.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-01.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-02.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-03.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-Slanted-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Bold-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-01.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-02.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-03.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-01.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-02.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-03.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-Slanted-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Light-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-01.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-02.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-03.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-01.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-02.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-03.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-Slanted-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/comfortaa/Comfortaa-Regular-x2.tfm
%{_texmfdistdir}/fonts/truetype/public/comfortaa/Comfortaa-Bold.ttf
%{_texmfdistdir}/fonts/truetype/public/comfortaa/Comfortaa-Light.ttf
%{_texmfdistdir}/fonts/truetype/public/comfortaa/Comfortaa-Regular.ttf
%{_texmfdistdir}/fonts/type1/public/comfortaa/Comfortaa-Bold-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/comfortaa/Comfortaa-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/comfortaa/Comfortaa-Light-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/comfortaa/Comfortaa-Light.pfb
%{_texmfdistdir}/fonts/type1/public/comfortaa/Comfortaa-Regular-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/comfortaa/Comfortaa-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-lgr.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-ot1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-t1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-t2a.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-t2b.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-t2c.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-ts1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-Slanted-x2.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-lgr.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-ot1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-t1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-t2a.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-t2b.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-t2c.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-ts1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Bold-x2.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-lgr.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-ot1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-t1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-t2a.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-t2b.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-t2c.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-ts1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-Slanted-x2.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-lgr.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-ot1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-t1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-t2a.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-t2b.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-t2c.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-ts1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Light-x2.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-lgr.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-ot1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-t1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-t2a.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-t2b.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-t2c.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-ts1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-Slanted-x2.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-lgr.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-ot1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-t1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-t2a.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-t2b.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-t2c.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-ts1.vf
%{_texmfdistdir}/fonts/vf/public/comfortaa/Comfortaa-Regular-x2.vf
%{_texmfdistdir}/tex/latex/comfortaa/comfortaa.sty
%{_texmfdistdir}/tex/latex/comfortaa/lgrfco.fd
%{_texmfdistdir}/tex/latex/comfortaa/ot1fco.fd
%{_texmfdistdir}/tex/latex/comfortaa/t1fco.fd
%{_texmfdistdir}/tex/latex/comfortaa/t2afco.fd
%{_texmfdistdir}/tex/latex/comfortaa/t2bfco.fd
%{_texmfdistdir}/tex/latex/comfortaa/t2cfco.fd
%{_texmfdistdir}/tex/latex/comfortaa/ts1fco.fd
%{_texmfdistdir}/tex/latex/comfortaa/x2fco.fd
%doc %{_texmfdistdir}/doc/fonts/comfortaa/CHANGES
%doc %{_texmfdistdir}/doc/fonts/comfortaa/README
%doc %{_texmfdistdir}/doc/fonts/comfortaa/comfortaa-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/comfortaa/comfortaa-samples.tex
%doc %{_texmfdistdir}/doc/fonts/comfortaa/comfortaa.pdf
%doc %{_texmfdistdir}/doc/fonts/comfortaa/comfortaa.tex
%doc %{_texmfdistdir}/doc/fonts/comfortaa/manifest.txt
#- source
%doc %{_texmfdistdir}/source/fonts/comfortaa/Makefile
%doc %{_texmfdistdir}/source/fonts/comfortaa/comfortaa-01.etx
%doc %{_texmfdistdir}/source/fonts/comfortaa/comfortaa-02.etx
%doc %{_texmfdistdir}/source/fonts/comfortaa/comfortaa-03.etx
%doc %{_texmfdistdir}/source/fonts/comfortaa/comfortaa-diacritics.mtx
%doc %{_texmfdistdir}/source/fonts/comfortaa/comfortaa-dotlessj.etx
%doc %{_texmfdistdir}/source/fonts/comfortaa/comfortaa-drv.tex
%doc %{_texmfdistdir}/source/fonts/comfortaa/comfortaa-fixcyrillic.mtx
%doc %{_texmfdistdir}/source/fonts/comfortaa/comfortaa-fixgreek.mtx
%doc %{_texmfdistdir}/source/fonts/comfortaa/comfortaa-fixlatin.mtx
%doc %{_texmfdistdir}/source/fonts/comfortaa/comfortaa-fixtextcomp.mtx
%doc %{_texmfdistdir}/source/fonts/comfortaa/comfortaa-map.tex
%doc %{_texmfdistdir}/source/fonts/comfortaa/ttf2type1.pe

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-1
+ Revision: 762563
- Update to latest upstream package

* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 758837
- Update to latest upstream release

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 750400
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 718106
- texlive-comfortaa
- texlive-comfortaa
- texlive-comfortaa
- texlive-comfortaa

