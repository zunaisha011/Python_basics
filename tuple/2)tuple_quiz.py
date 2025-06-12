#Find the length of the tuple, genres_tuple
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco")
print(len(genres_tuple))

#Access the element, with respect to index 3
print(genres_tuple[3])

#Use slicing to obtain indexes 3, 4 and 5
print(genres_tuple[3:6])

#Find the first two elements of the tuple genres_tuple
print(genres_tuple[0:2])

#Find the index of 's' in "disco"
print('disco'.find('s'))

#Generate a sorted List from the Tuple C_tuple=(-5, 1, -3)
C_tuple=(-5, 1, -3)
print(sorted(C_tuple))