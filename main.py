import os
import sys
import glob
import eyed3

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


print('convert .ui to .py')
os.system("pyuic5 -x gui/form.ui -o gui.py")

print('convert completed')
from gui import Ui_MainWindow

from audioplayer import AudioPlayer


class PlayerGui(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

		self.minimize_window_button.clicked.connect(lambda: self.showMinimized())
		self.close_window_button.clicked.connect(lambda: self.close())
		self.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

		self.list_music = []
		self.play_now = 0

		self.get_list_music()
		self.pause = False
		self.player = AudioPlayer()
		self.load_music(self.list_music[self.play_now])

		self.btn_play.clicked.connect(self.play_music)
		self.btn_next.clicked.connect(self.next_music)
		self.btn_back.clicked.connect(self.back_music)

		def moveWindow(e):
			if self.isMaximized() == False:
				if e.buttons() == Qt.LeftButton:
					self.move(self.pos() + e.globalPos() - self.clickPosition)
					self.clickPosition = e.globalPos()
					e.accept()
		self.frame_header.mouseMoveEvent = moveWindow

	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()

	def restore_or_maximize_window(self):
		if self.isMaximized():
			self.showNormal()
			self.restore_window_button.setIcon(QtGui.QIcon("img\\cil-window-restore.png"))
		else:
			self.showMaximized()
			self.restore_window_button.setIcon(QtGui.QIcon("img\\cil-window-maximize.png"))

	def load_music(self, music):
		self.player.load_music(music)
		self.player.play_music()
		self.player.pause_music()
		self.show_title()

	def play_music(self):
		play_ico = QtGui.QIcon()
		if self.pause:
			play_ico.addPixmap(QtGui.QPixmap("gui\\../img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.pause = False
		else:
			play_ico.addPixmap(QtGui.QPixmap("gui\\../img/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.pause = True
		
		#self.btn_play.setIcon(play_ico)
		self.btn_play.setIconSize(QtCore.QSize(55, 55))
		self.player.pause_music()

	def next_music(self):
		self.play_now += 1
		try:
			self.player.next_music(self.list_music[self.play_now])
		except IndexError:
			self.play_now = 0
			self.player.next_music(self.list_music[self.play_now])

		self.show_title()

	def back_music(self):
		self.play_now -= 1
		if self.play_now < 0:
			self.play_now = 0

		self.player.next_music(self.list_music[self.play_now])
		self.show_title()

	def show_title(self):
		data = eyed3.load(self.list_music[self.play_now])

		artist = data.tag.artist
		if artist:
			if len(artist) > 20:
				artist = artist[:19] + '...'
		else:
			artist = 'Unknown Artist'
		title = data.tag.title
		if title:
			if len(title) > 20:
				title = title[:19] + '...'
		else:
			title = 'Unknown Title'
		self.label_title.setText(str(title))
		self.label_albom.setText(str(artist))


	def get_list_music(self, location='music'):
		os.chdir(location)
		self.list_music = []
		for file in glob.glob("*.mp3", recursive=True):
			self.list_music.append(file)



if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = PlayerGui()
	window.show()
	sys.exit(app.exec_())

