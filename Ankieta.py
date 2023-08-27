print("Witam, zapraszam cie do quizu o Ksawerym! UWAGA! Jak odpowiesz zle to wywali cie z programu!")

granie = input("Czy chcesz grac? odpowiedz tak lub nie ")
if granie ==  "tak":
    print("No to zaczynajmy!")
else:
    print("No to szkoda...")
    quit()
odpowiedz = input("Ktory sport lubi Ksawery najbardziej? ")
if odpowiedz == "koszykowka":
    print("Bardzo dobrze!")
else:
    print("Nie prawda! Zaczynaj od nowa!")
    quit()

odpowiedz = input("Czy Ksawery woli Audi czy bmw? ")
if odpowiedz == "bmw":
    print("Bardzo dobrze! znasz ksawerego 25%!")
else:
    print("Nie prawda, lecisz od nowa!")
    quit()

print("UWAGA! Ciezkie pytanie!")
odpowiedz = input("Jaki energetyk lubi Ksawery najbardziej? ")
if odpowiedz == "mango":
    print("Bardzo dobrze, nie duzo osob to wie :>")
else:
    print("Niestety nie udalo ci sie, lecisz od nowa :D")
    quit()

odpowiedz = input("Jak sie nazywa idiotyczny kolega Ksawerego? (z malej litery)  ")
if odpowiedz == "kuba":
    print("Okej, tego sie nie spodziewalem, jest on doslownie idota xD. Znasz Ksawerego 31%")
else:
    print("Niestety nie nazywa sie tak, lecisz od nowa. TIP! Idiotyczny kolega zaczyna na litere K")
    quit()
