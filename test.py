

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        #ENTRADA DE DADOS
        self.txtText = QtWidgets.QLineEdit(self.centralwidget)
        self.txtText.setGeometry(QtCore.QRect(110, 260, 171, 31))
        self.txtText.setObjectName("txtText")
        self.txtText.setMaxLength(23)

        #LISTA PRODUTOS
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(380, 70, 211, 401))
        self.listWidget.setObjectName("listWidget")


        #LISTA QUANTIDADES
        self.listWidget2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget2.setGeometry(QtCore.QRect(530, 70, 151, 401))
        self.listWidget2.setObjectName("listWidget_2")

        #DEFINIDOR DE QUANTIDADE
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(110, 310, 171, 31))
        self.spinBox.setMaximum(500)



        #TEXTOS
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 520, 51))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 320, 101, 21))
        self.label_2.setObjectName("label_2")

        self.texto_nome = QtWidgets.QLabel(self.centralwidget)
        self.texto_nome.setGeometry(QtCore.QRect(20, 260, 101, 41))
        self.texto_nome.setObjectName("texto_nome")


        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(20)

        self.label.setFont(font)
        self.label.setObjectName("label")

        #GRADE FRONT END
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 70, 281, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grade = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grade.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.grade.setContentsMargins(0, 0, 0, 0)
        self.grade.setObjectName("grade")


        #BOTÕES
        self.botaoRemove = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botaoRemove.setObjectName("botaoRemove")
        self.grade.addWidget(self.botaoRemove, 1, 0, 1, 1)

        self.botaoAdd = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botaoAdd.setObjectName("botaoAdd")
        self.grade.addWidget(self.botaoAdd, 0, 0, 1, 1)

        self.botaoEdit = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botaoEdit.setObjectName("botaoEdit")
        self.grade.addWidget(self.botaoEdit, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.botaoAdd.clicked.connect(self.add_item)
        self.botaoRemove.clicked.connect(self.show_remove_popup())
        self.botaoEdit.clicked.connect(self.edit_item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Estoque atual"))
        self.botaoAdd.setText(_translate("MainWindow", "Adicionar ao estoque"))
        self.botaoRemove.setText(_translate("MainWindow", "Remover do estoque"))
        self.botaoEdit.setText(_translate("MainWindow", "Editar o estoque"))
        self.label_2.setText(_translate("MainWindow", "Quantidade:"))
        self.texto_nome.setText(_translate("MainWindow", "Nome do produto:"))


    #ADIÇÃO DE ITEM
    def add_item(self):
        if(self.txtText.text() == "" or self.spinBox.value() == 0):
            self.label.setText("Preencha os campos corretamente")


        else:
            self.listWidget.addItem(self.txtText.text())
            self.listWidget2.addItem(str(self.spinBox.value()))


    def show_remove_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Remover")
        msg.setText("Deseja mesmo remover o item da lista?")

        x= msg.exec()

    #REMOÇÃO DE ITENS
    def remove_item(self):
        self.row= self.listWidget.currentRow()
        self.listWidget.takeItem(self.row)


        self.row = self.listWidget2.currentRow()
        self.listWidget2.takeItem(self.row)


    #EDIÇÃO DE ITEM
    def edit_item(self):
        #if self.listWidget.currentRow()
        self.row = self.listWidget.currentRow()
        self.listWidget.takeItem(self.row)
        self.listWidget.insertItem(self.row, self.txtText.text())


        self.row = self.listWidget2.currentRow()
        self.listWidget2.takeItem(self.row)
        self.listWidget2.insertItem(self.row, str(self.spinBox.value()))

    def subtracao_item(self):
        pass

    def adicao_item(self):
        pass




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    sys.exit(app.exec_())
