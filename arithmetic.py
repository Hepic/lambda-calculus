_0 = lambda f: lambda x: x    

_succ = lambda n: lambda f: lambda x: f(n(f)(x)) 
_1 = _succ(_0)

_add = lambda n1: lambda n2: n2(_succ)(n1)    
_mult = lambda n1: lambda n2: n2(_add(n1))(_0)
#_exp = lambda n1: lambda n2: n2(n1)
_exp = lambda n1: lambda n2: n2(_mult(n1))(_1)
#pred = lambda n: _0, _1 


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
