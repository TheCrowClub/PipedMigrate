from json import dumps, load

from requests import Session, get, post


def get_token(instance, username, password):
    return post(
        f"{instance}/login", json={"username": username, "password": password}
    ).json()


def get_playlists(instance, token, file="export.json"):
    lists = {}
    plists = get(f"{instance}/user/playlists", headers={"Authorization": token}).json()
    for x in plists:
        req = get(f"{instance}/playlists/{x.get('id')}")
        lists[x.get("name")] = []
        for y in req.json().get("relatedStreams"):
            lists[x.get("name")].append(y.get("url"))
    with open(file, "w") as f:
        f.write(dumps(lists, indent=4, ensure_ascii=False))


def save_playlists(instance, token, file="export.json"):
    with open(file, "r") as f:
        data = load(f)
    session = Session()
    session.headers.update({"Authorization": token})
    for x in data:
        print(f"Creating {x}")
        playlistId = (
            session.post(f"{instance}/user/playlists/create", json={"name": x})
            .json()
            .get("playlistId")
        )
        for y in data.get(x):
            session.post(
                f"{instance}/user/playlists/add",
                json={"videoId": y.split("=")[-1], "playlistId": playlistId},
            )
