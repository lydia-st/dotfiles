# waybar

my waybar config, of course very barebones, very speed.


## "building" and editing

when changing the config, you should avoid editing the `config.jsonc` file
directly, as it is generated from the `config.json` file. they're really both
the same, but with different names.

when editing the configs, you can run [`watcher.py`](.watcher.py) to
automatically "build" the `config.jsonc` file and reload waybar. it will watch
for changes in the config.json and style.css files. make sure the file is
executable.

## requirements

* waybar
* make sure you have some sort of nerd font installed for icons.
* the pulseaudio module requires pulseaudio or pipewire.
* the mpris module requires an [mpris client](https://wiki.archlinux.org/title/MPRIS#Supported_clients).
* the sway/* modules require sway.
