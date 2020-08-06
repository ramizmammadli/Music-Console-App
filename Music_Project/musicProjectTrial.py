from problem2.musicProject import *

print("""

Welcome to Music Application:

1. Show all the musics
2. Add Music
3. Delete Music
4. Search Music
5. Search Singer
6. Show total Duration
7. Play music Randomly

Press 'q' to quit
""")

library = MusicLibrary()

while True:
    op = input("\nEnter the operation: ")

    if (op == "q"):
        print("Program is being ended...")
        time.sleep(1.5)
        print("Program finished successfully. Have a good day!")
        break

    elif( op == "1"):

        print("Processing...")
        time.sleep(1)
        print("\n")
        library.show_table()

    elif(op == "2"):

        name = input("Name: ")
        singer = input("Singer: ")
        album = input("Album: ")
        production = input("Production company: ")
        duration = input("Duration (secs): ")

        print("Processing...")
        time.sleep(1)
        library.add_music(name, singer, album, production, duration)
        print("Music is added successfully.")

    elif ( op == "3"):

        name = input("Enter the name of music to delete: ")

        print("Processing...")
        time.sleep(1)
        library.delete_music(name)
        print("Music is deleted successfully.")

    elif(op == "4"):

        name = input("Enter the music name to search: ")
        print("Processing...")
        time.sleep(1)
        print("\n")
        library.ask_musicName(name)

    elif (op == "5"):

        singer = input("Enter the singer name to see his(her) musics: ")

        print("Processing...")
        time.sleep(1)
        print("\n")
        library.show_singer(singer)

    elif( op == "6"):

        print("Processing...")
        time.sleep(1)
        print("\n")
        library.sum_duration()
    elif (op == "7"):

        print("Processing...")
        time.sleep(1)
        print("\n")
        library.random_open()
    else:
        print("Invalid operation. ")