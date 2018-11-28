#*Hits sick dab*

val = 0
steam_önske_lista = ""

while val != 3:
    print("Välkomen till loggboken.\n 1.Öppna loggen.\n 2.Skriv i loggen.\n 3.Avsluta loggen.\n 4.Rensa.")

    val = int(input())

    if val == 1: 
        f = open('ligma.txt', 'r') 
        for line in f: 
            print(line)
        f.close()

    elif val == 2:
        f = open('ligma.txt', 'a+') 
        steam_önske_lista = input("Skriv in en ny rad: ")
        f.write("\n" + steam_önske_lista)
        f.close()

    else: 
        print("bye!")
