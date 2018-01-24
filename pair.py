import boolean as b
import arithmetic as ar

_pair = lambda x: lambda y: lambda f: f(x)(y)
_fir = b._true
_sec = b._false

_sum_pair = lambda x: _pair(ar._succ(x(_fir)))(ar._add(x(_fir))(x(_sec))) # input: pair(a, b). output: pair(a + 1, a + b)
_mult_pair = lambda x: _pair(ar._succ(x(_fir)))(ar._mult(x(_fir))(x(_sec))) # input: pair(a, b). output: pair(a + 1, a * b)
_fibo_pair = lambda x: _pair(x(_sec))(ar._add(x(_fir))(x(_sec))) # input: pair(a, b). output: pair(b, a + b)
