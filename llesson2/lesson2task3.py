import random

nom = ["bobo","Abdu","Marim","Loiq"]
fimilia = ["Kartoshkaev", "Abdumanapovich", "kartoshkaev","Ser"]
email = ["@gmail.com", "@outlook.com", "@yahoo.com", "@mail.ru"]

nom1 = random.choice(nom)
fimilia1 = random.choice(fimilia)
email1 = random.choice(email)
tellphon_number = random.randrange(1000000 , 9999999)
print(f"User->{nom1} {fimilia1} ")
print(f"email is-> {nom1}{fimilia1}{email1}")
print("Number ->+992 92",tellphon_number)