Name:           doom3bfg
Version:        1.1400
Release:        2
Summary:        Doom 3 BFG Edition
Group:          Amusements/Games
License:        Proprietary
URL:            http://www.idsoftware.com/
BuildArch:      noarch

Source0:        %{name}.tar.gz
# Doom 3 BFG Edition: Retail game data
Source1:	    %{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  tar
Requires:       doom3bfg-engine >= %{version}

%description
Developed by id Software, the original team responsible for the franchise
legacy, DOOM 3 BFG Edition features Steam Achievements, improved rendering and
lighting, and a new checkpoint save system allowing for smoother progression
through the game. id has fine-tuned the controls to bringing even more intensity
to the DOOM single and multiplayer experience and all DOOM 3 games now feature
the new armor-mounted flashlight, allowing players to illuminate dark corners
and blast enemies at the same time.

DOOM 3, Resurrection of Evil and the all-new ‘Lost Mission’ have all been
optimized in stereoscopic 3D (on supported hardware), further immersing the
player in the demonic world of this terrifying horror masterpiece.
The Lost Mission:

DOOM 3 BFG Edition includes an all-new chapter in the DOOM 3 experience, ‘The
Lost Mission’, featuring eight heart-pounding single player levels and a
completely new storyline that will have players once again on the edge of their
seats. 

%prep
%setup -q -c -n doom3bfg -a 1
mv base ./%{_datadir}/%{name}/

%install
cp -fr usr %{buildroot}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Thu Jul 02 2020 Simone Caronni <negativo17@gmail.com> - 1.1400-2
- Remove dist tag.

* Fri Nov 15 2013 Simone Caronni <negativo17@gmail.com> - 1.1400-1
- First build.
