def build_album(artist_name, album_title, tracks=0):
	album = {
		'artist': artist_name, 
		'album': album_title
		}
	if tracks:
		album['tracks'] = tracks
	return album

#Prepare the prompt
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "\nWho's the artist? "

#let the user know how to quit
print("Enter 'quit' at anytime to stop.")

while True:
	title = input(title_prompt)
	if title == 'quit':
		break

	artist = input(artist_prompt)
	if artist == 'quit':
		break

	album = build_album(artist, title)
	print(album)
