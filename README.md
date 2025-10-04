# Audapa

## Install
On Ubuntu(jammy noble) from PPA.
```sh
sudo add-apt-repository ppa:colin-i/ppa
```
Or the *manual installation step* from this link *https://gist.github.com/colin-i/e324e85e0438ed71219673fbcc661da6* \
Install:
```sh
sudo apt-get install audapa
```
Will also install libgtk-4-1 if is not already installed.\
\
\
On openSUSE, run the following as __root__:\
For openSUSE Tumbleweed(x86_64/i586 aarch64):
```sh
zypper addrepo https://download.opensuse.org/repositories/home:costin/openSUSE_Tumbleweed/home:costin.repo
```
And:
```sh
zypper refresh
zypper install python313-audapa
```
Replace *python313* with *python312* or *python311* if needed.\
Will also install libgtk-4-1 if is not already installed.\
\
\
On Fedora 42/43(x86_64 aarch64), run the following as __root__:
```sh
dnf copr enable colin/project
dnf install python3-audapa
```
And having gtk4.\
\
\
On Arch Linux, <i>.zst</i> file from [releases](https://github.com/colin-i/audapa/releases). Or:
```sh
yay -Sy python-audapa
```
Will also install gtk4 if is not already installed.\
\
\
From [PyPI](https://pypi.org/project/audapa):
```sh
pip install audapa
```
And having gtk4. Also working on Windows MinGW64 MSys2 with the right PyAudio bindings.\
\
\
On linux distributions(x86_64) with gtk4, <i>.AppImage</i> file from [releases](https://github.com/colin-i/audapa/releases).

## From source
Requiring python >= 3.8 .\
More info at setup.pre.py file.\
If there is a problem with pyaudio playback, see the *Info* section at this page.

## [Info](https://github.com/colin-i/audapa/blob/master/info.md)

## Donations
The *donations* section is here
*https://gist.github.com/colin-i/e324e85e0438ed71219673fbcc661da6*
