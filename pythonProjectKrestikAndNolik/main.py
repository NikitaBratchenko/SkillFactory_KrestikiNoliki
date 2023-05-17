def Hello():
    print(f"   Приветствуем вас")
    print(f"        в игре")
    print(f"   крестики нолики!!!")
    print(f"   Вы будете 'Игрок_1'")
    print(f"------------------------------------------")
    print(f"   Формат ввода данных x y")
    print(f"Вводите данные через пробел")
    print(f"   Пример: 1 0 или 2 1")
    print(f"------------------------------------------")
    print(f"Сделайте выбор:")
    print(f"Если хотите выбрать X или 0 первым")
    print(f"Напишите 'Символ' ")
    print(f"Если хотите сделать ход первым")
    print(f"Напишите 'Ход' ")
    print(f"------------------------------------------")
def ask(Player):
    while True:
        x, y =input("Выберите координаты для хода:").split()
        if (x.isdigit()) and (y.isdigit()):
            x, y=int(x), int(y)
            if x > 2 or x < 0 or y > 2 or y < 0:
                print("Вы вышли за поле!!!")

            else:
                if Arr[x][y] == " ":
                    Arr[x][y] = Player
                    return x, y
                else:
                    print(f"Эти клетка уже занята")
                    x, y = input("Выберите координаты для хода:").split()
        else:
            print("Вам нужно выбрать числа!")
            x, y = input("Выберите координаты для хода:").split()
def show():
    print(f"    | 0 | 1 | 2 |")
    print(f"------------------")
    for i, row in enumerate(Arr):
        Arr_1= f" {i}  | {' | '.join(row)} | "
        print(Arr_1)
        print(f"------------------")
def win():
    index_y = 0
    for index_x in range(0,3):
        if Arr[index_x][0]==Arr[index_x][1]==Arr[index_x][2] or Arr[0][index_x]==Arr[1][index_x]==Arr[2][index_x]:
            if Arr[index_x][index_x]=="X":
                print(f"Победил игрок с символом {Player_1}")
                return 1
            elif Arr[index_x][index_x]=="0":
                print(f"Победил игрок с символом {Player_2}")
                return 1
        elif Arr[0][0]==Arr[1][1]==Arr[2][2]:
            if Arr[0][0]=="X":
                print(f"Победил игрок с символом {Player_1}")
                return 1
            elif Arr[0][0]=="0":
                print(f"Победил игрок с символом {Player_2}")
                return 1
        elif Arr[0][2]==Arr[1][1]==Arr[2][0]:
            if Arr[0][2]=="X":
                print(f"Победил игрок с символом {Player_1}")
                return 1
            elif Arr[0][2]=="0":
                print(f"Победил игрок с символом {Player_2}")
                return 1
Arr = [[" "] * 3 for i in range(3)]
Hello()
Ans=str(input())
if Ans=="Символ":
    Player_1=str(input("Введите 'X' или '0' = "))
    if Player_1=="X":
        move=2
        Player_2="0"
    elif Player_1=="0":
        move=2
        Player_2="X"
    else:
        Player_1 = str, input("Введите 'X' или '0' = ")
elif Ans=="Ход":
    move=1
    Player_2 = str(input(f"Игрок_2 введите 'X' или '0' = "))
    if Player_2=="X":
        Player_1="0"
    elif Player_2=="0":
        Player_1="X"
    else:
        Player_2 = str, input("Введите 'X' или '0'")
count=0
while True:
    show()
    count+=1
    if move%2==0:
        ask(Player_1)
        move+=1
    else:
        ask(Player_2)
        move+=1
    if win():
        break
    if count==9:
        print("Ничья!!!")
        break
