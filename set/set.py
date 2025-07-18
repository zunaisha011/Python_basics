set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)

# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list) 
print(album_set)

#new()
A = set(["Thriller", "Back in Black", "AC/DC"])
A.add('new')
print(A)

#remove()
A = set(["Thriller", "Back in Black",'new', "AC/DC"])
A.remove('new')
print(A)

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
print(album_set1,album_set2)
intersection = album_set1 & album_set2
print(intersection)
print(album_set1.difference(album_set2))