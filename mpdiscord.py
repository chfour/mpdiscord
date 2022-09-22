import pypresence, time, json

with open("config.json", "rt") as f:
    config = json.load(f)

print(f"using id {config['id']}...")
rpc = pypresence.Presence(config["id"])
rpc.connect()
rpc.update(details="details", state="state")
while True:
    time.sleep(1)
