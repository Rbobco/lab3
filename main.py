from collatz import syracuse_sequence, syracuse_max

def main():
    while True:
        n = int(input("Введите положительное целое число N (0 для выхода): "))
        if  n == 0:
            break
        elif n < 0:
            print ("N должно быть положительным")
            continue
        seq = syracuse_sequence(n)
        max_val = syracuse_sequence(n)
        print("Поселдовательность для" + n + ":" + seq)
        print("Максимум:" + max_val)

main()