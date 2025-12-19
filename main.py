from collatz import syracuse_sequence, syracuse_max


def main():
    while True:
        n = int(input("Введите положительное целое число N (0 для выхода): "))
        if n == 0:
            break
        elif n < 0:
            print("N должно быть положительным")
            continue
        seq = syracuse_sequence(n)
        max_val = syracuse_max(n)
        print("Поселдовательность для" + str(n) + ":" + str(seq))
        print("Максимум:" + str(max_val))


main()
