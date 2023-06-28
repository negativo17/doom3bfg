Name:           doom3bfg
Version:        1.1400
Release:        4
Summary:        Doom 3 BFG Edition
License:        Proprietary
URL:            http://www.idsoftware.com/
BuildArch:      noarch

# Doom 3 BFG Edition: Retail game data
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.desktop 
Source2:        %{name}
Source3:        doom3bfg-24.png
Source4:        doom3bfg-32.png
Source5:        doom3bfg-48.png
Source6:        doom3bfg-256.png

BuildRequires:  desktop-file-utils

Requires:       doom3bfg-engine >= %{version}
Requires:       doom3bfg-lights-data >= 1.3.0

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
%setup -q -c -n doom3bfg

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -fr base %{buildroot}%{_datadir}/%{name}/

install -p -m 0644 -D %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -p -m 0755 -D %{SOURCE2} %{buildroot}%{_bindir}/%{name}
install -p -m 0644 -D %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
install -p -m 0644 -D %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 0644 -D %{SOURCE5} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -m 0644 -D %{SOURCE6} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Wed Jun 28 2023 Simone Caronni <negativo17@gmail.com> - 1.1400-4
- Add tarball content list and declare as sources the single extra files.
- Drop EL7 support.

* Fri Mar 31 2023 Simone Caronni <negativo17@gmail.com> - 1.1400-3
- Update SPEC file.

* Thu Jul 02 2020 Simone Caronni <negativo17@gmail.com> - 1.1400-2
- Remove dist tag.

* Fri Nov 15 2013 Simone Caronni <negativo17@gmail.com> - 1.1400-1
- First build.
