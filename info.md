To remove configuration files launch the program with one argument.\
```rpm -i --nodeps``` and ```yum remove --noautoremove``` to deal at pyaudioo...rpm, audapa...rpm and python3-pyaudio.\
PortAudio can ask for portaudio.h (the file is in portaudio19-dev).\
PyAudio and python 3.10 can report playback errors (install from [here](https://github.com/colin-i/pyaudio) and add libportaudio2 package).\
The audio records are saved where *appdirs.user_data_dir("audapa")* points at (example: ~/.local/share/audapa/1650089398.wav).\
The points are saved in the *\_audapacache\_* folder which is at the file folder or in the home folder if the option is selected. (example: /home/x/audapa/\_audapacache\_/example.wav.json or /home/x/\_audapacache\_/home/x/audapa/example.wav.json)\
Knowing where the points are saved, in the root folder at source, write "example.wav" and click the build button from top-right.\
[Git Page](https://github.com/colin-i/audapa)
