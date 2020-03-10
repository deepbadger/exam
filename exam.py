def quadraticEquation(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        print("Нет действительных корней")
        return
    if d == 0:
        x1 = (-b + (d ** 0.5)) / (2 * a)
        print(x1)
        return
    if d > 0:
        x1 = (-b + (d ** 0.5)) / (2 * a)
        x2 = (-b - (d ** 0.5)) / (2 * a)
        print(x1, x2)
        return


def main():
    print("Введите коэффициенты для квадратного уравнения:")
    while True:
        str = input("a b c = ")
        s = str.split()
        if len(s) == 3:
            try:
                a = float(s[0])
                b = float(s[1])
                c = float(s[2])
                break
            except ValueError:
                print("Это не число!")
                continue
        print("недостаточно аргументов")


    quadraticEquation(a, b, c)

if __name__ == '__main__':
    main()
