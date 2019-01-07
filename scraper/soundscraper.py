from selenium import webdriver
import requests
import bs4
import os

top_url = "https://soundcloud.com/charts/top"
new_url = "https://soundcloud.com/charts/new"
track_url = "https://soundcloud.com/search/sounds?q="
artist_url = "https://soundcloud.com/search/people?q="
mix_url_end = "&filter.duration=epic"

browser = webdriver.Chrome('/Users/Asus/Downloads/Compressed/chromedriver')
browser.get("https://soundcloud.com")

print()
print(">>> Welcome to the Python Soundcloud Scraper")
print(">>> Explore the Top / New & Hot Charts for all Genres")
print(">>> Search Soundcloud for Tracks, Artist, and Mixes")
print()

while True:
    print(">>> Menu")
    print(">>> 1 - Search for a track")
    print(">>> 2 - Search for an artist")
    print(">>> 3 - Search for a mix")
    print(">>> 4 - Top charts")
    print(">>> 5 - New & hot charts")
    print(">>> 0 - Exit")
    print()
    choice = int(input(">>> Your choice: "))
    if choice == 0:
        browser.quit()
        break
    print()

    if choice == 1:
        name = input("Name of the track: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name)
        continue


    if choice == 2:
        name = input("Name of the artist: ")
        print()
        "%20".join(name.split(" "))
        browser.get(artist_url + name)
        continue

    if choice == 3:
        name = input("Name of the mix: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name + mix_url_end)
        continue
