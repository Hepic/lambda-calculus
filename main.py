import arithmetic as ar
import boolean as b

def increase(x):
    return x + 1

def print_number(func):
    return func(increase)(0)

def print_boolean(func):
    return func(True)(False)


def main():
    print print_boolean(b._is_zero(ar._0))

if __name__ == "__main__":
    main()
