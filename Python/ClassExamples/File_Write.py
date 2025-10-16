
Text = """Lose Yourself # Eminem # 2002",
"Without Me # Eminem # 2002",
"Toxic # Britney Spears # 2003",
"Baby One More Time # Britney Spears # 1998",
"Womanizer # Britney Spears # 2008",
"Crazy in Love # Beyonc ft. Jay-Z # 2003",
"Single Ladies (Put a Ring on It) # Beyonc # 2008",
"Irreplaceable # Beyonc # 2006",
"Halo # Beyonc # 2008",
"I Kissed a Girl # Katy Perry # 2008",
"Hot n Cold # Katy Perry # 2008",
"Umbrella # Rihanna ft. Jay-Z # 2007",
"Hey Ya! # Outkast # 2003 """

list_songs = Text.split("\n")


for line in list_songs:
    file_obj = open("songs.txt", "a")  # a append
    file_obj.write(line+"\n")
    file_obj.close()




