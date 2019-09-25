from PyQt5 import QtWidgets, QtGui, QtCore
from datetime import timedelta
from cavaleiros.stars import Stars
from cavaleiros.fim import Fim
from cavaleiros.battle import Battle
from cavaleiros.mapa import mapa_casas
from PyQt5 import QtMultimedia
import time
#from bfs import BFS
import sys, os

class Player:
	def __init__(self, pos_x, pos_y):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.peso = 0

	def movi(self, i):
		mov_x = [0,0,1,-1]
		mov_y = [1,-1,0,0]

		return mov_x[i], mov_y[i]


class Mapa:
	def __init__(self, alt, larg, mapa):
		self.alt = alt
		self.larg = larg
		self.mapa = mapa_casas
		self.mapa_vis = []
		self.vis()
	
	def pos(self, x, y):
	
		return self.mapa[x][y]
	
	def peso(self, x, y):
		if self.mapa[x][y] == 0:
			return 200
		
		elif self.mapa[x][y] == 1 or self.mapa[x][y] == 3:
			return 1
		
		elif self.mapa[x][y] == 2:
			return 5

	def vis(self):
		for i in range(self.alt):
			self.mapa_vis.append([])
			for j in range(self.larg):
				self.mapa_vis[i].append(False)

class IA:
	def __init__(self):
		self.S = Stars()

	def solu(self, cava, casa, mapa):
		return self.S.buscar(cava, casa, mapa)


class Result(QtWidgets.QWidget):
	def __init__(self, maxTime, cava, casa):
		super(Result, self).__init__()
		self.audio = os.path.join(os.path.dirname(__file__), 'audio')
		self.image = os.path.join(os.path.dirname(__file__), 'image')
		self.initUI(maxTime, cava, casa)

	def initUI(self, maxTime, cava, casa):
		self.setStyleSheet("QWidget { background: rgb(0,0,0) }") 
		self.setFixedSize(772, 672)
		self.setWindowTitle('App')
		self.fim = None
		self.battle = False
		self.seque_cav = [0,1,2,3,4]
		self.cavaleiros = cava

		audioUrl = QtCore.QUrl.fromLocalFile(os.path.join(self.audio, 'soundtrack.mp3'))
		audioOutput = QtMultimedia.QMediaContent(audioUrl)
		self.mediaObject = QtMultimedia.QMediaPlayer()
		self.mediaObject.setMedia(audioOutput)
		self.mediaObject.play()

		self.player = Player(37,37)
		self.casas = casa
		self.maxTime = maxTime

		self.mapa = Mapa(42,42,mapa_casas)
		self.caminho = IA().solu(self.player, self.casas[0], self.mapa)
		self.timer = QtCore.QBasicTimer()
		self.novo = 0
		self.casa_at = 0
		self.total_casa = 12
		self.tempo = 0
		self.fim = None

		self.start()
		self.show()

	def start(self):
		self.timer.start(200, self)
		self.update()

	def paintEvent(self, event):
		qp = QtGui.QPainter()
		qp.begin(self)
		self.drawMapa(qp)
		qp.drawPixmap(37 * 16, 4 * 16,QtGui.QPixmap(os.path.join(self.image,'athena.png')))
		self.drawCava(qp)
		self.placarLife(qp)
		self.placarTime(qp)
		#print(self.tempo)
		if self.battle:
			b = Battle(self.cavaleiros, self.casas[self.casa_at-1].difi)
			self.total_casa -= 1
			res = b.buscar(self.maxTime, self.seque_cav)
			self.tempo += int(res.tempo)
			seque = list(res.seque)
			for i in seque:
				self.cavaleiros[i].vida -= 1
			self.drawBattle(qp,len(seque), seque)
			self.battle = False
			self.timer.stop()
			QtCore.QTimer.singleShot(2000, lambda:self.start())
		#self.drawQue(qp)
		qp.end()

	def keyPressEvent(self, e):
		if self.battle and e.key() == QtCore.Qt.Key_Space:
			self.start()


	def moviCava(self):
		if self.checaStatu():
			self.tempo += self.caminho[self.novo].tempo
			#print(self.caminho[self.novo].peso)
			self.player.pos_x = self.caminho[self.novo].v_x
			self.player.pos_y = self.caminho[self.novo].v_y
			if self.mapa.mapa[self.caminho[self.novo].v_x][self.caminho[self.novo].v_y] != 3:
				self.mapa.mapa[self.caminho[self.novo].v_x][self.caminho[self.novo].v_y] = 4
			self.novo += 1

	def checaStatu(self):
		for i in self.seque_cav:
			if self.cavaleiros[i].vida == 0:
				self.seque_cav.remove(i)

		if self.player.pos_x == 4 and self.player.pos_y == 37:
			self.timer.stop()
			self.mediaObject.stop()
			self.tela = QtWidgets.QWidget()
			self.ui = Fim()
			self.ui.setupUi(self.tela)
			self.tela.show()
			return False

		elif self.player.pos_x == self.casas[self.casa_at].pos_x and self.player.pos_y == self.casas[self.casa_at].pos_y:
			self.battle = True
			self.casa_at += 1
			self.novo = 0
			self.caminho = IA().solu(self.player, self.casas[self.casa_at], self.mapa)
			return True

		return True

	def drawMapa(self, qp):
		qp.setPen(QtCore.Qt.NoPen)
		for i in range(self.mapa.larg):
			for j in range(self.mapa.alt):
				if self.mapa.mapa[i][j] == 0:
					qp.setBrush(QtGui.QColor(95, 95, 95))
					qp.drawRect(j * 16, i * 16, 15, 15)
				if self.mapa.mapa[i][j] == 1:
					qp.setBrush(QtGui.QColor(164, 164, 164))
					qp.drawRect(j * 16, i * 16, 15, 15)

				if self.mapa.mapa[i][j] == 2:
					qp.setBrush(QtGui.QColor(217, 217, 217))
					qp.drawRect(j * 16, i * 16, 15, 15)

				if self.mapa.mapa[i][j] == 4:
					qp.setBrush(QtGui.QColor(242, 0, 0))
					qp.drawRect(j * 16, i * 16, 15, 15)

				if self.mapa.mapa[i][j] == 3:
					qp.drawPixmap(j * 16, i * 16, QtGui.QPixmap(os.path.join(self.image, 'templo.png')))

	def drawCava(self, qp):
		qp.drawPixmap(self.player.pos_y * 16, self.player.pos_x * 16, QtGui.QPixmap(os.path.join(self.image, 'seya.png')))

	def placarLife(self, qp):
		if self.cavaleiros[0].vida == 0:
			qp.drawPixmap(42 * 16, 0 * 16, QtGui.QPixmap(os.path.join(self.image, 'seya2_rip.png')))
		else:
			qp.drawPixmap(42 * 16, 0 * 16, QtGui.QPixmap(os.path.join(self.image, 'seya2.png')))
		for i in range(self.cavaleiros[0].vida):
			qp.drawPixmap((42 + i) * 16, 5 * 16, QtGui.QPixmap(os.path.join(self.image, 'vida.png')))

		if self.cavaleiros[1].vida == 0:
			qp.drawPixmap(42 * 16, 7 * 16, QtGui.QPixmap(os.path.join(self.image, 'shiryu_rip.png')))
		else:
			qp.drawPixmap(42 * 16, 7 * 16, QtGui.QPixmap(os.path.join(self.image, 'shiryu.png')))
		for i in range(self.cavaleiros[1].vida):
			qp.drawPixmap((42 + i) * 16, 12 * 16, QtGui.QPixmap(os.path.join(self.image, 'vida.png')))
		
		if self.cavaleiros[2].vida == 0:
			qp.drawPixmap(42 * 16, 14 * 16, QtGui.QPixmap(os.path.join(self.image, 'hyoga_rip.png')))
		else:
			qp.drawPixmap(42 * 16, 14 * 16, QtGui.QPixmap(os.path.join(self.image, 'hyoga.png')))
		for i in range(self.cavaleiros[2].vida):
			qp.drawPixmap((42 + i) * 16, 19.2 * 16, QtGui.QPixmap(os.path.join(self.image, 'vida.png')))

		if self.cavaleiros[3].vida == 0:
			qp.drawPixmap(42 * 16, 21 * 16, QtGui.QPixmap(os.path.join(self.image, 'shun_rip.png')))
		else:
			qp.drawPixmap(42 * 16, 21 * 16, QtGui.QPixmap(os.path.join(self.image, 'shun.png')))
		for i in range(self.cavaleiros[3].vida):
			qp.drawPixmap((42 + i) * 16, 26.5 * 16, QtGui.QPixmap(os.path.join(self.image, 'vida.png')))

		if self.cavaleiros[4].vida == 0:
			qp.drawPixmap(43 * 16, 27.7 * 16, QtGui.QPixmap(os.path.join(self.image, 'ikki_rip.png')))
		else:
			qp.drawPixmap(43 * 16, 27.7 * 16, QtGui.QPixmap(os.path.join(self.image, 'ikki.png')))
		for i in range(self.cavaleiros[4].vida):
			qp.drawPixmap((42 + i) * 16, 33 * 16, QtGui.QPixmap(os.path.join(self.image, 'vida.png')))
		

	
	def drawBattle(self, qp, cava, seque):
		cava -= 1
		cs = 25 + cava
		vs = 20 + cava
		cv = 10 + cava

		qp.drawPixmap(16 * 16, 13 * 16, QtGui.QPixmap(os.path.join(self.image, self.casas[self.casa_at-1].title)))
		qp.drawPixmap(cs * 16, 15 * 16, QtGui.QPixmap(os.path.join(self.image, self.casas[self.casa_at-1].cava_or)))
		qp.drawPixmap(vs * 16, 20 * 16, QtGui.QPixmap(os.path.join(self.image, 'VS2.png')))
		qp.drawPixmap(cv * 16, 15 * 16, QtGui.QPixmap(os.path.join(self.image, self.cavaleiros[seque[0]].cava)))

		seque.pop(0)
		for i in (seque):
			cv -= 6
			qp.drawPixmap(cv * 16, 15 * 16, QtGui.QPixmap(os.path.join(self.image, self.cavaleiros[i].cava)))


	def placarTime(self, qp):
		qp.setPen(QtGui.QColor(255, 255, 255))
		qp.setFont(QtGui.QFont('Times', 22))
		qp.drawText(42 * 16, 37 * 16, "TEMPO")
		qp.drawText(42 * 16, 39 * 16, str(timedelta(minutes=self.tempo))[:-3]) 


	def timerEvent(self, event):
		self.moviCava()
		self.repaint()


"""
if __name__ == '__main__':
	qt = QtGui.QApplication(sys.argv)
	app = App()
	sys.exit(qt.exec_())
"""