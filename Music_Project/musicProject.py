import sqlite3
import time
import random

class Music():

    def __init__(self, name, singer, album, production, duration):
        self.name = name
        self.singer = singer
        self.album = album
        self.production = production
        self.duration = duration

    def __str__(self):
        return "Name: {}\nSinger: {}\nAlbum: {}\nProduction Company: {}\nSong Duration: {}"\
            .format(self.name, self.singer, self.album, self.production, self.duration)

class MusicLibrary():
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = sqlite3.connect("MusicProject.db")
        self.cursor = self.connection.cursor()

        ask = "CREATE TABLE IF NOT EXISTS music_table (name TEXT, singer TEXT, album TEXT, production_company TEXT, song_duration INT)"

        self.cursor.execute(ask)
        self.connection.commit()

    def cut_connection(self):
        self.connection.close()

    def show_table(self):
        ask = "SELECT * FROM music_table"

        self.cursor.execute(ask)

        musics = self.cursor.fetchall()
        if (len(musics) == 0):
            print("There is no music in the library.")
        else:
            for i in musics:
                music = Music(i[0],i[1],i[2],i[3],i[4])
                print(music, "\n")

    def ask_musicName(self, name):

        ask = "SELECT * FROM music_table WHERE name = ?"

        self.cursor.execute(ask, (name,))

        musics = self.cursor.fetchall()

        if (len(musics) == 0):
            print("There is no music like this.")
        else:
            music = Music(musics[0][0], musics[0][1], musics[0][2], musics[0][3], musics[0][4])
            print(music)

    def add_music(self, name, singer, album, production, duration):
        ask = "INSERT INTO music_table VALUES (?,?,?,?,?)"

        self.cursor.execute(ask, (name, singer, album, production, duration))

        self.connection.commit()

    def delete_music(self, name):
        ask = "DELETE FROM music_table WHERE name = ?"

        self.cursor.execute(ask, (name,))

        self.connection.commit()

    def show_singer(self, singer):
        ask = "SELECT * FROM music_table WHERE singer = ?"

        self.cursor.execute(ask, (singer,))

        singers = self.cursor.fetchall()

        if (len(singers) == 0):
            print("This singer has no song in the library.")
        else:
            for i in singers:
                music = Music(i[0], i[1], i[2], i[3], i[4])
                print(music, "\n")

    def sum_duration(self):
        ask = "SELECT * FROM music_table"

        self.cursor.execute(ask)

        musics = self.cursor.fetchall()
        sum = 0
        if (len(musics) == 0):
            print("Total Duration: 0 second")
        else:
            for i in musics:
                sum += i[4]

            print("Total Duration: {} seconds".format(sum))

    def random_open(self):

        ask = "SELECT * FROM music_table"

        self.cursor.execute(ask)

        musics = self.cursor.fetchall()

        num = random.randint(0,len(musics) - 1)

        if (len(musics) == 0):
            print("There is no song in the library.")

        else:
            music = Music(musics[num][0], musics[num][1], musics[num][2], musics[num][3], musics[num][4])
            print("Now playing: ")
            print(music)



