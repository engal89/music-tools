import navidrome
import json
import utility

PLAYLIST_NAME = "Brani preferiti"

def get_playlist_by_name(session, playlists, name):
    """Trova una playlist per nome."""
    for playlist in playlists:
        if playlist["name"] == name:
            return playlist
    raise ValueError(f"Playlist '{name}' non trovata.")

def main():
    # Autenticazione
    session = navidrome.authenticate()

    try:
        # Recupera tutte le playlist
        navidrome_playlists = navidrome.get_playlists(session)
        requested_playlist = get_playlist_by_name(session, navidrome_playlists, PLAYLIST_NAME)
        print(f"Trovata playlist: {requested_playlist['name']} (ID: {requested_playlist['id']})")

        # Recupera i brani della playlist
        entries = navidrome.get_playlist_songs(session, requested_playlist["id"])
        print(f"{len(entries)} brani trovati nella playlist.")

        # Salva i dati su file
        utility.save_to_json_file(entries, PLAYLIST_NAME+".json", "navidrome-playlists")

    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    main()
