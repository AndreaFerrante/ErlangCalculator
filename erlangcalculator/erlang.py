from math import exp, factorial


class Erlang(object):


	def __init__(self, shrinkage:float=0.35, calls:int=200, aht:int=400, tat:int=20, ap:int=60):

		super().__init__()
		self.shrinkage = shrinkage
		self.calls     = calls
		self.aht       = aht
		self.tat       = tat
		self.ap        = ap


	def __call__(self, shrinkage:float, calls:int, aht:int, tat:int, ap:int):

		self.shrinkage = shrinkage
		self.calls     = calls
		self.aht       = aht
		self.tat       = tat
		self.ap        = ap


	def __str__(self):

		return 'This class calculates Erlang modelling equations for staffing scientifically a call center. \nTime unit measure is one hour.'


	def GammaFunction(self, x, y, iterations):

		def GetProd(x_, k):

			prod_ = 1

			for j in range(1, k + 1):
				prod_ *= x_ + j

			return prod_

		sum_ = 0

		for i in range(1, iterations + 1):


			sum_ += (y**i / GetProd(x, i))

		return 1 + sum_


	def ErlangA(self, x, y, ro):

		return 1 / (ro * self.GammaFunction(x, y, 100)) + 1 - ( 1 / ro )


	def ErlangB(self, E, N):

		num = (E**N) / factorial(N)
		sum = 0

		for i in range(0, N + 1):
			sum += (E**i) / factorial(i)

		return num / sum


	def ErlangC(self, A, N):

		L    = (A**N / factorial(N)) * (N / (N - A))
		sum_ = 0

		for i in range(N):
			sum_ += (A**i) / factorial(i)

		return ( L / (sum_ + L) )


	def GradeOfService(self, Erlang, n, t, AHT):

		GoS = 1 - self.ErlangC(Erlang, n) * exp( -(n - Erlang) * (t / AHT) )
		return GoS


	@property
	def get_shrinkage(self):
		return self.shrinkage # This parameter has been set like the industry standard (i.e. 35%) . . .

	@property
	def get_calls(self):
		return self.calls # This parameter has been set like the industry standard (i.e. 35%) . . .


	@property
	def get_aht(self):
		return self.aht # Model parameter called average handling time that is answer to the call duration (i.e. AHT) . . .

	@property
	def get_tat(self):
		return self.tat # Model parameter called targeting answering time (i.e. TAT) . . .

	@property
	def get_ap(self):
		return self.ap  # Model parameter called average patience used in abandoned rate calculation (i.e. AP) . . .
	




