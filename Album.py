def build_album(artist_name, album_title, tracks=0):
	album = {
		'artist': artist_name, 
		'album': album_title
		}
	if tracks:
		album['tracks'] = tracks
	return album

album = build_album('kanye west', 'my dark twisted fantasy')
print(album)

album = build_album('childish gambino', 'kaui', tracks=7)
print(album)