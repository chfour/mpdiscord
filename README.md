# mpdiscord

this is discord presence for mpd, the [music player daemon](https://musicpd.org/), written in python using [pypresence](https://github.com/qwertyquerty/pypresence) and [python-mpd2](https://musicpd.org/libs/python-mpd2/). very hacky, nuff said

## how to run it

install requirements with `pip install -r requirements.txt`

copy the config `cp config.json.dist config.json` and modify it (optionally)

run with `python mpdiscord.py`

will figure out a systemd service Later™
