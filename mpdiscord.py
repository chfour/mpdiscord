import pypresence, time, json, mpd

with open("config.json", "rt") as f:
    config = json.load(f)

print(f"using id {config['id']}...")
rpc = pypresence.Presence(config["id"])
rpc.connect()

print(f"connecting to {config['server']}...")
client = mpd.MPDClient()
client.idletimeout = None
if type(config["server"]) is str:
    client.connect(config["server"])
else:
    client.connect(config["server"][0], config["server"][1])
print("connected!")

while True:
    status = client.status()
    current_song = client.currentsong()

    if status["state"] == "play":
        if "albumartist" not in current_song:
            current_song["albumartist"] = current_song["artist"]

        presence = {
            "details": f"{current_song.get('track', '?')}: {current_song.get('title', '?')} ({status['audio'].split(':')[1]}bit@{int(status['audio'].split(':')[0])/1000}kHz, {current_song['file'].split('.')[-1]})",
            "state": f"on {current_song.get('albumartist', '?')} - {current_song.get('album', '?')}",
            "large_image": "0"
        }

        print(f"update: {' '.join([f'{p[0]}={p[1]!r}' for p in presence.items()])}")

        rpc.update(**presence)
    else:
        print("clear")
        rpc.clear()

    client.idle("player")
