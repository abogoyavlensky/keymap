# Keyboard preview

![Keyboard preview](keyboard-layout.png?raw=true "Title")

*Our aim to have a keyboard which would be convenient for typing without distraction.
In current instruction we will get keybindings look like in preview,
but you could change any of them on your own using current example.*

# Setup instruction for Linux

## Requirements

* Ubuntu 18.04
* GNOME Tweaks
* AutoKey

*Tested on [Pop!_OS](https://system76.com/pop) (based on Ubuntu 18.04).
But also should work on clean Ubuntu 18.04 the same way.*

## Change keys for a couple of default actions

*Settings -> Devices -> Keyboard:*

```
Lock screen -> Shift+Ctrl+L
Close window -> Shift+Ctrl+W
```

## Make Caps Lock as Hyper

Then install `GNOME Tweaks`

```bash
$ sudo apt-get install gnome-tweak-tool
```

Open tweak tools and choose settings:

* Typing->Caps Lock key behavior->Make Caps Lock an additional Hyper

## Change keyboard key bindings

Install `AutoKey`:

```bash
$ sudo apt-get install autokey-gtk
```

Open the program and disable default bindings for Hyper key inside AutoKey
itself:

* Edit->Preferences->Special Hotkeys
* Make clean all of them

Add symlink for predefined keybindings from current repository:

```bash
$ git clone https://github.com/abogoyavlensky/keymap.git
$ ln -s /full/path/to/keymap/Phrases /full/path/to/.config/autokey/data/Phrases
```

Also nice to have `AutoKey` always running. For that, please put it to
autostart:

* Open `Gnome Tweak Tools` and add the program in the tab called
`Startup Application`.

# Setup instruction for macOS

## Requirements
* Tested on macOS 10.14.4
* Install [Karabiner](https://pqrs.org/osx/karabiner/index.html)

## Import configuration

Copy the next link to the browser to import configuration into Karabiner:
`karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/abogoyavlensky/keymap/master/Karabiner/keymap.json`

# That's it

Now your keyboard should look like on preview above.

*All key bindings also work for any additional layout on your machine
without delay after switching between them.*

# Additional info

## To know keycode of usual keys run following command and press the key

```bash
$ xev -event keyboard
```

## To know name of special keys please check wiki page of AutoKey

https://github.com/autokey/autokey/wiki/Special-Keys

## Useful links

* http://tonsky.me/blog/cursor-keys/ - inspiration;
* https://github.com/madslundt/keybindings - different approach for Linux;
* http://www.keyboard-layout-editor.com/ - keyboard picture.

## Caveats:

* some of helpful Ubuntu system key bindings don't work with new arrow
keys. For example, you should still use ordinary arrows to move
current window to bottom workspace and so on: `<ctrl>+<alt>+<down>`
