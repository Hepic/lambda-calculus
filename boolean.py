_true = lambda x: lambda y: x
_false = lambda x: lambda y: y
_if_else = lambda b: lambda op1: lambda op2: b(op1)(op2)
_and = lambda b1: lambda b2: b1(b2)(_false)
_or = lambda b1: lambda b2: b1(_true)(b2)
_not = lambda b: b(_false)(_true)
_xor = lambda b1: lambda b2: b1(_not(b2))(b2)
_is_zero = lambda n: n(lambda x:_false)(_true) 
