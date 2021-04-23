#! /bin/bash

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
nitrogen --restore &
nm-applet &
xfce4-power-manager &
picom &
dunst &
