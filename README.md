# dotfiles
My dotfiles for Configs.

Within this repo are dotfiles for all programs where they have been modified from their defaults.
These include:
- abcde
- Alacritty
- GNU Nano
- i3 (Gaps)
- Neofetch
- Polybar
- QTile
- Rofi

# Dependencies
Dependencies for the included Config Files are as follows:
- abcde
  - flac
  - vorbis-tools
- alacritty
  - no additional dependencies
- GNU Nano
  - no additional dependencies
- i3(-gaps)
  - blurlock
  - lxterminal
  - nitrogen
  - polkit-gnome
  - polybar
  - rofi
- Neofetch
  - no additional dependencies
- Polybar
  - alsa
  - i3
  - lxterminal
  - nmtui
  - pulseaudio
  - trizen
  - xbacklight
- QTile
  - alacritty
  - arcolinux-logout
  - nitrogen
  - nmtui
  - numlockx
  - pavucontrol
  - picom (Config for this is in ".config/qtile/scripts/")
  - polkit-gnome
  - rofi
  - scrot
  - thunar
  - trizen
  - xfce4-notifyd
  - xfce4-power-manager
  - xfce4-screenshooter
- Rofi
  - no additional dependencies
- oh-my-bash (optional)

You will need to source these yourself, as instructions vary by distro. Having said that, some or all of these packages should be included in your distro's repositories.

# Installation

**MAKE SURE TO CREATE A BACKUP OF YOUR PREVIOUS CONFIGURATION FIRST.**

**I AM NOT RESPONSIBLE FOR DATA LOSS, MISERY, THERMONUCLEAR WAR OR INJURY.**

**ALWAYS AUDIT SCRIPTS FOUND ON THE INTERNET BEFORE YOU EXECUTE THEM!!!**

---

Download the [setup.sh](https://raw.githubusercontent.com/Conjuam/dotfiles/master/setup.sh) file (add execute permissions if necessary) then run (NOT AS SUDO!). Follow the instructions and then make sure log out and log back in. Dotfiles should now be applied.
