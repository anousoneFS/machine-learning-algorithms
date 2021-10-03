ox = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

ox2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = []

def display():
    for id, i in enumerate(ox):
        if id % 3 == 0:
            print()
            print(f"{ox[id]} ", end="")
        else:
            print(f"{ox[id]} ", end="")
    print()


def myinput():
    try:
        o = int(input("shoose your position: "))
    except:
        print("is not digit")
        o = 0
    if o == 10:
        print("program exit")
        exit()
    if 1 <= o <= 9:
        if ox[o - 1] == "-":
            ox[o - 1] = "O"
            display()
        else:
            print("shoose another position")
            display()
    else:
        print("out of range(1-9)")
        display()


if __name__ == "__main__":
    while True:
        myinput()
        for id, i in enumerate(ox):
            if ox[id] == '-':
                x.append(id+1)
                ox[id] = 'x'
                for j in x:
                    if(j in [1, 3, 7, 9]):
                        if(j == 1):
                            if(ox[1] == 'x' and ox[2] == 'x')
                                display()
                                print("computer win")
                                exit()

                        else:
                    
                    elif(j in [2, 4, 6, 8]):

                    elif(j == 5):


