from heapq import heappush, heappop
from itertools import combinations

class Battle:
	def __init__(self, cava, casa):
		self.fronteira = []
		self.list_cava = cava
		self.poder_casa = casa 

	def calcular_tempo(self, seque):
		soma_poder = 0
		poder_vida = 0
		for i in seque:
			soma_poder += self.list_cava[i].poder
			if self.list_cava[i].vida < 5:
				poder_vida += self.list_cava[i].poder * (5 - self.list_cava[i].vida + 2)
			else:
				poder_vida += self.list_cava[i].poder
		return self.poder_casa/soma_poder, poder_vida

	def buscar(self, maxTime, seque):
		print(maxTime)
		lista = []
		fronteira = []
		tempo, poder_vida = self.calcular_tempo(seque)
		V = Vertice(seque, tempo, poder_vida)
		fronteira.append(V)

		while fronteira != []:

			#TODO: retirar no da fronetira
			u = fronteira.pop(0)
			if u.quat > 1:
				cobinacoes = combinations(u.seque, u.quat-1)

				for cobi_i in cobinacoes:
					tempo, poder_vida = self.calcular_tempo(cobi_i)
					if tempo < maxTime:
						V = Vertice(cobi_i, tempo, poder_vida)
						heappush(lista, V)
						fronteira.append(V)

		return heappop(lista)
	

class Vertice:
	def __init__(self, seque, tempo, poder_vida):
		self.seque = seque
		self.quat = len(seque)
		self.tempo = tempo
		self.heuri = tempo/poder_vida
	
	def __lt__(self, other):
		return self.heuri > other.heuri
