def factorization(inp):
    ans = [1]
    prime = 2
    while inp != 1:
        if inp % prime == 0 and ans[-1] != prime:   #jestliže je na posledním místě prime, nezapisuj ho
            if ans == [1]:                          #jednicka nesmí zůstat v rozkladu, jinak by bylo phi 0
                ans.clear()
            ans.append(prime)
            inp = inp / prime
        elif inp % prime == 0:
            inp = inp / prime
        else:
            if prime == 2:      #tento blok říká, že pokud jsme dělili číslem 2,
                prime = 3       #další máme zvolit číslo 3, jinak skáčeme o 2 čísla
            else:               #(nemá smysl testovat sudá čísla)
                prime += 2
    return(ans)

def phi(num, factInp):
    r = num
    for i in range(0, len(factInp)):
        #print(factInp[i])
        r *= (1-(1/factInp[i]))
    return int(r)
            
num = int(input("Vložte číslo, jehož funkci Fí chcete zjistit.\n"))
print(phi(num, factorization(num)))

input()
