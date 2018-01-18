def increase(x):
    return x + 1

def print_number(func):
    return func(increase)(0)


def main():
    _0 = lambda f: lambda x: x    
    succ = lambda n: lambda f: lambda x: f(n(f)(x)) 
    _1 = succ(_0)
    _2 = succ(_1)
    _3 = succ(_2)
    add = lambda n1: lambda n2: n2(succ)(n1)    
    mult = lambda n1: lambda n2: n2(add(n1))(_0)
    #exp = lambda n1: lambda n2: n2(n1)
    exp = lambda n1: lambda n2: n2(mult(n1))(_1)
    _5 = add(_2)(_3)
    _6 = add(_3)(_3)
    _125 = exp(_5)(_3)
    _30 = mult(_5)(_6)

    print print_number(_125)


if __name__ == "__main__":
    main()
