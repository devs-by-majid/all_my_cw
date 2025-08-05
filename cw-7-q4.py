
class Song:
    def __init__(self, track_name, duration):
        self.track_name = track_name
        self.duration = duration


class PlayList:
    def __init__(self):
        self.song_list = []

    def add_song(self, song):
        self.song_list.append(song)

    def remove_song(self, *song2):
        filtered = list(filter(lambda song: song.track_name !=
                        song2[0] and song.duration!=song2[1], self.song_list))
        return filtered

    def total_duration(self):
        total = sum(song.duration for song in self.song_list)
        return total

    def show_list(self):
        return self.song_list


music1 = Song("music1", "3:20")
music2 = Song("music2", "1:20")
music3 = Song("music3", "2:56")

play_list1 = PlayList()
play_list1.add_song(music1)
play_list1.add_song(music2)
play_list1.add_song(music3)

print(play_list1.show_list())
print(play_list1.remove_song("music1","3:20"))
