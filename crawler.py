import requests
from bs4 import BeautifulSoup


def get_artist(url):
    ret = []
    r = requests.get(url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    tracklist = soup.find("table", {"class": "tracklist"})
    links = tracklist.find_all("a")
    for i in links:
        ret.append((i.text, i['href']))
    return ret


def get_songs(artist_url):
    songs = []
    r = requests.get(artist_url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    tracklists = soup.find("table", {"class": "tracklist"})
    links = tracklists.find_all("a")
    for i in links:
        songs.append((i.text, i['href']))
    return songs


def get_lyrics(song_url):
    r = requests.get(song_url)
    soup = BeautifulSoup(r.content, features="html.parser")
    lyrics_div = soup.find("p", {"id": "songLyricsDiv"})
    lyrics = lyrics_div.text
    return lyrics


def crawl():
    artists = get_artist("https://www.songlyrics.com/a/")
    for name, link in artists:
        print(name, "   :   ", link)
        songs = get_songs(link)
        for song, song_link in songs:
            with open("lyric.txt", "a") as d:
                lyrics = get_lyrics(song_link)
                d.write("\n\n\n\n")
                d.write(song)
                d.write("\n\n\n\n")
                d.write(lyrics)


if __name__ == "__main__":
    crawl()
