# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_header = QtWidgets.QFrame(self.centralwidget)
        self.frame_header.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_header.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_header.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.frame_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setObjectName("frame_header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_header)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header_center_frame = QtWidgets.QFrame(self.frame_header)
        self.header_center_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_center_frame.setObjectName("header_center_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout.addWidget(self.header_center_frame)
        self.frame = QtWidgets.QFrame(self.frame_header)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.label_2.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("gui\\../img/icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.frame)
        self.header_right_frame = QtWidgets.QFrame(self.frame_header)
        self.header_right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_right_frame.setObjectName("header_right_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.minimize_window_button = QtWidgets.QPushButton(self.header_right_frame)
        self.minimize_window_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui\\../../python/sys_info/sys_info/icons/cil-minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_window_button.setIcon(icon)
        self.minimize_window_button.setObjectName("minimize_window_button")
        self.horizontalLayout_5.addWidget(self.minimize_window_button)
        self.restore_window_button = QtWidgets.QPushButton(self.header_right_frame)
        self.restore_window_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("gui\\../../python/sys_info/sys_info/icons/cil-window-restore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restore_window_button.setIcon(icon1)
        self.restore_window_button.setObjectName("restore_window_button")
        self.horizontalLayout_5.addWidget(self.restore_window_button)
        self.close_window_button = QtWidgets.QPushButton(self.header_right_frame)
        self.close_window_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("gui\\../../python/sys_info/sys_info/icons/X.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_window_button.setIcon(icon2)
        self.close_window_button.setObjectName("close_window_button")
        self.horizontalLayout_5.addWidget(self.close_window_button)
        self.horizontalLayout.addWidget(self.header_right_frame, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_header)
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 320))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_img = QtWidgets.QFrame(self.frame_top)
        self.frame_img.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_img.setObjectName("frame_img")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_img)
        self.gridLayout.setObjectName("gridLayout")
        self.label_img = QtWidgets.QLabel(self.frame_img)
        self.label_img.setMaximumSize(QtCore.QSize(200, 200))
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap("gui\\../img/Music.jpg"))
        self.label_img.setScaledContents(True)
        self.label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img.setObjectName("label_img")
        self.gridLayout.addWidget(self.label_img, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_img)
        self.frame_controls = QtWidgets.QFrame(self.frame_top)
        self.frame_controls.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_controls.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_controls.setObjectName("frame_controls")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_controls)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_controls)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_back = QtWidgets.QPushButton(self.frame_2)
        self.btn_back.setStyleSheet("QPushButton{\n"
"border-width: 5px;\n"
"border-style: solid;\n"
"border-radius: 25px;;\n"
"border-color: rgb(24, 24, 24);\n"
"background-color: qlineargradient(spread:pad, x1:0.474, y1:1, x2:0.484221, y2:0, stop:0.0328638 rgba(0, 0, 0, 255), stop:0.478873 rgba(56, 56, 56, 255), stop:0.957746 rgba(98, 98, 98, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.46, y1:0, x2:0.488915, y2:1, stop:0.0328638 rgba(0, 0, 0, 255), stop:0.488263 rgba(56, 56, 56, 255), stop:0.957746 rgba(98, 98, 98, 255));\n"
"}")
        self.btn_back.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("gui\\../img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon3)
        self.btn_back.setIconSize(QtCore.QSize(40, 40))
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_3.addWidget(self.btn_back)
        self.btn_play = QtWidgets.QPushButton(self.frame_2)
        self.btn_play.setStyleSheet("QPushButton{\n"
"border-width: 5px;\n"
"border-style: solid;\n"
"border-radius: 30px;;\n"
"border-color: rgb(24, 24, 24);\n"
"background-color: qlineargradient(spread:pad, x1:0.474, y1:1, x2:0.484221, y2:0, stop:0.0328638 rgba(0, 0, 0, 255), stop:0.478873 rgba(56, 56, 56, 255), stop:0.957746 rgba(98, 98, 98, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.46, y1:0, x2:0.488915, y2:1, stop:0.0328638 rgba(0, 0, 0, 255), stop:0.488263 rgba(56, 56, 56, 255), stop:0.957746 rgba(98, 98, 98, 255));\n"
"}")
        self.btn_play.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("gui\\../img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon4)
        self.btn_play.setIconSize(QtCore.QSize(55, 55))
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout_3.addWidget(self.btn_play)
        self.btn_next = QtWidgets.QPushButton(self.frame_2)
        self.btn_next.setStyleSheet("QPushButton{\n"
"border-width: 5px;\n"
"border-style: solid;\n"
"border-radius: 25px;;\n"
"border-color: rgb(24, 24, 24);\n"
"background-color: qlineargradient(spread:pad, x1:0.474, y1:1, x2:0.484221, y2:0, stop:0.0328638 rgba(0, 0, 0, 255), stop:0.478873 rgba(56, 56, 56, 255), stop:0.957746 rgba(98, 98, 98, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.46, y1:0, x2:0.488915, y2:1, stop:0.0328638 rgba(0, 0, 0, 255), stop:0.488263 rgba(56, 56, 56, 255), stop:0.957746 rgba(98, 98, 98, 255));\n"
"}")
        self.btn_next.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("gui\\../img/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next.setIcon(icon5)
        self.btn_next.setIconSize(QtCore.QSize(40, 40))
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout_3.addWidget(self.btn_next)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame_controls)
        self.frame_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.music_volume = QtWidgets.QSlider(self.frame_4)
        self.music_volume.setStyleSheet("QSlider::groove:vertical {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:1, stop:0 rgba(22, 22, 22, 255), stop:0.446009 rgba(40, 40, 40, 255), stop:0.699531 rgba(40, 40, 40, 255), stop:1 rgba(29, 29, 29, 255));\n"
"    border-radius: 5px;\n"
"    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"    left: 4px; right: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 15px;\n"
"    background-color: rgb(97, 97, 97);\n"
"    margin: 0 -4px; /* expand outside the groove */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    border-radius: 5px;\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(0, 49, 145, 255), stop:0.399061 rgba(0, 49, 145, 255), stop:0.7277 rgba(0, 87, 255, 255), stop:1 rgba(0, 87, 255, 255));\n"
"}\n"
"")
        self.music_volume.setOrientation(QtCore.Qt.Vertical)
        self.music_volume.setObjectName("music_volume")
        self.verticalLayout_4.addWidget(self.music_volume)
        self.label_volum_img = QtWidgets.QLabel(self.frame_4)
        self.label_volum_img.setMaximumSize(QtCore.QSize(50, 50))
        self.label_volum_img.setText("")
        self.label_volum_img.setPixmap(QtGui.QPixmap("gui\\../img/volume.png"))
        self.label_volum_img.setScaledContents(True)
        self.label_volum_img.setObjectName("label_volum_img")
        self.verticalLayout_4.addWidget(self.label_volum_img)
        self.gridLayout_2.addWidget(self.frame_4, 1, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_controls)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_title = QtWidgets.QLabel(self.frame_3)
        self.label_title.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_title.setFont(font)
        self.label_title.setAcceptDrops(False)
        self.label_title.setStyleSheet("color: rgb(5, 186, 188);")
        self.label_title.setScaledContents(False)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setWordWrap(False)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_3.addWidget(self.label_title)
        self.label_albom = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_albom.setFont(font)
        self.label_albom.setStyleSheet("color: rgb(131, 131, 136);")
        self.label_albom.setAlignment(QtCore.Qt.AlignCenter)
        self.label_albom.setObjectName("label_albom")
        self.verticalLayout_3.addWidget(self.label_albom)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 2)
        self.horizontalLayout_2.addWidget(self.frame_controls)
        self.verticalLayout.addWidget(self.frame_top, 0, QtCore.Qt.AlignTop)
        self.frame_bottom = QtWidgets.QFrame(self.centralwidget)
        self.frame_bottom.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_bottom.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_bottom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.music_slider = QtWidgets.QSlider(self.frame_bottom)
        self.music_slider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border-radius: 7px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(22, 22, 22, 255), stop:0.446009 rgba(40, 40, 40, 255), stop:0.699531 rgba(40, 40, 40, 255), stop:1 rgba(29, 29, 29, 255));\n"
"    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"    left: 4px; right: 4px;\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    border-radius: 7px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 85, 255, 255), stop:0.262911 rgba(0, 89, 255, 255), stop:0.57277 rgba(0, 57, 162, 255), stop:1 rgba(0, 47, 141, 255));\n"
"}")
        self.music_slider.setOrientation(QtCore.Qt.Horizontal)
        self.music_slider.setObjectName("music_slider")
        self.verticalLayout_2.addWidget(self.music_slider)
        self.label = QtWidgets.QLabel(self.frame_bottom)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_bottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "My Player"))
        self.label_title.setText(_translate("MainWindow", "Unknown Title"))
        self.label_albom.setText(_translate("MainWindow", "Unknown Albom - Track 10"))
        self.label.setText(_translate("MainWindow", "25:10 / 70:10"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
