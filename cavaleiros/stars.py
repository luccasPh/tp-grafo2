from heapq import heappush, heappop
from math import sqrt


class Stars:
    def __init__(self):
        self.fronteira = []

    def distancia(self, player, casa):
        return sqrt((player.pos_x - casa.pos_x) ** 2 + (player.pos_y - casa.pos_y) ** 2)

    def buscar(self, player, casa, mapa):

        d = 0
        V = Vertice(player.pos_x, player.pos_y, d, player.peso, 0)
        mapa.mapa_vis[player.pos_x][player.pos_y] = True

        self.fronteira.append(V)

        while self.fronteira != []:

            # TODO: retirar no da fronetira
            u = heappop(self.fronteira)

            if u.v_x == casa.pos_x and u.v_y == casa.pos_y:
                V = u
                player.peso = u.peso
                break

            for i in range(4):
                x, y = player.movi(i)
                player.pos_x = u.v_x + x
                player.pos_y = u.v_y + y

                if not mapa.mapa_vis[player.pos_x][
                    player.pos_y
                ]:  # and mapa.pos(player.pos_x, player.pos_y) != 0:
                    p = mapa.peso(player.pos_x, player.pos_y)
                    p_t = p + u.peso
                    d = self.distancia(player, casa) + p_t
                    V = Vertice(player.pos_x, player.pos_y, d, p_t, p)
                    V.pai = u
                    heappush(self.fronteira, V)

            mapa.mapa_vis[u.v_x][u.v_y] = True

        caminho = []
        while True:
            caminho.insert(0, V)
            if V.pai == None:
                break
            V = V.pai

        return caminho


class Vertice:
    def __init__(self, v_x, v_y, d, p, t):
        self.v_x = v_x
        self.v_y = v_y
        self.dist = d
        self.peso = p
        self.tempo = t
        self.pai = None

    def __lt__(self, other):
        return self.dist < other.dist
