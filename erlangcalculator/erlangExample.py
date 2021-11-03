from erlangcalculator.erlangClass import Erlang


def erlang_example_printer():

	##################
	er      = Erlang()
	##################


	n       = 23   # - inforced of the number of agents...
	lambda_ = 170  # - calls per hour...
	AHT     = 400  # - duration in seconds of the answer call...
	t       = 22   # - targeting answering time...
	ap      = 65   # - average patience of clients...


	erlang  = lambda_ * (AHT / 3600) # this is the erlang as unit measure...
	teta    = 1 / (ap / 3600)
	mu      = 1 / (AHT / 3600)
	ro      = lambda_  / (n * mu)
	x       = (n * mu) / teta
	y       = lambda_  / teta
	AR      = er.ErlangA(x, y, ro)
	PW      = ( er.GammaFunction(x, y, 100) * er.ErlangB(erlang, n) ) / (1 + (er.GammaFunction(x, y, 100) - 1) * er.ErlangB(erlang, n) )


	print('---------------------------------------------------------')
	print('Service Level ', er.GradeOfService(erlang, n, t, AHT))
	print('Abandoned Rate ', AR * PW)
	print('Answered immediately', 1 - er.ErlangC(erlang, n))
	print('---------------------------------------------------------')