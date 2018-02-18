# Setup instruction

*Tested on Ubuntu 16.04 but also should work on any linux*

### Disable default behavior of Super key

First of all you should install `CompizConfig Settings Manager`:

```bash
$ sudo apt-get install sudo apt-get install compizconfig-settings-manager
```

Open it, got to "Ubuntu Unity Plugin" and disable or override keybindings
for super key such as:

* General->Key to lock the screen
* Launcher->Key to show the Dash, Launcher and Help Overlay

### Make Caps Lock as Super

Then install `Gnome Tweak Tools``:add the program in 

```bash
$ sudo apt-get install gnome-tweak-tool
```

Open tweak tools and chose settings:

* Typing->Caps Lock key behavior->Make Caps Lock an additional Super

### Change keyboard key bindings

Install `AutoKey`:

```bash
$ sudo apt-get install autokey-gtk
```

Open the program and disable default bindings for Super key inside AutoKey 
itself:

* Edit->Preferences->Special Hotkeys
* Make clear all of them

Copy predefined keybindings from current repository:

```bash
$ git clone https://github.com/abogoyavlensky/keymap.git
$ cp -a keymap/Phrases/. ~/.config/autokey/data/My\ Phrases
```

Also nice to have `AutoHokey` always running. For that please put it to 
autostart:

* Open `Gnome Tweak Tools` and add the program in the tab called 
`Startup Application`.

### Keyboard preview

That's it. Now your keyboard key bindings should look like:
![Keyboard preview](keyboard.png?raw=true "Title")

*Arrow keys, backspace and delete also work for russian layout but without 
other modifiers.*

## Additional info

### To know keycode usual run

```bash
$ xev -event keyboard
```

### To know name of special key please check wiki page of AutoKey

https://github.com/autokey/autokey/wiki/Special-Keys

### Useful links

* http://tonsky.me/blog/cursor-keys/ - article inspired me to rebind keys;
* https://github.com/madslundt/keybindings - aproach for Linux but slightly 
different;
* http://www.keyboard-layout-editor.com/ - help with makeing keyboard picture.

### TODO and caveats:

* bind `Insert` key to `u` for example;
* some of helpful ubuntu system key bindings still doesn't work with new arrow 
keys, for example: `<ctrl>+<alt>+<down>` to move current window to bottom 
workspace and so on.
