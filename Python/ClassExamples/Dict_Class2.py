
MOVIES_DICT = {"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"],"Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}


def info_movie_write(True_False,Dict):
    if True_False == False: # not Sorted
        for key in Dict.items():
            movie= key[0]
            actor= key[1]
            print(movie,":",",".join(actor))
    else:#  Sorted
        for key in Dict.items():
            movie= key[0]
            actor= sorted(key[1])
            print(movie,":",",".join(actor))




info_movie_write(True,MOVIES_DICT)