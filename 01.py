# Sastādi programmu, kas liek datoram "iedomāties" skaitli starp 1 un 100, bet
# lietotājam ļauj to uzminēt. Pēc katra minējuma programmai jāpaziņo, vai lietotāja
# ievadītais skaitlis ir lielāks, mazāks vai vienāds ar datora "iedomāto" skaitli.
# Kad lietotājs skaitli ir uzminējis, programmai jāpaziņo, ar cik minējumiem lietotājs
# skaitli ir atminējis. Spēles protokolu ierakstīt failā Protokols.txt
# (protokola katrā rindiņā iekļaut: gājiena kārtas numuru, lietotāja ievadīto skaitli
# un norādi, vai tas ir mazāks, lielāks vai vienāds ar datora "izdomāto" skaitli)

import random

random.seed()
skaitlis = random.randint(1, 100)

#print("Random skaitlis šoreiz ir: " +str(skaitlis))

reizes = 0
f = open("Protokols.txt", "a")

while True :
    sk = int(input("Minamais skaitli: "))
    reizes = reizes + 1
    if(sk < skaitlis):
        print(str(sk) + " ir mazāks par minamo skaitli. Mēģini vēlreiz! ")
        f.write(str(reizes) + ". mēģinājums. Ievadīts " + str(sk) + ". Tas ir mazāks par datora " + str(skaitlis))
        f.write("\n")
    if(sk > skaitlis):
        print(str(sk) + " ir lielāks par minamo skaitli. Mēģini vēlreiz! ")
        f.write(str(reizes) + ". mēģinājums. Ievadīts " + str(sk) + ". Tas ir lielaks par datora " + str(skaitlis))
        f.write("\n")
    if(sk == skaitlis):
        print("Apsveicu! Esi uzminējis datora iedomāto skaitli " + str(skaitlis) + " ar veseliem " + str(reizes) + " mēģinājumiem")
        f.write(str(reizes) + ". mēģinājums. Ievadīts " + str(sk) + ". Tas ir vienāds par datora " + str(skaitlis))
        f.write("\n")
        print("Game Over")
        break

f.close()
