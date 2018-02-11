# xmodmap
Custom keybinding for Linux keyboard

## Simple setup

*Some of command will require root permissions.*

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
