fav_movies = ["Avatar","Definitely,Maybe","Jurassic Park"]

for x in fav_movies:
    print(x)

new = [x for x in fav_movies]
print(new)
# list comprehension


for x  in range(1,40):
    if x % 2 == 0:
        print(x)
