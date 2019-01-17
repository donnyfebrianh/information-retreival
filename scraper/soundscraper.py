from selenium import webdriver
import requests
import bs4
import os

top_url = "https://soundcloud.com/charts/top"
new_url = "https://soundcloud.com/charts/new"
track_url = "https://soundcloud.com/search/sounds?q="
artist_url = "https://soundcloud.com/search/people?q="
mix_url_end = "&filter.duration=epic"

browser = webdriver.Chrome('D:\chromedriver')
browser.get("https://soundcloud.com/discover")

while True:
    print(">>> Menu")
    print(">>> 1 - Mencari lagu")
    print(">>> 2 - Mencari artis")
    print(">>> 3 - Mencari lagu mix")
    print(">>> 4 - Terpopuler")
    print(">>> 5 - Lagu baru dan terpopuler")
    print(">>> 0 - Exit")
    print()
    choice = int(input(">>> Pilihanmu: "))
    if choice == 0:
        browser.quit()
        break
    print()

    if choice == 1:
        name = input("Nama lagu: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name)
        continue


    if choice == 2:
        name = input("Name artis: ")
        print()
        "%20".join(name.split(" "))
        browser.get(artist_url + name)
        continue

    if choice == 3:
        name = input("Nama lagu mix: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name + mix_url_end)
        continue
while True:
        print(">>> Genre yang tersedia:")
        print()

        # genre menu
        url = ''
        if choice == 4: url = top_url
        else: url = new_url

        # parse html dengan beautiful soup
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        # print request.text
        
        genres = soup.select("a[href*=genre]")[2:]
        # print genre

        genre_links = []

        # print semua genre yang tersedia
        for index, genre in enumerate(genres):
            print(str(index) + ": " + genre.text)
            genre_links.append(genre.get("href"))

        print()
        choice = input(">>> Pilihanmu (tekan x untuk kembali): ")
        print()

        if choice == 'x': break
        else: choice = int(choice)

        # print(genre_links[pilihan])

        url = "http://soundcloud.com" + genre_links[choice]
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")

        tracks = soup.select("h2")[3:]
        track_links = []
        track_names = []
        # print(lagu)

        for index, track in enumerate(tracks):
            track_links.append(track.a.get("href"))
            track_names.append(track.text)
            print(str(index+1) + ": " + track.text)
            print()

        # song selection loop
        while True:
            choice = input(">>> Pilihanmu (tekan x untuk kembali): ")
            print()

            if choice == 'x': break
            else: choice = int(choice)-1

            print("Memutar: " + track_names[choice])
            print()

            browser.get("http://soundcloud.com" + track_links[choice])

print()
print("Byebye")
print()
