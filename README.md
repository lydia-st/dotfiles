# dotfiles

my super cool dotfiles managed with gnu stow, including configurations for:

* foot
* tmux
* sway
* waybar
* yambar
* zed

## dependencies

dependencies are listed in each individual configuration directory.
i'll probably provide a list here at some point in the future, but for now,
suffer.

## installation

```bash
git clone https://gitlab.com/ttaylor-st/dotfiles.git
cd dotfiles
stow -t ~ ./
```

## uninstallation

```bash
cd dotfiles
stow -t ~ -D ./
```

## license

everything is licensed under the mit license unless otherwise specified.
