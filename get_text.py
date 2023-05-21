with open('longreads.txt', 'r') as file:
    content = file.read()
    c1 = content.split()
    c2 = content.replace("™", "")
    c2 = c2.replace("â", "")
    c2 = c2.replace("€", "")
    print(c2)
    print("USA" in content)



my_words = ""
while(True):
    words = input("What are your thoughts? Enter -1 to exit)")
    if(words=="-1"):
        break
    else:
        my_words += words + "\n"

with open("my_thoughts.txt", "w") as my_file:
    my_file.write(my_words)



