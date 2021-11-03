from . import Erlang


##################
er      = Erlang()
##################


n       = 23
lambda_ = 170
AHT     = 400
t       = 22
ap      = 65

erlang  = lambda_ * (AHT / 3600)
teta    = 1 / (ap / 3600)
mu      = 1 / (AHT / 3600)
ro      = lambda_  / (n * mu)
x       = (n * mu) / teta
y       = lambda_  / teta
AR      = er.ErlangA(x, y, ro)
PW      = ( er.GammaFunction(x, y, 100) * er.ErlangB(erlang, n) ) / (1 + (er.GammaFunction(x, y, 100) - 1) * er.ErlangB(erlang, n) )


print('Service Level ', er.GradeOfService(erlang, n, t, AHT))
print('Abandoned Rate ', AR * PW)
print('Answered immediately', 1 - er.ErlangC(erlang, n))
print('Erlang class', er)

