import turtle
turtle.setup(1200, 600)
prozor = turtle.Screen()
prozor.title("Hangman.")
turtle.bgpic("slika.gif")
strelica = turtle.getturtle()
strelica.penup()
turtle.hideturtle()
turtle.setposition(-50, 300)
turtle.write("Hangman", align="left", font=("Arial", 30))
turtle.setposition(100, 200)
turtle.write("Dobrodošli!", align="left", font=("Arial", 15))
turtle.setposition(100, 180)
turtle.write("Ovo je igrica Hangman.Odaberi slovo i pogodi riječ.", font=("Arial", 15))
turtle.setposition(100, 160)
turtle.write("Sretno! :)", font=("Arial", 15))


import random

rijec_iz_liste = "false"

Rijeci = ["telefon", "majmun", "tigar", "medvjed", "vjeverica", "gepard",
 "laptop", "torba", "slika", "farmaceut", "cvijet", "zeko", "kalendar",
 "radijator", "zgrada", "priroda", "odmor", "planina", "dukserica", "garderoba",
 "klavir", "orkestar", "doktor", "fakultet", "automobil", "helikopter", "diploma"]

duzinaRijeci = len(Rijeci)
pozicija_rijeci = random.randint(0, duzinaRijeci)
rijec_za_pogadjanje = (Rijeci[pozicija_rijeci])
D = len(rijec_za_pogadjanje)

A = ""   # A je crtica
for i in rijec_za_pogadjanje:
    A = A + "_ "
turtle.setposition(100, 0)
turtle.write(A, font=70)


# Funkcija za unos slova
def unos_slova():
#Kreiramo varijablu za unos slova
    slovo = ""
    slovo = turtle.textinput("Hangman", "Unesite slovo ili riječ")
    return slovo


# Funkcija za provjeru unesenog slova
def provjera_slova(A):
    global greska
    global netacno
    turtle.clear()
    if len(slovo) > 1:
        if slovo == rijec_za_pogadjanje:
            return slovo
        else:
            greska += 1
            netacno.append(slovo)
            return A
    else:
        if slovo in rijec_za_pogadjanje:
            turtle.setposition(100, -60)
            turtle.write("Izabrana riječ sadrži: ", font=15)
            turtle.setposition(250, -60)
            turtle.write(slovo, font=15)
            A_temp = ""
            count = 0
            for i in rijec_za_pogadjanje:
                if i == slovo:
                    A_temp = A_temp + i + " "
                else:
                    A_temp += A[count * 2] + " "
                count = count + 1
            return A_temp
        else:
            turtle.setposition(100, -80)
            turtle.write("Izabrana riječ ne sadrži: ", font=15)
            turtle.setposition(280, -80)
            turtle.write(slovo, font=15)
            greska += 1
            netacno.append(slovo)
            return A


greska = 0
netacno = []
kraj = "false"
while kraj == "false":
    slovo = unos_slova()
    A = provjera_slova(A)
    turtle.setposition(100, 0)
    turtle.write(A, font=15)
    turtle.setposition(100, -120)
    turtle.write("Preostali pokušaji: ", font=15)
    turtle.setposition(100, -140)
    turtle.write(9 - greska, font=15)
    turtle.setposition(100, -160)
    turtle.write("Pogrešni pokušaji: ", font=15)
    turtle.setposition(100, -180)
    turtle.write(netacno, font=15)
    if not "_" in A:
        rijec_iz_liste == "true"
        turtle.setposition(-50, 0)
        turtle.write("Bravo!", font=("Arial", 70))
        ponovo = turtle.textinput("Hangman", "Da li želite igrati ponovo? (DA ili NE)")
        if ponovo == "NE":
            kraj = "true"
        else:
            duzinaRijeci = len(Rijeci)
            pozicija_rijeci = random.randint(0, duzinaRijeci)
            rijec_za_pogadjanje = (Rijeci[pozicija_rijeci])
            D = len(rijec_za_pogadjanje)
            A = ""   # A je crtica
            for i in rijec_za_pogadjanje:
                A = A + "_ "
            turtle.setposition(100, 0)
            turtle.write(A, font=70)
    if greska == 1:
        turtle.bgpic("slika2.gif")
    if greska == 2:
        turtle.bgpic("slika3.gif")
    if greska == 3:
        turtle.bgpic("slika4.gif")
    if greska == 4:
        turtle.bgpic("slika5.gif")
    if greska == 5:
        turtle.bgpic("slika6.gif")
    if greska == 6:
        turtle.bgpic("slika7.gif")
    if greska == 7:
        turtle.bgpic("slika8.gif")
    if greska == 8:
        turtle.bgpic("slika9.gif")
    if greska == 9:
        turtle.bgpic("slika10.gif")
        turtle.penup()
        turtle.setposition(-50, 100)
        turtle.pendown()
        turtle.write("Izgubili ste!", font=("Arial", 70))


turtle.exitonclick()