# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# This file has since been modified by Connor Prettyman, where, parts of these 
# modificaions have been taken from the confiuration file of Derek Taylor
# (DistroTube). You can see his configuration file at 
# https://gitlab.com/dwt1/dotfiles/-/blob/master/.config/qtile.
# Also support his great work on Patreon, and view his videos on LBRY/YouTube.

import os
import re
import socket
import subprocess

from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook
from libqtile.config import KeyChord, Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.command import lazy

mod = "mod4"
terminal = "alacritty"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    Key([mod], "d", lazy.spawn('rofi -show drun -font "Iosevka 11"'), desc="Launch Rofi"),
]

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.MonadTall(border_focus="#1e88e5", border_normal="#1f1f1f", border_width=1, margin=15, name="MonadTall"),
    #layout.Stack(num_stacks=2, border_focus="#1e88e5"),
    # Try more layouts by unleashing below layouts.
    #layout.Bsp(border_focus="#1e88e5"),
    #layout.Columns(border_focus="#1e88e5", border_normal="#1f1f1f", border_width=1, margin=15, name="Columns"),
    #layout.Matrix(border_focus="#1e88e5", border_normal="#1f1f1f", border_width=1, margin=15, name="Matrix"),
    layout.Max(border_focus="#1e88e5", border_normal="#1f1f1f", border_width=1, margin=15, name="Max"),
    layout.MonadWide(border_focus="#1e88e5", border_normal="#1f1f1f", border_width=1, margin=15, name="MonadWide"),
    layout.RatioTile(border_focus="#1e88e5", border_normal="#1f1f1f", border_width=1, margin=15, name="RatioTile"),
    #layout.Tile(border_focus="#1e88e5", border_normal="#1f1f1f", border_width=1, margin=15, name="Tile"),
    #layout.TreeTab(border_focus="#1e88e5"),
    #layout.VerticalTile(border_focus="#1e88e5"),
    #layout.Zoomy(border_focus="#1e88e5"),
    ]

widget_defaults = dict(
    font='Iosevka',
    fontsize=14,
    padding=0,
)
extension_defaults = widget_defaults.copy()

# Mouse Callbacks

def run_updates(qtile):
	qtile.cmd_spawn(terminal + " -e trizen -Syu")

def update_widget(qtile):
    qtile.cmd_spawn("sh ~/.config/qtile/scripts/check-all-updates.sh")

def power_menu(qtile):
	qtile.cmd_spawn("rofi -show powermenu -modi powermenu:~/.config/rofi/scripts/rofi-power-menu.sh -width 6 -lines 6")

def net_settings(qtile):
	qtile.cmd_spawn(terminal + " -e nmtui")

# Bars & Widgets

screens = [
    Screen(
        top=bar.Bar(
            [
            	widget.Sep(
                            linewidth=0,
                            padding=5
                            ),

                widget.GroupBox(
                            highlight_method="line"
                            ),

                widget.PulseVolume(
                            ),

                widget.Prompt(
                            ),

                widget.WindowName(
                            ),

                widget.Clock(
                            format='  %a %d %b %Y |  %T ',
                            background="#1e88e5"
                            ),

                widget.Spacer(
                            length=bar.STRETCH
                            ),
                widget.Net(
                            interface="wlp4s0"
                            ),

                widget.CurrentLayout(
                            ),

                widget.TextBox(
                    " Updates: "
                            ),

                widget.Pacman(
                            update_interval = 1800,
                            mouse_callbacks = {'Button1': run_updates},
                            ),

                widget.Wlan(
                            interface="wlp4s0",
                            format=" {essid} {percent:2.0%}",
                            mouse_callbacks={'Button1': net_settings}
                            ),

                widget.Systray(
                            icon_size="20",
                            background="#1e88e5",
                            ),

                widget.TextBox(
                            " 拉 ",
                            mouse_callbacks={'Button1': power_menu}
                            ),

            	# widget.Sep(linewidth=0, padding=5),
            ],
            24, background="#1f1f1f",
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
	home = os.path.expanduser('~')
	subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
