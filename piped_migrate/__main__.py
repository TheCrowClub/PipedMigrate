from piped_migrate import get_playlists, save_playlists, get_token


def main():
    jtype = input("Import or Export?: ")
    if jtype.lower().startswith("e"):
        instance = input("API url of instance: ").strip("/")
        token = get_token(instance, input("Username: "), input("Password: ")).get(
            "token"
        )
        get_playlists(instance, token)
        print("Done!")
        return 1
    else:
        instance = input("API url of instance: ").strip("/")
        token = get_token(instance, input("Username: "), input("Password: ")).get(
            "token"
        )
        save_playlists(instance, token)
        print("Import done!")


if __name__ == "__main__":
    main()
