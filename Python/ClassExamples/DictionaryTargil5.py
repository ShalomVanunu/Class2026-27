
movies = {"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"],
  "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}


def write_movie_info(Tr_Fa,movies ):

    if Tr_Fa:
        for value in movies.items():
            print(value[0]+":"+" ".join(sorted(value[1])))
    else:
        for value in movies.items():
            print(value)
            print(value[0]+":"+" ".join(value[1]))

Tr_Fa = False
write_movie_info(Tr_Fa,movies )