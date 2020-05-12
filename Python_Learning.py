pop = []
jpop = []

def collect_songs():
    song = "曲名を入力してください:"
    ask = "pかjのどちらかを入力してください。qで終わります。"

    while True:
        genre = input(ask)

        if genre == "q":
            break

        if genre == "p":
            pop.append(input(song))

        elif genre == "j":
            jpop.append(input(song))

        else:
            print("不正な値です")

    print("pop songs:", pop)
    print("jpop songs:", jpop)

collect_songs()