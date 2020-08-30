#! /bin/bash

# Install Script for Configuration Files

cd $HOME

echo Cloning Github Repository...

git clone https://github.com/Conjuam/dotfiles Conjuam-Dotfiles

echo Copying Files To Their Locations...

cp -rviT Conjuam-Dotfiles $HOME

echo Cleaning Up...

rm -rf Conjuam-Dotfiles

echo Done! Log Out or Reboot to ensure changes are successful!