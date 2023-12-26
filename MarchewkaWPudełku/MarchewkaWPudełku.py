import random

print("""To jest gra na blefowanie
Kazdy z graczy ma pudelko - jeden z nich ma w srodku marchewke, drugi nie ma nic.
Jeden z graczy zna zawartosc pudelek, drugi nie.
Celem jest doprowadzenie przeciwnika do posiadania pustego pudelka.""")

Player1 = input("Gracz 1 - podaj swoje imie: ")
Player2 = input("Gracz 2 - podaj swoje imie: ")

print(f"""OTO DWA PUDELKA:
 __________        __________
/         /|      /         /|
+--------+ |      +--------+ |
|CZERWONE| |      |ZLOTE   | |
|PUDELKO | /      |PUDELKO | /
+--------+/       +--------+/
{Player1}             {Player2}""")

print(f"""
{Player1}, masz przed soba CZERWONE pudelko.
{Player2}, masz przed soba ZLOTE pudelko.

{Player1} moze zajrzec do swojego pudelka!
Poczekaj az drugi gracz zamknie oczy i otworz swoje pudelko.

Nacisnij Enter by otworzyc pudelko...""")
input()
print()

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print("Masz Marchewke!")
else:
    print("Drugi gracz ma Marchewke!")

input("Nacisnij Enter aby kontynuowac...")
print('\n' * 100)