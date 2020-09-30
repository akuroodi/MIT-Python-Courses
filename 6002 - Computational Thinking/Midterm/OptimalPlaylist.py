def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    if not songs: return []
    if max_size == 0: return []
    
    currentSpace = 0
    playlist = []
    songs2 = songs.copy()

    # Add first song to your list, IF THERE'S CAPACITY
    if songs2[0][-1] <= max_size:
        playlist.append(songs2[0][0])
        currentSpace += songs2[0][-1]
        songs2.pop(0)                   # remove first song from your list
    else: return []
    
    # Sort the remaining songs based on smallest disk space
    sortedSongs = sorted(songs2, key=sorter)

    # Keep addings songs in ascending size as long as it fits
    for song in sortedSongs:
        if (currentSpace + song[-1]) <= max_size:
            playlist.append(song[0])
            currentSpace += song[-1]

    return playlist

def sorter(song):
    return song[-1]





songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]

print(song_playlist(songs, 11))