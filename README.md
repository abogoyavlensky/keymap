# Keyboard preview

![Keyboard preview](keyboard-layout.png?raw=true "Title")

*Our aim to have a keyboard which would be convenient for typing without distraction.
In current instruction we will get keybindings look like in preview,
but you could change any of them on your own using current example.*


# Setup instruction for Linux with Key Mapper

*Key Mapper link: https://github.com/sezanzeb/key-mapper*

## Disable Caps Lock

Then install `GNOME Tweaks`

```bash
$ sudo apt-get install gnome-tweak-tool
```

Open tweak tools and choose settings in
"Keyboard & Mouse" -> "Additional Layout Options" -> "Caps Lock behavior":

* "Caps Lock is disabled"


## Make Control as Win


Open tweak tools and choose settings in 
"Keyboard & Mouse" -> "Additional Layout Options" -> "Alt/Win behavior":

* "Ctrl is mapped to Alt; Alt is mapped to Win"

## Install the latest Key Mapper

```bash
sudo apt install git python3-setuptools
wget https://github.com/sezanzeb/key-mapper/releases/download/0.8.1/key-mapper-0.8.1.deb
sudo dpkg -i key-mapper-0.8.1.deb
```

## Configure Key Mapper

Create new preset with any name you choose. 
Then copy text from config from file of this repo:

```bash 
cat key-mapper/presets/USB-HID Keyboard/Andrey.json 
```

to the Key Mapper preset config: `.config/key-mapper/presets/USB-HID Keyboard`.

*Note: a keyboard name could be different.*

*Note: other config files in dir `key-mapper` of the repo are for backup purposes.*

## Enable mapping

Now you could open Key Mapper and chose the preset you configured.
After that press `Apply`. And key mapping should work immediatly.
If you want to make it default on system start enable `Autoload` switch.


# Setup instruction for Linux with Autokey (DEPRECATED)

## Requirements

* Ubuntu 18.04
* GNOME Tweaks
* AutoKey

*Tested Ubuntu 18.04.

## Change keys for a couple of default actions

In Autokey itself *Settings -> Devices -> Keyboard:* 

```
Lock screen -> Shift+Ctrl+L
Close window -> Shift+Ctrl+W
```

## Make Caps Lock as Hyper

Then install `GNOME Tweaks`

```bash
$ sudo apt-get install gnome-tweak-tool
```

Open tweak tools and choose settings in
"Keyboard & Mouse" -> "Additional Layout Options" -> "Caps Lock behavior":

* Typing->Caps Lock key behavior->Make Caps Lock an additional Hyper


## Make Control as Win

Open `GNOME Tweaks`

Open tweak tools and choose settings in 
"Keyboard & Mouse" -> "Additional Layout Options" -> "Alt/Win behavior":

* "Ctrl is mapped to Alt; Alt is mapped to Win"


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

## Enable karabiner_grabber

*Source: https://github.com/pqrs-org/Karabiner-Elements/issues/3011#issuecomment-1046265810*

- go to macOS settings: System Preferences -> Security & Privacy -> Input Monitoring
- unlock to make changes
- if you don't see `karabiner_grabber` click plus "+" button
- add the /Library/Application Support/org.pqrs/Karabiner-Elements/bin/karabiner_grabber
- and enable it by clicking checkbox

## Import configuration

Open next links to the browser to import configuration into Karabiner:
- `karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/abogoyavlensky/keymap/master/Karabiner/keymap-arrows.json`
- `karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/abogoyavlensky/keymap/master/Karabiner/keymap-f-keys.json`

# That's it

Now your keyboard should look like on preview above.

*All key bindings also work for any additional layout on your machine
without delay after switching between them.*

# Additional info

## UK keyboard

### Mapping UK keyboard signs to US

- `karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/abogoyavlensky/keymap/master/Karabiner/keymap-uk-pound-to-hash.json`

### Reassign § key to ~

- [https://github.com/pqrs-org/Karabiner-Elements/issues/1365](https://github.com/pqrs-org/Karabiner-Elements/issues/1365)


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

* in Autokey some of helpful Ubuntu system key bindings don't work with new arrow
keys. For example, you should still use ordinary arrows to move
current window to bottom workspace and so on: `<ctrl>+<alt>+<down>`. 
