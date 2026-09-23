import random
hero_name = input("Vad heter karaktären? ")
hero_age = int(input("Hur gammal är karaktären?"))
print("Denna karaktär heter", hero_name)
print("Denna karaktären är", hero_age, "år gammal.")

gold = int(input("Hur mycket guld har hjälten?"))
print("Hjälten kommer fram till en affär där man kan köpa ett svärd.")
print(f"Svärdet kostar 7 guld och åldersgränsen är 18 år.")
if gold >= 7 and hero_age >= 18:
    print("Du får köpa svärdet.")
elif gold <= 7:
  print("Du har för lite guld för att köpa svärdet.")
else:
  print("Du är för ung för att köpa svärdet.")
 
hero_strenght = int(input("Hur stark är hjälten? (1-10):"))
hero_health = 10
troll_strenght = 2
troll_health = 10
print(hero_name, "har kommit till en bro.")
print("På bron står ett stort monster.")
has_sword = input("Har hjälten ett svärd? (ja/nej): ")
if hero_strenght >= troll_strenght and has_sword == "ja":
   print("Trollet ser nervös ut.")
else:
  print("Trollet skrattar och drar upp sin klubba.")
damage = random.randint(1, 6)
while hero_health > 0 and troll_health > 0:
  print("Hjälten har", hero_health, "hälsa kvar.")
  print("Trollet har", troll_health, "hälsa kvar.")
  choise = input("Vill du attackera? (ja/nej)")
  if choise == "ja":
   print("Hjälten attackerar!")
   print("Attacken gjorde", hero_strenght, "skada.")
   troll_health = troll_health - hero_strenght
   print("Trollet attackerar tillbaka!")
   print("Attacken gjorde", damage, "skada.")
   hero_health = hero_health - damage
  else:
    print("Hjälten flyr därifrån.")
    break
    
if troll_health <= 0:
  print("Du vann mot trollet.")
  
if hero_health <= 0 and troll_health > 1:
  print("Trollet vann mot hjälten.")
  
print("När du vann mot trollet så hittade du en nyckel som låg i hans ficka och ett äpple.")

if gold >= 7 and hero_age >= 18:
 inventory = ["svärd", "äpple", "nyckel"]
else:
  inventory = ["äpple", "nyckel"]


print("Hjälten har nu: ")
for item in inventory:
  print("-", item)
def show_warning(name):
  print(name, "ser något rör sig i mörkret...")
  print(name, "hör fotsteg..")
show_warning(hero_name)
event = random.randint(1, 3)
if event == 1:
  print("Det var bara en mus som rörde sig.")
elif event == 2:
  print("Det var en fladdermus som satt i mörkret.")
else:
  print("Det var ett spöke!")
  choise == ("Vill du slåss mot spöket? (ja/nej): ")
  if choise == "ja":
    print("Hjälten tar upp sitt svärd och med ett slag så besegrar hjälten spöket!")
    print("Spöket gav dig 10 guld mynt.")
  else:
    print("Hjälten sprang därifrån.")

print("Utomhus så hittar du en skattkista som du öppnar.")
skatt = ["tröja", "kniv", "trollstav"]
skattkista = random.choice(skatt)
print("I skattkistan finns det en", skattkista,".")