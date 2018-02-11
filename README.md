# xmodmap
Custom keybinding for Linux keyboard

## Simple setup

*Some of command will require root permissions. Also suppose that you place
xmodmap repo at the root of you home path.*

```bash
$ cd
$ git clone git@github.com:abogoyavlensky/xmodmap.git
$ chmod a+x setup.sh
$ ./setup.sh
```

## Short description

### To know keycode run

```bash
$ xev -event keyboard
```

### To know name of key in your locale check in corresponding xkb symbols file

*For me, for example, it is `ru` locale. And rest of the tutorial will explain
how to do it for Russian language layout but it should be really simple adjust
for any other.*

```bash
$ cat /usr/share/X11/xkb/symbols/ru
```

### Setup script runs systemd setup

*You could check status of xmodmap service or entirly disable it*

```bash
$ sudo systemctl status xmodmap.service # Check if it's running
$ sudo systemctl stop xmodmap.service
$ sudo systemctl disable xmodmap.service
```
