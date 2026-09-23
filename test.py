run = True

while run:
    try:
        age = int(input("Hur gammal är du?"))
        if age < 120 and age > 0:
          print("Du har en vanlig ålder!")
          run = False
        else:
            print("Du har en ovanlig ålder!")
            run = False
    except:
        print("Du måste använda heltal.")

print("Hejdå!")
    



