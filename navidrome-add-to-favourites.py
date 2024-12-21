import json
import utility
import navidrome

# File input
NOT_FOUND_FILE = "compare_report/songs_not_found.json"

def main():
    # Carica i dati
    not_found_songs = utility.load_json_data(NOT_FOUND_FILE)

    # Autenticazione a Navidrome
    session = navidrome.authenticate()

    # Cerca e aggiorna i preferiti
    for song in not_found_songs:
        spotify_artist = utility.clean_string(song["artists"][0]["name"])
        spotify_album = utility.clean_string(song["album"])
        spotify_title = utility.clean_string(song["name"])
        
        # Cerca il brano esatto su Navidrome
        matches = navidrome.search_song(session, spotify_artist, spotify_album, spotify_title)

        if matches:
            print(f"Trovati {len(matches)} brani per {spotify_title} - {spotify_artist} ({spotify_album}).")
            navidrome.add_to_favorites(session, matches)
        else:
            print(f"Nessun brano trovato per {spotify_title} - {spotify_artist} ({spotify_album}).")

if __name__ == "__main__":
    main()
