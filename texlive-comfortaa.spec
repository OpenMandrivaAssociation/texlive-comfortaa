%global tl_name comfortaa
%global tl_revision 77682
%global tl_version 3.2

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Sans serif font, with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/comfortaa
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/comfortaa.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/comfortaa.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Comfortaa is a sans-serif font, comfortable in every aspect, designed by
Johan Aakerlund. The font, which includes three weights (thin, regular
and bold), is available on Johan's deviantArt web page as TrueType files
under the Open Font License version 1.1. This package provides support
for this font in LaTeX, and includes both the TrueType fonts, and
conversions to Adobe Type 1 format.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from comfortaa:
Map comfortaa.map
TL_DROPIN_EOF
