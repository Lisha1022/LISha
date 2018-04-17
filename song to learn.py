
name_of_songs = []
artists = []
year_of_songs = []
learned = []

MENU = """
    L - List songs
    A - Add new song
    C - Complete a song
    Q - Quit"""



def main():
    print("Songs To Learn 1.0 - by LiSha")
    song_load()
    load_count = len(open("songs.csv").readlines())
    print("{} songs loaded".format(load_count))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "A":
            add_new_song()
        elif choice == "L":
            list_all_songs()
        elif choice == "C":
            complete_a_song()
        else:
            print("select a valid menu")
        print(MENU)
        choice = input(">>> ").upper()
    save_songs()
    save_count = len(open("songs.csv").readlines())
    print("{} songs saved to the songs.csv".format(save_count))



def song_load():
    load_file = open("songs.csv", 'r')
    for each_song in load_file:
        store_song = each_song.split(',')
        name_of_songs.append(store_song[0])
        artists.append(store_song[1])
        year_of_songs.append(int(store_song[2]))
        store_song[3] = store_song[3].strip('\n')
        if store_song[3] == "y":
            store_song[3] = " "
        if store_song[3] == "n":
            store_song[3] = "*"
        learned.append(store_song[3])
    load_file.close()



def list_all_songs():
    for i in range(0, len(name_of_songs)):
        print("{0}. {1} {2:30} - {3:30} ({4})".format(i, learned[i], name_of_songs[i], artists[i], year_of_songs[i]))
    print("\n {} songs learned, {} songs still to learn".format(learned.count(" "), learned.count("*")))



def save_songs():
    save_file = open("songs.csv", 'w')
    for i in range(0, len(name_of_songs)):
        learned_save_song = learned[i]
        if learned_save_song == " ":
            learned_save_song = "y"
        if learned_save_song == "*":
            learned_save_song = "n"
        print("{},{},{},{}".format(name_of_songs[i], artists[i], year_of_songs[i], learned_save_song), file=save_file)

    save_file.close()



def add_new_song():
    song_name_title = input("Title: ")
    while song_name_title.isspace() or song_name_title == "":
        print("Not valid it cant be empty")
        song_name_title = input("Title: ")

    song_name_artist = input("Artist: ")
    while song_name_artist.isspace() or song_name_artist == "":
        print("Invalid. Cannot be empty")
        song_name_artist = input("Artist: ")

    try:
        song_name_year = int(input("Year: "))
        if 1000 <= song_name_year <= 9999:
            not_learned = "*"
            name_of_songs.append(song_name_title)
            artists.append(song_name_artist)
            year_of_songs.append(song_name_year)
            learned.append(not_learned)
            print("{} by {} ({}) added to song list".format(song_name_title, song_name_artist, song_name_year))
        else:
            print("Number must be >= 1000")
    except ValueError:
        print("Give the valid entry")



def complete_a_song():
    try:
        choice_of_song = int(input("Enter songs to be marked as learnt: "))
        try:
            if learned[choice_of_song] == "*":
                learned[choice_of_song] = " "
                print("{} by {} learned".format(name_of_songs[choice_of_song], artists[choice_of_song]))
            elif learned[choice_of_song] == " ":
                print("Song has already been learned")
        except IndexError:
            print("Could'nt find the song ")
    except ValueError:
        print("enter the valid input")


if __name__ == '__main__':
    main()