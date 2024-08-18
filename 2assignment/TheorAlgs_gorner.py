import time
n = 169745787500
def main():
    n = int(input("Введіть натуральне число: "))
    if n <= 0:
        print("Число повинно бути натуральним (більше 0).")
        return

    start_time = time.time()

    i = 2
    is_first = True

    while i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1

        if k > 0:
            if not is_first:
                print("*", end="")
            is_first = False
            print(i, end="")
            if k > 1:
                print(f"^{k}", end="")

        i += 1

    print()

    end_time = time.time()
    exec_time = end_time-start_time
    print(f'{exec_time:.6f}')

if __name__ == "__main__":
    main()
