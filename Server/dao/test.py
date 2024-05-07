from MusicDAO import MusicDAO
class test:
    dao = MusicDAO()
    for r in dao.search_music_by_name("F"):
        print(r[0], "\t", r[1])