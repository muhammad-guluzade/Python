# revision_number is the number of times python code accessed
# some playlist. When you create a new playlist, its revision
# number is set 1, and for each added track, your revision number
# increases by 1
# In PythonPlaylist used in this code, the revision number is 26,
# which is stored in the txt file in this project

from yandex_music import Client
import requests
from bs4 import BeautifulSoup

# scraping data from billboard

response = requests.get(url="https://www.billboard.com/charts/hot-100/2016-03-05/")
soup = BeautifulSoup(response.text, "html.parser")

tracks_to_save = [title.find(id="title-of-a-story").getText().strip() for title in soup.find_all(class_="lrv-u-width-100p")
                  if title.find(id="title-of-a-story") is not None]

with open("revision_number.txt") as file:
    REVISION = int(file.read())

USER_ID = "AQAAAABxs7LmG5kufsQvB9h4VGAE"
USER_ID_2 = "qswcrwdsfwecm"
PLAYLIST_ID = None


client = Client(USER_ID)
client.init()
000
# creating the playlist

# client.users_playlists_create(title="PythonPlaylist",
#                               user_id=USER_ID)

# finding the playlist with name "PythonPlaylist"
for item in client.users_playlists_list(user_id=USER_ID):
    if item['title'] == "PythonPlaylist":
        PLAYLIST_ID = item['kind']

for track in tracks_to_save:
    results = client.search(text=track,
                            nocorrect=False,
                            type_="all",
                            page=0,
                            playlist_in_best=False)

    try:
        track_id = results["best"]["result"]["id"]
    except:
        continue
    try:
        album_id = results["best"]["result"]["albums"][0]["id"]
    except:
        continue

    client.users_playlists_insert_track(kind=PLAYLIST_ID,
                                        track_id=track_id,
                                        album_id=album_id,
                                        user_id=USER_ID_2,
                                        revision=REVISION)
    REVISION += 1
    print(REVISION)

with open("revision_number.txt", "w") as file:
    file.write(f"{REVISION}")
