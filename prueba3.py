# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba3.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 490, 481, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 771, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(580, 270, 151, 31))
        self.label_23.setObjectName("label_23")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(360, 150, 131, 31))
        self.label_4.setObjectName("label_4")
        self.label_ptrdash = QtWidgets.QLabel(self.tab_3)
        self.label_ptrdash.setGeometry(QtCore.QRect(580, 370, 161, 31))
        self.label_ptrdash.setObjectName("label_ptrdash")
        self.label_valorrub = QtWidgets.QLabel(self.tab_3)
        self.label_valorrub.setGeometry(QtCore.QRect(570, 180, 131, 31))
        self.label_valorrub.setObjectName("label_valorrub")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(190, 270, 151, 31))
        self.label_12.setObjectName("label_12")
        self.label_ltcptr = QtWidgets.QLabel(self.tab_3)
        self.label_ltcptr.setGeometry(QtCore.QRect(380, 320, 151, 31))
        self.label_ltcptr.setObjectName("label_ltcptr")
        self.label_fecha = QtWidgets.QLabel(self.tab_3)
        self.label_fecha.setGeometry(QtCore.QRect(280, 0, 321, 31))
        self.label_fecha.setObjectName("label_fecha")
        self.label_f = QtWidgets.QLabel(self.tab_3)
        self.label_f.setGeometry(QtCore.QRect(380, 270, 161, 31))
        self.label_f.setObjectName("label_f")
        self.label_btcptr = QtWidgets.QLabel(self.tab_3)
        self.label_btcptr.setGeometry(QtCore.QRect(0, 320, 151, 31))
        self.label_btcptr.setObjectName("label_btcptr")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_3.setObjectName("label_3")
        self.label_dashptr = QtWidgets.QLabel(self.tab_3)
        self.label_dashptr.setGeometry(QtCore.QRect(580, 320, 161, 31))
        self.label_dashptr.setObjectName("label_dashptr")
        self.label_ethptr = QtWidgets.QLabel(self.tab_3)
        self.label_ethptr.setGeometry(QtCore.QRect(190, 320, 151, 31))
        self.label_ethptr.setObjectName("label_ethptr")
        self.label_ptrltc = QtWidgets.QLabel(self.tab_3)
        self.label_ptrltc.setGeometry(QtCore.QRect(380, 370, 151, 31))
        self.label_ptrltc.setObjectName("label_ptrltc")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(0, 150, 131, 31))
        self.label_2.setObjectName("label_2")
        self.label_valorusd = QtWidgets.QLabel(self.tab_3)
        self.label_valorusd.setGeometry(QtCore.QRect(170, 180, 131, 31))
        self.label_valorusd.setObjectName("label_valorusd")
        self.label_valorbs = QtWidgets.QLabel(self.tab_3)
        self.label_valorbs.setGeometry(QtCore.QRect(0, 110, 131, 31))
        self.label_valorbs.setObjectName("label_valorbs")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(170, 150, 131, 31))
        self.label_5.setObjectName("label_5")
        self.label_ptreth = QtWidgets.QLabel(self.tab_3)
        self.label_ptreth.setGeometry(QtCore.QRect(190, 370, 151, 31))
        self.label_ptreth.setObjectName("label_ptreth")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(0, 270, 151, 31))
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(0, 40, 301, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(570, 150, 141, 31))
        self.label_7.setObjectName("label_7")
        self.label_ptrbtc = QtWidgets.QLabel(self.tab_3)
        self.label_ptrbtc.setGeometry(QtCore.QRect(0, 370, 151, 31))
        self.label_ptrbtc.setObjectName("label_ptrbtc")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(0, 230, 301, 31))
        self.label_17.setObjectName("label_17")
        self.label_valorcny = QtWidgets.QLabel(self.tab_3)
        self.label_valorcny.setGeometry(QtCore.QRect(360, 180, 131, 31))
        self.label_valorcny.setObjectName("label_valorcny")
        self.label_valoreur = QtWidgets.QLabel(self.tab_3)
        self.label_valoreur.setGeometry(QtCore.QRect(0, 180, 131, 31))
        self.label_valoreur.setObjectName("label_valoreur")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(0, 0, 321, 31))
        self.label.setObjectName("label")
        self.label_btcptr_3 = QtWidgets.QLabel(self.tab_3)
        self.label_btcptr_3.setGeometry(QtCore.QRect(0, 300, 151, 31))
        self.label_btcptr_3.setObjectName("label_btcptr_3")
        self.label_btcptr_4 = QtWidgets.QLabel(self.tab_3)
        self.label_btcptr_4.setGeometry(QtCore.QRect(0, 350, 151, 31))
        self.label_btcptr_4.setObjectName("label_btcptr_4")
        self.label_btcptr_5 = QtWidgets.QLabel(self.tab_3)
        self.label_btcptr_5.setGeometry(QtCore.QRect(190, 350, 151, 31))
        self.label_btcptr_5.setObjectName("label_btcptr_5")
        self.label_btcptr_6 = QtWidgets.QLabel(self.tab_3)
        self.label_btcptr_6.setGeometry(QtCore.QRect(190, 300, 151, 31))
        self.label_btcptr_6.setObjectName("label_btcptr_6")
        self.label_btcptr_8 = QtWidgets.QLabel(self.tab_3)
        self.label_btcptr_8.setGeometry(QtCore.QRect(380, 350, 151, 31))
        self.label_btcptr_8.setObjectName("label_btcptr_8")
        self.label_btcptr_9 = QtWidgets.QLabel(self.tab_3)
        self.label_btcptr_9.setGeometry(QtCore.QRect(380, 300, 151, 31))
        self.label_btcptr_9.setObjectName("label_btcptr_9")
        self.label_btcptr_11 = QtWidgets.QLabel(self.tab_3)
        self.label_btcptr_11.setGeometry(QtCore.QRect(580, 300, 151, 31))
        self.label_btcptr_11.setObjectName("label_btcptr_11")
        self.label_btcptr_12 = QtWidgets.QLabel(self.tab_3)
        self.label_btcptr_12.setGeometry(QtCore.QRect(580, 350, 151, 31))
        self.label_btcptr_12.setObjectName("label_btcptr_12")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 321, 31))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(10, 80, 151, 31))
        self.label_13.setObjectName("label_13")
        self.label_ptrbtc_2 = QtWidgets.QLabel(self.tab_4)
        self.label_ptrbtc_2.setGeometry(QtCore.QRect(10, 140, 151, 31))
        self.label_ptrbtc_2.setObjectName("label_ptrbtc_2")
        self.label_btcptr_2 = QtWidgets.QLabel(self.tab_4)
        self.label_btcptr_2.setGeometry(QtCore.QRect(10, 110, 151, 31))
        self.label_btcptr_2.setObjectName("label_btcptr_2")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 301, 31))
        self.label_14.setObjectName("label_14")
        self.label_cptrventa = QtWidgets.QLabel(self.tab_4)
        self.label_cptrventa.setGeometry(QtCore.QRect(80, 110, 151, 31))
        self.label_cptrventa.setObjectName("label_cptrventa")
        self.label_cptrcompra = QtWidgets.QLabel(self.tab_4)
        self.label_cptrcompra.setGeometry(QtCore.QRect(90, 140, 151, 31))
        self.label_cptrcompra.setObjectName("label_cptrcompra")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(270, 80, 151, 31))
        self.label_15.setObjectName("label_15")
        self.label_ptrbtc_3 = QtWidgets.QLabel(self.tab_4)
        self.label_ptrbtc_3.setGeometry(QtCore.QRect(270, 140, 151, 31))
        self.label_ptrbtc_3.setObjectName("label_ptrbtc_3")
        self.label_cptr1venta = QtWidgets.QLabel(self.tab_4)
        self.label_cptr1venta.setGeometry(QtCore.QRect(340, 110, 151, 31))
        self.label_cptr1venta.setObjectName("label_cptr1venta")
        self.label_cptr1compra = QtWidgets.QLabel(self.tab_4)
        self.label_cptr1compra.setGeometry(QtCore.QRect(350, 140, 151, 31))
        self.label_cptr1compra.setObjectName("label_cptr1compra")
        self.label_btcptr_7 = QtWidgets.QLabel(self.tab_4)
        self.label_btcptr_7.setGeometry(QtCore.QRect(270, 110, 151, 31))
        self.label_btcptr_7.setObjectName("label_btcptr_7")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(530, 80, 151, 31))
        self.label_16.setObjectName("label_16")
        self.label_ptrbtc_4 = QtWidgets.QLabel(self.tab_4)
        self.label_ptrbtc_4.setGeometry(QtCore.QRect(530, 140, 151, 31))
        self.label_ptrbtc_4.setObjectName("label_ptrbtc_4")
        self.label_cbtcventa = QtWidgets.QLabel(self.tab_4)
        self.label_cbtcventa.setGeometry(QtCore.QRect(600, 110, 151, 31))
        self.label_cbtcventa.setObjectName("label_cbtcventa")
        self.label_cbtccompra = QtWidgets.QLabel(self.tab_4)
        self.label_cbtccompra.setGeometry(QtCore.QRect(610, 140, 151, 31))
        self.label_cbtccompra.setObjectName("label_cbtccompra")
        self.label_btcptr_10 = QtWidgets.QLabel(self.tab_4)
        self.label_btcptr_10.setGeometry(QtCore.QRect(530, 110, 151, 31))
        self.label_btcptr_10.setObjectName("label_btcptr_10")
        self.tabWidget.addTab(self.tab_4, "")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 500, 64, 17))
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 430, 501, 61))
        self.label_8.setObjectName("label_8")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 530, 481, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(10, 540, 64, 17))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(610, 490, 141, 61))
        self.label_19.setObjectName("label_19")
        self.tabWidget.raise_()
        self.textBrowser.raise_()
        self.label_10.raise_()
        self.label_8.raise_()
        self.textBrowser_2.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Por ahora no :)</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Dash (DASH)</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Yuan (CNY)</span></p></body></html>"))
        self.label_ptrdash.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Tasa PTR/DASH</span></p></body></html>"))
        self.label_valorrub.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Valor RUB</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Ether (ETH)</span></p></body></html>"))
        self.label_ltcptr.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Tasa LTC/PTR</span></p></body></html>"))
        self.label_fecha.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">fecha</span></p></body></html>"))
        self.label_f.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Litecoin (LTC)</span></p></body></html>"))
        self.label_btcptr.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Tasa BTC/PTR</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Bolívar (Bs)</span></p></body></html>"))
        self.label_dashptr.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Tasa DASH/PTR</span></p></body></html>"))
        self.label_ethptr.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Tasa ETHPTR</span></p></body></html>"))
        self.label_ptrltc.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Tasa PTR/LTC</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Euro (EUR)</span></p></body></html>"))
        self.label_valorusd.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Valor USD</span></p></body></html>"))
        self.label_valorbs.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Valor Bs</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Dolar (USD)</span></p></body></html>"))
        self.label_ptreth.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Tasa PTR/ETH</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Bitcoin (BTC)</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Divisas Internacionales</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Rublo (RUB)</span></p></body></html>"))
        self.label_ptrbtc.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Tasa PTR/BTC</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Criptomonedas</span></p></body></html>"))
        self.label_valorcny.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Valor CNY</span></p></body></html>"))
        self.label_valoreur.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Valor EUR</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">COTIZACIÓN DEL PETRO</span></p></body></html>"))
        self.label_btcptr_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">BTC/PTR:</span></p></body></html>"))
        self.label_btcptr_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">PTR/BTC:</span></p></body></html>"))
        self.label_btcptr_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">PTR/ETH:</span></p></body></html>"))
        self.label_btcptr_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">ETH/PTR:</span></p></body></html>"))
        self.label_btcptr_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">PTR/LTC:</span></p></body></html>"))
        self.label_btcptr_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">LTC/PTR:</span></p></body></html>"))
        self.label_btcptr_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">DASH/PTR:</span></p></body></html>"))
        self.label_btcptr_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">PTR/DASH:</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">TASAS EXCHANGES</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">PTR/Bs</span></p></body></html>"))
        self.label_ptrbtc_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Compra:</span></p></body></html>"))
        self.label_btcptr_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Venta: </span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Criptolago</span></p></body></html>"))
        self.label_cptrventa.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Tasa Venta</span></p></body></html>"))
        self.label_cptrcompra.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Tasa Compra</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">PTR/BTC</span></p></body></html>"))
        self.label_ptrbtc_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Compra:</span></p></body></html>"))
        self.label_cptr1venta.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Tasa Venta</span></p></body></html>"))
        self.label_cptr1compra.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Tasa Compra</span></p></body></html>"))
        self.label_btcptr_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Venta: </span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">BTC/Bs</span></p></body></html>"))
        self.label_ptrbtc_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Compra:</span></p></body></html>"))
        self.label_cbtcventa.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Tasa Venta</span></p></body></html>"))
        self.label_cbtccompra.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Tasa Compra</span></p></body></html>"))
        self.label_btcptr_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Venta: </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">BTC</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Este software se encuentra en fase de desarrollo </span><span style=\" font-size:12pt;\"><br/>Desarrollado por Andrés Bustamante para </span><span style=\" font-size:12pt; font-style:italic;\">Cripto Economía Vzla</span><span style=\" font-size:12pt;\"><br/>Contribuciones</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Por ahora no :)</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">PTR</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">Fuentes:<br/>API Prices/Sunacrip<br/>API Criptolago</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
