import arithmetic as ar
import boolean as bl
import pair as pr

def increase(x):
    return x + 1

def print_number(func):
    print func(increase)(0)

def print_boolean(func):
    print func(True)(False)

def main():
    num = ar._sub(ar._3)(ar._5)
    print_number(num)

if __name__ == "__main__":
    main()
