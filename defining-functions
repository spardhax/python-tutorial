numbers=input()
print(type(numbers))
numbers="1 2 3 4 5".split()

#split method can only be used for string array
print(numbers)

#the above list of numbers is an array
int(numbers[0])
#turn it into integer

completelist="1 2 3 4 5".split()
#following process is aclled LIST COMPREHENSION
number_completelist=[int(x) for x in completelist]

print(number_completelist)

for i in number_completelist:
    if i==1:
        print("a")
    elif i==2:
        print("b")
    elif i==3:
        print("c")
    else:
        print("inavlid")
        
#dictionary
pokemon={
    1:"a",
    2:"b",
    3:"c"
}

print(pokemon[2])
print(pokemon.get(1))

if pokemon.get(5) is None:
    print("pokemon not found")
else:
    print(pokemon[5])
    
for x in number_completelist:
    if pokemon.get(x) is None:
        print("pokemon not found")
    else:
        print(pokemon[x])
        
pokemon=[("a",200),("b",400),("c",600)]
pokemon[0]

#if written in paranthesis(),it is a tuple
#readonly
t=("A","B","C)")

print(type(t))

def printpokemons(numbers):
    pokemon={
    1:"a",
    2:"b",
    3:"c"
     }
    for i in numbers:
        if pokemon.get(i) is None:
            print("pokemon not found")
        else:
            print(pokemon[i])
    return
    
numbers=[int(x) for x in input().split()]
printpokemons(numbers)
