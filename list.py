fav_movies = ["Avatar","Definitely,Maybe","Jurassic Park"]
print(fav_movies[0:2])
print(len(fav_movies))

fav_movies.append("Transformer")
#adding at ending
print(fav_movies)
print(len(fav_movies))

fav_movies.insert(2,"Transformer")
#insert at indexed value
print(fav_movies)

del(fav_movies[0:3])
del(fav_movies[1])
# for deleting values from list through indexed
print(fav_movies)

fav_num = [0,2,7]
print(fav_num[0])