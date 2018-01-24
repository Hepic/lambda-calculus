import pair as pr

_0 = lambda f: lambda x: x 

_succ = lambda n: lambda f: lambda x: f(n(f)(x)) 
_1 = _succ(_0)

_add = lambda n1: lambda n2: n2(_succ)(n1)    
_mult = lambda n1: lambda n2: n2(_add(n1))(_0)
_exp = lambda n1: lambda n2: n2(_mult(n1))(_1) # alternative -> _exp = lambda n1: lambda n2: n2(n1)
_pred_pair = lambda x: pr._pair(x(pr._sec))(_succ(x(pr._sec)))
_pred = lambda n: n(_pred_pair)(pr._pair(_0)(_0))(pr._fir)
_sub = lambda n1: lambda n2: n2(_pred)(n1)
_sum = lambda n: n(pr._sum_pair)(pr._pair(_1)(_0))(pr._sec)
_factorial = lambda n: n(pr._mult_pair)(pr._pair(_1)(_1))(pr._sec)
_nth_fibo = lambda n: n(pr._fibo_pair)(pr._pair(_1)(_0))(pr._sec)

_2 = _succ(_1)
_3 = _succ(_2)
_4 = _add(_2)(_2)
_5 = _add(_2)(_3)
_6 = _add(_3)(_3)
_7 = _succ(_6)
_8 = _mult(_2)(_4)
_9 = _exp(_3)(_2)
_10 = _mult(_2)(_5)
_30 = _mult(_5)(_6)
_125 = _exp(_5)(_3)
