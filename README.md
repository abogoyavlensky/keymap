# Setup instruction

*Tested on Pop!_OS (based on Ubuntu 18.04). But also should work
on clean Ubuntu 18.04 the same way*

### Slightly change default behavior of Super key

First of all we are going to change couple of key binding in system settings:
*Settings -> Devices -> Keyboard*

```
Lock screen -> Shift+Ctrl+L
Close window -> Shift+Ctrl+W
```

### Make Caps Lock as Hyper

Then install `Gnome Tweak Tools`

```bash
$ sudo apt-get install gnome-tweak-tool
```

Open tweak tools and chose settings:

* Typing->Caps Lock key behavior->Make Caps Lock an additional Hyper

### Change keyboard key bindings

Install `AutoKey`:

```bash
$ sudo apt-get install autokey-gtk
```

Open the program and disable default bindings for Hyper key inside AutoKey
itself:

* Edit->Preferences->Special Hotkeys
* Make clean all of them

Copy predefined keybindings from current repository:

```bash
$ git clone https://github.com/abogoyavlensky/keymap.git
$ ln -s /full/path/to/keymap/Phrases /full/path/to/.config/autokey/data/Phrases
```

Also nice to have `AutoHokey` always running. For that, please put it to
autostart:

* Open `Gnome Tweak Tools` and add the program in the tab called
`Startup Application`.

### Keyboard preview

That's it. Now your keyboard key bindings should look like:

![Keyboard preview](keyboard.png?raw=true "Title")

*All key bindings also work for any additional layout on your machine
without delay after switching between them.*

## Additional info

### To know keycode usual keys run

```bash
$ xev -event keyboard
```

### To know name of special keys please check wiki page of AutoKey

https://github.com/autokey/autokey/wiki/Special-Keys

### Heavily inspired by

* http://tonsky.me/blog/cursor-keys/ - article inspired me to rebind keys;
* https://github.com/madslundt/keybindings - aproach for Linux but slightly
different;
* http://www.keyboard-layout-editor.com/ - help with makeing keyboard picture.

### Caveats:

* some of helpful ubuntu system key bindings don't work with new arrow
keys, for example: `<ctrl>+<alt>+<down>` to move current window to bottom
workspace and so on, and you should still use ordinary arrows for that.
