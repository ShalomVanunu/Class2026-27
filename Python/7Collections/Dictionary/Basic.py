
harry_potter_movie = {"title":"Harry Poter","year":1987,"cast":['jhone','Eric']}
print(harry_potter_movie.keys())
print(harry_potter_movie.values())
print(harry_potter_movie["title"])
harry_potter_movie["teacher"] = "shalom"

list_keys = []
for key in harry_potter_movie.keys():
    list_keys.append(key)
print(list_keys)
print("#".join(list_keys))

