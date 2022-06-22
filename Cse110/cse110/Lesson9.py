
trys = int(0)
print("Guess the word: The knights of the  _ _ _ _ _ table.")
right = 0 
gotit = 0
word = ['r','o','u','n','d']
tris = ['-','-','-','-','-']
print(*tris)

while right == 0 :
    guess = input("Your guess:")
    lista = list(guess.lower())
    for x in lista:
        if "round".count(x)!= -1 and tris["round".find(f'{x.lower()}')] != word["round".find(f'{x.lower()}')]:
            tris["round".find(f'{x.lower()}')] = word["round".find(f'{x.lower()}')]
            gotit +=1 
            print(*tris)
            if gotit == 5:
                right +=1 
            else:
                trys +=1                
print(f"You won in {trys} tries.")

