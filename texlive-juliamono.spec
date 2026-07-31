%global tl_name juliamono
%global tl_revision 79753

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.06a
Release:	%{tl_revision}.1
Summary:	Support for the TrueType font JuliaMono
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/juliamono
License:	lppl1.3 ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/juliamono.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/juliamono.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
JuliaMono is a monospaced font for scientific and technical computing.
There are font files for Regular, Italic, Bold and BoldItalic in light,
medium, black and extra bold version. There are more than 12 thousand
glyphs in every font file.

