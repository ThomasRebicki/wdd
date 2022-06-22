stop = int(0) 
things = int(0)
precos = [0]
items = [0]
dump = int(0)
option = 0
nun = int(0)
lista = ['bed','chair','blanket']
pric = [int(100), int(24.99),int(48.50)]
while stop == 0:

    if int(option) == 1:
        add = input("What item would you like to add?")
        if add.lower() in lista:
            things +=1 
            wr = lista.index(add.lower())
            items.append(lista[wr])
            precos.append(pric[wr])
        else: 
            things +=1 
            items.append(add)
            dump = 0
            while dump == 0: 
                price = input(f"What is the price of {items[things]}?")
                if price.isnumeric():
                    precos.append(int(price))
                    dump +=1
                else:
                    print("insert valid price")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXX------------ITEM-ADDED-------------XXXXXXXXXXXXXXXXXXXXXXXXXX")      


    if int(option) == 2:
        if things == 0:
            print("Empty cart")
        else:
            for x in range(things):
              print(f"{x+1}:{items[x+1]} - {precos[x+1]}$")
            for i in range(0, len(precos)):    
                    nun = nun + precos[i];    
            print(f"total cost:{nun}$")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXX------------VIEW-CART--------------XXXXXXXXXXXXXXXXXXXXXXXXXX")

    if int(option) == 3:
        for x in range(things):
            print(f"{x+1}:{items[x+1]} - {precos[x+1]}$")
        caguei = input("What item would you like to remove?")
        if int(caguei) <= things:
            items.remove(items[int(caguei)])
            precos.remove(precos[int(caguei)])
            things -=1
        print("XXXXXXXXXXXXXXXXXXXXXXXXXX------------ITEM-REMOVED-------------XXXXXXXXXXXXXXXXXXXXXXXXXX")      


    print("labeled items:")
    for x in range(3):
              print(f"{x}: {lista[x]} - {pric[x]}$")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX")
    option = input("Please enter an action:")
             

    if int(option) == 5:
         print("Bye")
         stop = 3876567890
