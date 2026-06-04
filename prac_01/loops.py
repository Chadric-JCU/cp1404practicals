for i in range(1, 21, 2):
    print(i, end=' ')
print()

#counting in 10s

for i in range(0, 101, 10):
    print(i, end=" ")
print()

#counting down from 20

for i in range(20, 0, -1):
    print(i, end=" ")
print()

#printing stars in a line

number_of_stars =  int(input("Enter number of stars: "))
for number in range(number_of_stars):
    print("*", end="")
print()


#print lines of increasing stars

number_of_stars =  int(input("Enter number of stars: "))
for number in range(1, number_of_stars + 1):
    print(number * "*")
print()

