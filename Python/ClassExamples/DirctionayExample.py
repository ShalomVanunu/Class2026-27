

# list = []
# Tuple = ()
# Dictionary = {}


Dictionary_Class = { "Students" : ['Shalom',"Alin",'Talya'] , "Ages" : [ 23,45,67,89]  }
harry_potter_movie = {"title":"Harry Poter","year":1987,"cast":['jhone','Eric']}

print(harry_potter_movie["title"])
harry_potter_movie["viewers"] = 9000000
harry_potter_movie["year"] = 1981
harry_potter_movie["cast"].append("Shalom")
print(harry_potter_movie)


print(harry_potter_movie.keys())
for key in harry_potter_movie.keys():
    print(key)

print(harry_potter_movie.values())


