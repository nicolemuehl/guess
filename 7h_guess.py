secret = 13

guess = int(raw_input("Errate die Zahl: "))

if guess == secret:
    print "Super, du hast die Zahl erraten!"
elif guess != secret:
    print "Leider nicht, versuchs noch mal!"
else:
    print "Das ist wohl keine Zahl..."
    # Hilfe, ich will folgendes: wenn die Eingabe keine Zahl ist, dann schreib....


