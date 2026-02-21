N = int(input("Enter number of songs: "))
playlist = []
found = False
for i in range(N):
    time_period = int(input("Enter song duration " + str(i+1) + ": "))
    if time_period <= 0:
        found = True
    playlist.append(time_period)
if found:
    category = "Invalid Playlist"
    suggestion = "Contains invalid song durations"
else:
    found = False
    for i in playlist:
        if playlist.count(i) > 1:
            found = True
            break
    total_time = sum(playlist)
    if found:
        category = "Repetitive Playlist"
        suggestion = "Add variety songs"
    elif total_time < 300:
        category = "Too Short Playlist"
        suggestion = "Add few more songs"
    elif total_time > 3600:
        category = "Too Long Playlist"
        suggestion = "Reduce the playlist"
    else:
        category = "Balanced Playlist"
        suggestion = "Good listening session"
print("Category:", category)
print("Recommendation:", suggestion)