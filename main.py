




def main():
    print("Welcome to the Calculus Calculator")
    print("You can choose between:")
    print("1. Calculus 1")
    print("2. Calculus 2")
    print("3. Calculus 3")
    choice = input("Enter Your Decision: ")
    if choice == 1:
        calculus1()
    if choice == 2:
        calculus2()
    else:   
        calculus3()

def calculus1():
    print("Calculus 1")

def calculus2():
    print("Calculus 2")

def calculus3():
    print("Calculus 3")
    print("1. Dot Product")
    print("2. Cross Product")
    print("3. Unit Vector")
    print("4. Projection")
    print("5. Composition") 
    print("6. Distance between point and plane")
    print("7. Curvature")
    choice = input("Enter your Decision: ")
    if choice == 1:
        calculus1()
    if choice == 2:
        calculus2()
    if choice == 3:
        calculus1()
    if choice == 4:
        calculus2()
    if choice == 5:
        calculus1()
    if choice == 6:
        calculus2()
    if choice == 7:
        calculus1()

main()