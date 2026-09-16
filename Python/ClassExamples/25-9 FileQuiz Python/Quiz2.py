SONGS_LIST =  [
    "Lose Yourself # Eminem # 2002",
    "Without Me # Eminem # 2002",
    "Toxic # Britney Spears # 2003",
    "Baby One More Time # Britney Spears # 1998",
    "Womanizer # Britney Spears # 2008",
    "Crazy in Love # Beyoncé ft. Jay-Z # 2003",
    "Single Ladies (Put a Ring on It) # Beyoncé # 2008",
    "Irreplaceable # Beyoncé # 2006",
    "Halo # Beyoncé # 2008",
    "I Kissed a Girl # Katy Perry # 2008",
    "Hot n Cold # Katy Perry # 2008",
    "Umbrella # Rihanna ft. Jay-Z # 2007",
    "Hey Ya! # Outkast # 2003"]
def years(songs):
    list_of_years=[]
    for song in songs:
        list_of_years.append(song.split("#")[2])



    return list_of_years

print(years(SONGS_LIST))