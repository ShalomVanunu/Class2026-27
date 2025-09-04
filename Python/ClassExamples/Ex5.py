

with open("email-sample-html.html","r", encoding='utf-8') as HTMLfile:
    HTMLfile_content = HTMLfile.readlines()

HTMLfile_new = open("email-sample-html-new.html", "a")

for line in HTMLfile_content:
    new_line = line.replace("@","at")
    HTMLfile_new.write(new_line)

