# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\degrada_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1092, 857)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1047, 1622))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QtCore.QSize(0, 1600))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableView_TABLA = QtWidgets.QTableView(self.frame)
        self.tableView_TABLA.setGeometry(QtCore.QRect(530, 40, 491, 271))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableView_TABLA.setFont(font)
        self.tableView_TABLA.setObjectName("tableView_TABLA")
        self.pushButton_ACTUALIZAR = QtWidgets.QPushButton(self.frame)
        self.pushButton_ACTUALIZAR.setGeometry(QtCore.QRect(0, 0, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_ACTUALIZAR.setFont(font)
        self.pushButton_ACTUALIZAR.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_ACTUALIZAR.setMouseTracking(False)
        self.pushButton_ACTUALIZAR.setWhatsThis("")
        self.pushButton_ACTUALIZAR.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/OneDrive - ITALTEL PERU SAC/Escritorio/566023-901529706.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ACTUALIZAR.setIcon(icon)
        self.pushButton_ACTUALIZAR.setObjectName("pushButton_ACTUALIZAR")
        self.lbl_actual = QtWidgets.QLabel(self.frame)
        self.lbl_actual.setGeometry(QtCore.QRect(50, 20, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lbl_actual.setFont(font)
        self.lbl_actual.setObjectName("lbl_actual")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 391, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_EJECUTAR = QtWidgets.QPushButton(self.frame)
        self.pushButton_EJECUTAR.setGeometry(QtCore.QRect(190, 250, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_EJECUTAR.setFont(font)
        self.pushButton_EJECUTAR.setObjectName("pushButton_EJECUTAR")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(500, 40, 20, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(90, 310, 321, 31))
        self.progressBar.setMinimum(0)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(10, 350, 1011, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 480, 491, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_izq = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_izq.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_izq.setObjectName("verticalLayout_izq")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(520, 480, 501, 451))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_der = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_der.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_der.setObjectName("verticalLayout_der")
        self.comboBox_WTG_I = QtWidgets.QComboBox(self.frame)
        self.comboBox_WTG_I.setGeometry(QtCore.QRect(80, 380, 51, 21))
        self.comboBox_WTG_I.setObjectName("comboBox_WTG_I")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 380, 41, 21))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 410, 55, 21))
        self.label_4.setObjectName("label_4")
        self.comboBox_ANNO_I_GR = QtWidgets.QComboBox(self.frame)
        self.comboBox_ANNO_I_GR.setEnabled(False)
        self.comboBox_ANNO_I_GR.setGeometry(QtCore.QRect(80, 410, 61, 22))
        self.comboBox_ANNO_I_GR.setObjectName("comboBox_ANNO_I_GR")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(170, 400, 21, 31))
        self.label_5.setObjectName("label_5")
        self.comboBox_ANNO_J_GR = QtWidgets.QComboBox(self.frame)
        self.comboBox_ANNO_J_GR.setEnabled(False)
        self.comboBox_ANNO_J_GR.setGeometry(QtCore.QRect(260, 410, 61, 22))
        self.comboBox_ANNO_J_GR.setObjectName("comboBox_ANNO_J_GR")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(220, 410, 31, 21))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(220, 380, 41, 21))
        self.label_8.setObjectName("label_8")
        self.comboBox_WTG_J = QtWidgets.QComboBox(self.frame)
        self.comboBox_WTG_J.setEnabled(False)
        self.comboBox_WTG_J.setGeometry(QtCore.QRect(260, 380, 51, 21))
        self.comboBox_WTG_J.setEditable(False)
        self.comboBox_WTG_J.setFrame(True)
        self.comboBox_WTG_J.setObjectName("comboBox_WTG_J")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(540, 10, 411, 16))
        self.label_9.setObjectName("label_9")
        self.checkBox_BLOQUEAR = QtWidgets.QCheckBox(self.frame)
        self.checkBox_BLOQUEAR.setEnabled(True)
        self.checkBox_BLOQUEAR.setGeometry(QtCore.QRect(330, 380, 81, 20))
        self.checkBox_BLOQUEAR.setChecked(True)
        self.checkBox_BLOQUEAR.setObjectName("checkBox_BLOQUEAR")
        self.comboBox_ANNO_J = QtWidgets.QComboBox(self.frame)
        self.comboBox_ANNO_J.setGeometry(QtCore.QRect(300, 140, 73, 31))
        self.comboBox_ANNO_J.setObjectName("comboBox_ANNO_J")
        self.comboBox_MES_J = QtWidgets.QComboBox(self.frame)
        self.comboBox_MES_J.setGeometry(QtCore.QRect(210, 140, 61, 31))
        self.comboBox_MES_J.setObjectName("comboBox_MES_J")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(280, 140, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(130, 140, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(260, 170, 55, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox_MES_I_GR = QtWidgets.QComboBox(self.frame)
        self.comboBox_MES_I_GR.setEnabled(False)
        self.comboBox_MES_I_GR.setGeometry(QtCore.QRect(80, 440, 61, 22))
        self.comboBox_MES_I_GR.setObjectName("comboBox_MES_I_GR")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setEnabled(True)
        self.label_16.setGeometry(QtCore.QRect(40, 440, 55, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(220, 440, 55, 21))
        self.label_17.setObjectName("label_17")
        self.comboBox_MES_J_GR = QtWidgets.QComboBox(self.frame)
        self.comboBox_MES_J_GR.setEnabled(False)
        self.comboBox_MES_J_GR.setGeometry(QtCore.QRect(260, 440, 61, 22))
        self.comboBox_MES_J_GR.setObjectName("comboBox_MES_J_GR")
        self.pushButton_DESCARGAR_TABLA = QtWidgets.QPushButton(self.frame)
        self.pushButton_DESCARGAR_TABLA.setGeometry(QtCore.QRect(920, 320, 93, 28))
        self.pushButton_DESCARGAR_TABLA.setObjectName("pushButton_DESCARGAR_TABLA")
        self.pushButton_DESCARGA_GR_IZ = QtWidgets.QPushButton(self.frame)
        self.pushButton_DESCARGA_GR_IZ.setGeometry(QtCore.QRect(400, 940, 93, 28))
        self.pushButton_DESCARGA_GR_IZ.setObjectName("pushButton_DESCARGA_GR_IZ")
        self.pushButton_DESCARGA_GR_DR = QtWidgets.QPushButton(self.frame)
        self.pushButton_DESCARGA_GR_DR.setEnabled(False)
        self.pushButton_DESCARGA_GR_DR.setGeometry(QtCore.QRect(920, 940, 93, 28))
        self.pushButton_DESCARGA_GR_DR.setObjectName("pushButton_DESCARGA_GR_DR")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(130, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.checkBox_turbina = QtWidgets.QCheckBox(self.frame)
        self.checkBox_turbina.setGeometry(QtCore.QRect(300, 60, 91, 31))
        self.checkBox_turbina.setChecked(False)
        self.checkBox_turbina.setObjectName("checkBox_turbina")
        self.comboBox_ejey = QtWidgets.QComboBox(self.frame)
        self.comboBox_ejey.setGeometry(QtCore.QRect(590, 380, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_ejey.setFont(font)
        self.comboBox_ejey.setObjectName("comboBox_ejey")
        self.comboBox_ejex = QtWidgets.QComboBox(self.frame)
        self.comboBox_ejex.setGeometry(QtCore.QRect(590, 410, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_ejex.setFont(font)
        self.comboBox_ejex.setObjectName("comboBox_ejex")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(540, 380, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(540, 410, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.pushButton_graf_der = QtWidgets.QPushButton(self.frame)
        self.pushButton_graf_der.setGeometry(QtCore.QRect(630, 440, 93, 28))
        self.pushButton_graf_der.setObjectName("pushButton_graf_der")
        self.pushButton_login = QtWidgets.QPushButton(self.frame)
        self.pushButton_login.setGeometry(QtCore.QRect(400, 0, 93, 28))
        self.pushButton_login.setObjectName("pushButton_login")
        self.label_usuario = QtWidgets.QLabel(self.frame)
        self.label_usuario.setGeometry(QtCore.QRect(230, 1, 161, 20))
        self.label_usuario.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_usuario.setObjectName("label_usuario")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(130, 200, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.comboBox_MES_I = QtWidgets.QComboBox(self.frame)
        self.comboBox_MES_I.setGeometry(QtCore.QRect(210, 201, 61, 31))
        self.comboBox_MES_I.setObjectName("comboBox_MES_I")
        self.comboBox_ANNO_I = QtWidgets.QComboBox(self.frame)
        self.comboBox_ANNO_I.setGeometry(QtCore.QRect(300, 201, 73, 31))
        self.comboBox_ANNO_I.setObjectName("comboBox_ANNO_I")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(280, 201, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(220, 120, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(300, 120, 55, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_inv = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_inv.setGeometry(QtCore.QRect(210, 60, 71, 31))
        self.lineEdit_inv.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_inv.setObjectName("lineEdit_inv")
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Esperanza - curvas"))
        self.lbl_actual.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "Actualizar datos"))
        self.pushButton_EJECUTAR.setText(_translate("MainWindow", "Ejecutar"))
        self.label.setText(_translate("MainWindow", "INV:"))
        self.label_4.setText(_translate("MainWindow", "A??O:"))
        self.label_5.setText(_translate("MainWindow", "vs"))
        self.label_6.setText(_translate("MainWindow", "A??O:"))
        self.label_8.setText(_translate("MainWindow", "INV:"))
        self.label_9.setText(_translate("MainWindow", "Inversores con mayor degradaci??n entre mes base y mes eval:"))
        self.checkBox_BLOQUEAR.setText(_translate("MainWindow", "bloquear"))
        self.label_13.setText(_translate("MainWindow", "/"))
        self.label_12.setText(_translate("MainWindow", "Mes base:"))
        self.label_3.setText(_translate("MainWindow", "vs."))
        self.label_16.setText(_translate("MainWindow", "MES:"))
        self.label_17.setText(_translate("MainWindow", "MES:"))
        self.pushButton_DESCARGAR_TABLA.setText(_translate("MainWindow", "Descargar"))
        self.pushButton_DESCARGA_GR_IZ.setText(_translate("MainWindow", "Descargar"))
        self.pushButton_DESCARGA_GR_DR.setText(_translate("MainWindow", "Descargar"))
        self.label_15.setText(_translate("MainWindow", "Inversor:"))
        self.checkBox_turbina.setText(_translate("MainWindow", "Todo"))
        self.label_18.setText(_translate("MainWindow", "Eje Y:"))
        self.label_19.setText(_translate("MainWindow", "Eje X:"))
        self.pushButton_graf_der.setText(_translate("MainWindow", "Aceptar"))
        self.pushButton_login.setText(_translate("MainWindow", "Iniciar sesi??n"))
        self.label_usuario.setText(_translate("MainWindow", "No ha iniciado sesi??n"))
        self.label_11.setText(_translate("MainWindow", "Mes eval:"))
        self.label_10.setText(_translate("MainWindow", "/"))
        self.label_7.setText(_translate("MainWindow", "Mes:"))
        self.label_14.setText(_translate("MainWindow", "A??o:"))
        self.lineEdit_inv.setPlaceholderText(_translate("MainWindow", "1.1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
