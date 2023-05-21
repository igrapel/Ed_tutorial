#first_name = input("Give me your first name: ")
#last_name = input("Give my our last name")
#bday = input("Give me your birthday: Month Day, YYYY")


#automatiically a user name that consists of first three letters of first name
#followed by first and last letter of last name
#Michael Johnson:   MicJN

#Password: last two characters of name and four digit birth year    ig1983
first_name = "Bob"
last_name = "Markinson"
name_length = len(last_name)
#print(first_name[0:3] + last_name[0] + last_name[name_length-1])

def create_user(first, last):
    f = first[0:3]
    last_init = last[0]
    name_length = len(last)
    last_letter = last[name_length-1]
    return (f + last_init + last_letter)

u1 = create_user(first_name, last_name)
print(u1)
bday ="Augst, 12, 1999"
#mj2023
l = len(bday)
y = bday[l-4:]
print(y)


text = "Statistical Modeling, Causal Inference, and Social Science"
first_space = text.index(" ")
first_text = text[0:first_space]
second_text = text[first_space + 2:]
new_text = first_text + " m" + second_text

print(new_text)