# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Base_de_datos_proveedor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Banner_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1065, 948)
        self.actionGuardar_Archivo = QAction(MainWindow)
        self.actionGuardar_Archivo.setObjectName(u"actionGuardar_Archivo")
        self.actionAbrir_Archivo = QAction(MainWindow)
        self.actionAbrir_Archivo.setObjectName(u"actionAbrir_Archivo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setIconSize(QSize(17, 20))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 60, 71, 16))
        self.label_11.setFont(font)
        self.actividad4_lineedit = QLineEdit(self.tab)
        self.actividad4_lineedit.setObjectName(u"actividad4_lineedit")
        self.actividad4_lineedit.setGeometry(QRect(710, 200, 151, 21))
        self.actividad4_lineedit.setClearButtonEnabled(True)
        self.celular_lineedit = QLineEdit(self.tab)
        self.celular_lineedit.setObjectName(u"celular_lineedit")
        self.celular_lineedit.setGeometry(QRect(80, 280, 131, 21))
        self.celular_lineedit.setClearButtonEnabled(True)
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 230, 61, 16))
        self.label_8.setFont(font)
        self.producto6_lineedit = QLineEdit(self.tab)
        self.producto6_lineedit.setObjectName(u"producto6_lineedit")
        self.producto6_lineedit.setGeometry(QRect(450, 280, 151, 21))
        self.producto6_lineedit.setClearButtonEnabled(True)
        self.label_20 = QLabel(self.tab)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(630, 280, 81, 16))
        self.label_20.setFont(font)
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 160, 81, 16))
        self.label_4.setFont(font)
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 170, 61, 16))
        self.label_13.setFont(font)
        self.ciudad_lineedit = QLineEdit(self.tab)
        self.ciudad_lineedit.setObjectName(u"ciudad_lineedit")
        self.ciudad_lineedit.setGeometry(QRect(80, 170, 151, 21))
        self.ciudad_lineedit.setClearButtonEnabled(True)
        self.producto4_lineedit = QLineEdit(self.tab)
        self.producto4_lineedit.setObjectName(u"producto4_lineedit")
        self.producto4_lineedit.setGeometry(QRect(450, 200, 151, 21))
        self.producto4_lineedit.setClearButtonEnabled(True)
        self.actividad2_lineedit = QLineEdit(self.tab)
        self.actividad2_lineedit.setObjectName(u"actividad2_lineedit")
        self.actividad2_lineedit.setGeometry(QRect(710, 120, 151, 21))
        self.actividad2_lineedit.setClearButtonEnabled(True)
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 240, 81, 16))
        self.label_5.setFont(font)
        self.actividad3_lineedit = QLineEdit(self.tab)
        self.actividad3_lineedit.setObjectName(u"actividad3_lineedit")
        self.actividad3_lineedit.setGeometry(QRect(710, 160, 151, 21))
        self.actividad3_lineedit.setClearButtonEnabled(True)
        self.producto3_lineedit = QLineEdit(self.tab)
        self.producto3_lineedit.setObjectName(u"producto3_lineedit")
        self.producto3_lineedit.setGeometry(QRect(450, 160, 151, 21))
        self.producto3_lineedit.setClearButtonEnabled(True)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 200, 81, 16))
        self.label_3.setFont(font)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 80, 81, 16))
        self.label.setFont(font)
        self.actividad1_lineedit = QLineEdit(self.tab)
        self.actividad1_lineedit.setObjectName(u"actividad1_lineedit")
        self.actividad1_lineedit.setGeometry(QRect(710, 80, 151, 21))
        self.actividad1_lineedit.setClearButtonEnabled(True)
        self.label_15 = QLabel(self.tab)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(630, 80, 91, 16))
        self.label_15.setFont(font)
        self.recomienda_lineedit = QLineEdit(self.tab)
        self.recomienda_lineedit.setObjectName(u"recomienda_lineedit")
        self.recomienda_lineedit.setGeometry(QRect(100, 330, 241, 21))
        self.recomienda_lineedit.setClearButtonEnabled(True)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 120, 81, 16))
        self.label_2.setFont(font)
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 280, 61, 16))
        self.label_9.setFont(font)
        self.label_17 = QLabel(self.tab)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(630, 160, 81, 16))
        self.label_17.setFont(font)
        self.telefono_de_oficina_lineedit = QLineEdit(self.tab)
        self.telefono_de_oficina_lineedit.setObjectName(u"telefono_de_oficina_lineedit")
        self.telefono_de_oficina_lineedit.setGeometry(QRect(80, 240, 131, 21))
        self.telefono_de_oficina_lineedit.setClearButtonEnabled(True)
        self.label_19 = QLabel(self.tab)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(630, 240, 81, 16))
        self.label_19.setFont(font)
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 280, 81, 16))
        self.label_6.setFont(font)
        self.label_18 = QLabel(self.tab)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(630, 200, 81, 16))
        self.label_18.setFont(font)
        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 330, 91, 21))
        self.label_12.setFont(font)
        self.estado_lineedit = QLineEdit(self.tab)
        self.estado_lineedit.setObjectName(u"estado_lineedit")
        self.estado_lineedit.setGeometry(QRect(80, 200, 151, 21))
        self.estado_lineedit.setClearButtonEnabled(True)
        self.nombre_lineedit = QLineEdit(self.tab)
        self.nombre_lineedit.setObjectName(u"nombre_lineedit")
        self.nombre_lineedit.setGeometry(QRect(80, 20, 241, 21))
        self.nombre_lineedit.setClearButtonEnabled(True)
        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 200, 51, 16))
        self.label_14.setFont(font)
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 100, 71, 16))
        self.label_10.setFont(font)
        self.actividad6_lineedit = QLineEdit(self.tab)
        self.actividad6_lineedit.setObjectName(u"actividad6_lineedit")
        self.actividad6_lineedit.setGeometry(QRect(710, 280, 151, 21))
        self.actividad6_lineedit.setClearButtonEnabled(True)
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(9, 19, 71, 16))
        self.label_7.setFont(font)
        self.producto1_lineedit = QLineEdit(self.tab)
        self.producto1_lineedit.setObjectName(u"producto1_lineedit")
        self.producto1_lineedit.setGeometry(QRect(450, 80, 151, 21))
        self.producto1_lineedit.setClearButtonEnabled(True)
        self.producto5_lineedit = QLineEdit(self.tab)
        self.producto5_lineedit.setObjectName(u"producto5_lineedit")
        self.producto5_lineedit.setGeometry(QRect(450, 240, 151, 21))
        self.producto5_lineedit.setClearButtonEnabled(True)
        self.empresa_lineedit = QLineEdit(self.tab)
        self.empresa_lineedit.setObjectName(u"empresa_lineedit")
        self.empresa_lineedit.setGeometry(QRect(80, 60, 241, 21))
        self.empresa_lineedit.setClearButtonEnabled(True)
        self.producto2_lineedit = QLineEdit(self.tab)
        self.producto2_lineedit.setObjectName(u"producto2_lineedit")
        self.producto2_lineedit.setGeometry(QRect(450, 120, 151, 21))
        self.producto2_lineedit.setClearButtonEnabled(True)
        self.actividad5_lineedit = QLineEdit(self.tab)
        self.actividad5_lineedit.setObjectName(u"actividad5_lineedit")
        self.actividad5_lineedit.setGeometry(QRect(710, 240, 151, 21))
        self.actividad5_lineedit.setClearButtonEnabled(True)
        self.agregar_guardar_pushbutton = QPushButton(self.tab)
        self.agregar_guardar_pushbutton.setObjectName(u"agregar_guardar_pushbutton")
        self.agregar_guardar_pushbutton.setGeometry(QRect(10, 460, 871, 31))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.agregar_guardar_pushbutton.setFont(font1)
        self.agregar_guardar_pushbutton.setStyleSheet(u"background-color: rgb(199, 199, 199);")
        self.label_23 = QLabel(self.tab)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 250, 61, 16))
        self.label_23.setFont(font)
        self.direccion_lineedit = QLineEdit(self.tab)
        self.direccion_lineedit.setObjectName(u"direccion_lineedit")
        self.direccion_lineedit.setGeometry(QRect(80, 100, 241, 21))
        self.direccion_lineedit.setClearButtonEnabled(True)
        self.label_24 = QLabel(self.tab)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(600, 20, 101, 41))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(20)
        self.label_24.setFont(font2)
        self.label_24.setTextFormat(Qt.AutoText)
        self.label_24.setOpenExternalLinks(False)
        self.label_25 = QLabel(self.tab)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(630, 120, 91, 16))
        self.label_25.setFont(font)
        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(350, 310, 531, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(350, 10, 531, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(340, 20, 20, 301))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(870, 20, 20, 301))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.mostrar_todo_plaintextedit = QPlainTextEdit(self.tab)
        self.mostrar_todo_plaintextedit.setObjectName(u"mostrar_todo_plaintextedit")
        self.mostrar_todo_plaintextedit.setGeometry(QRect(20, 540, 871, 281))
        self.agregar_mostrar_todos_los_proveedores_pushbutton = QPushButton(self.tab)
        self.agregar_mostrar_todos_los_proveedores_pushbutton.setObjectName(u"agregar_mostrar_todos_los_proveedores_pushbutton")
        self.agregar_mostrar_todos_los_proveedores_pushbutton.setGeometry(QRect(20, 830, 871, 31))
        self.agregar_mostrar_todos_los_proveedores_pushbutton.setFont(font)
        self.label_16 = QLabel(self.tab)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 420, 71, 21))
        self.label_26 = QLabel(self.tab)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 370, 141, 21))
        self.correo_electronico_lineedit = QLineEdit(self.tab)
        self.correo_electronico_lineedit.setObjectName(u"correo_electronico_lineedit")
        self.correo_electronico_lineedit.setGeometry(QRect(130, 370, 211, 21))
        self.correo_electronico_lineedit.setClearButtonEnabled(True)
        self.link_lineedit = QLineEdit(self.tab)
        self.link_lineedit.setObjectName(u"link_lineedit")
        self.link_lineedit.setGeometry(QRect(50, 420, 831, 21))
        self.link_lineedit.setClearButtonEnabled(True)
        self.label_27 = QLabel(self.tab)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 130, 61, 16))
        self.label_27.setFont(font)
        self.colonia_lineedit = QLineEdit(self.tab)
        self.colonia_lineedit.setObjectName(u"colonia_lineedit")
        self.colonia_lineedit.setGeometry(QRect(80, 130, 151, 20))
        self.colonia_lineedit.setClearButtonEnabled(True)
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(350, 20, 531, 301))
        self.widget.setAutoFillBackground(True)
        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(410, 10, 31, 41))
        self.label_21.setStyleSheet(u"border-image: url(:/cct/2.png);")
        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(140, 10, 51, 41))
        self.label_22.setStyleSheet(u"border-image: url(:/cct/Producto.ico);")
        self.label_30 = QLabel(self.widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(410, 10, 41, 41))
        self.label_30.setStyleSheet(u"border-image: url(:/imagenes/2.png);")
        self.label_31 = QLabel(self.widget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(140, 10, 61, 41))
        self.label_31.setStyleSheet(u"border-image: url(:/imagenes/Producto.ico);")
        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-11, -1, 911, 501))
        self.widget_2.setAutoFillBackground(True)
        icon = QIcon()
        icon.addFile(u"Signo Mas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        self.widget_2.raise_()
        self.widget.raise_()
        self.label_11.raise_()
        self.actividad4_lineedit.raise_()
        self.celular_lineedit.raise_()
        self.label_8.raise_()
        self.producto6_lineedit.raise_()
        self.label_20.raise_()
        self.label_4.raise_()
        self.label_13.raise_()
        self.ciudad_lineedit.raise_()
        self.producto4_lineedit.raise_()
        self.actividad2_lineedit.raise_()
        self.label_5.raise_()
        self.actividad3_lineedit.raise_()
        self.producto3_lineedit.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.actividad1_lineedit.raise_()
        self.label_15.raise_()
        self.recomienda_lineedit.raise_()
        self.label_2.raise_()
        self.label_9.raise_()
        self.label_17.raise_()
        self.telefono_de_oficina_lineedit.raise_()
        self.label_19.raise_()
        self.label_6.raise_()
        self.label_18.raise_()
        self.label_12.raise_()
        self.estado_lineedit.raise_()
        self.nombre_lineedit.raise_()
        self.label_14.raise_()
        self.label_10.raise_()
        self.actividad6_lineedit.raise_()
        self.label_7.raise_()
        self.producto1_lineedit.raise_()
        self.producto5_lineedit.raise_()
        self.empresa_lineedit.raise_()
        self.producto2_lineedit.raise_()
        self.actividad5_lineedit.raise_()
        self.agregar_guardar_pushbutton.raise_()
        self.label_23.raise_()
        self.direccion_lineedit.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.mostrar_todo_plaintextedit.raise_()
        self.agregar_mostrar_todos_los_proveedores_pushbutton.raise_()
        self.label_16.raise_()
        self.label_26.raise_()
        self.correo_electronico_lineedit.raise_()
        self.link_lineedit.raise_()
        self.label_27.raise_()
        self.colonia_lineedit.raise_()
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.busqueda_lineedit = QLineEdit(self.tab_2)
        self.busqueda_lineedit.setObjectName(u"busqueda_lineedit")
        self.busqueda_lineedit.setGeometry(QRect(20, 540, 661, 51))
        font3 = QFont()
        font3.setFamily(u"Yu Gothic Medium")
        font3.setPointSize(12)
        self.busqueda_lineedit.setFont(font3)
        self.busqueda_lineedit.setStyleSheet(u"")
        self.buscar_pushbutton = QPushButton(self.tab_2)
        self.buscar_pushbutton.setObjectName(u"buscar_pushbutton")
        self.buscar_pushbutton.setGeometry(QRect(700, 540, 151, 51))
        self.buscar_pushbutton.setFont(font1)
        self.buscar_pushbutton.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.buscar_pushbutton.setStyleSheet(u"image: url(:/cct/lupa 2.ico);\n"
"image: url(:/imagenes/lupa 2.ico);")
        self.widget_3 = QWidget(self.tab_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 1091, 531))
        self.widget_3.setAutoFillBackground(True)
        self.tabla = QTableWidget(self.widget_3)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(20, 20, 1001, 491))
        self.tabla.setTextElideMode(Qt.ElideNone)
        self.reestablecer_pushbutton = QPushButton(self.tab_2)
        self.reestablecer_pushbutton.setObjectName(u"reestablecer_pushbutton")
        self.reestablecer_pushbutton.setGeometry(QRect(870, 540, 151, 51))
        self.reestablecer_pushbutton.setFont(font1)
        self.reestablecer_pushbutton.setStyleSheet(u"background-color: rgb(244, 128, 153);\n"
"background-color: rgb(225, 82, 101);")
        self.widget_4 = QWidget(self.tab_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(-10, 530, 1051, 71))
        self.widget_4.setAutoFillBackground(False)
        self.widget_4.setStyleSheet(u"background-color: rgb(211, 210, 221);")
        icon1 = QIcon()
        icon1.addFile(u"Lupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon1, "")
        self.widget_4.raise_()
        self.widget_3.raise_()
        self.busqueda_lineedit.raise_()
        self.buscar_pushbutton.raise_()
        self.reestablecer_pushbutton.raise_()
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.pushButton_23 = QPushButton(self.tab_3)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(480, 370, 121, 41))
        self.pushButton_24 = QPushButton(self.tab_3)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(1040, 280, 121, 41))
        self.pushButton_25 = QPushButton(self.tab_3)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(900, 180, 121, 41))
        self.pushButton_26 = QPushButton(self.tab_3)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(900, 330, 121, 41))
        self.pushButton_27 = QPushButton(self.tab_3)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(480, 320, 121, 41))
        self.pushButton_28 = QPushButton(self.tab_3)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(340, 220, 121, 41))
        self.pushButton_29 = QPushButton(self.tab_3)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(900, 230, 121, 41))
        self.pushButton_30 = QPushButton(self.tab_3)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(1040, 330, 121, 41))
        self.pushButton_31 = QPushButton(self.tab_3)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setGeometry(QRect(340, 370, 121, 41))
        self.pushButton_32 = QPushButton(self.tab_3)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setGeometry(QRect(1040, 180, 121, 41))
        self.pushButton_33 = QPushButton(self.tab_3)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setGeometry(QRect(340, 170, 121, 41))
        self.pushButton_34 = QPushButton(self.tab_3)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setGeometry(QRect(480, 220, 121, 41))
        self.label_28 = QLabel(self.tab_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(370, 130, 201, 31))
        font4 = QFont()
        font4.setFamily(u"Times New Roman")
        font4.setPointSize(14)
        self.label_28.setFont(font4)
        self.pushButton_35 = QPushButton(self.tab_3)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setGeometry(QRect(340, 320, 121, 41))
        self.pushButton_36 = QPushButton(self.tab_3)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setGeometry(QRect(900, 280, 121, 41))
        self.pushButton_37 = QPushButton(self.tab_3)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setGeometry(QRect(480, 270, 121, 41))
        self.pushButton_38 = QPushButton(self.tab_3)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setGeometry(QRect(1040, 230, 121, 41))
        self.pushButton_39 = QPushButton(self.tab_3)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setGeometry(QRect(480, 170, 121, 41))
        self.pushButton_40 = QPushButton(self.tab_3)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setGeometry(QRect(340, 270, 121, 41))
        self.pushButton_41 = QPushButton(self.tab_3)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setGeometry(QRect(1040, 380, 121, 41))
        self.label_29 = QLabel(self.tab_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(950, 140, 191, 31))
        self.label_29.setFont(font4)
        self.pushButton_42 = QPushButton(self.tab_3)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setGeometry(QRect(900, 380, 121, 41))
        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1065, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir_Archivo)
        self.menuArchivo.addAction(self.actionGuardar_Archivo)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        self.actionGuardar_Archivo.setText(QCoreApplication.translate("MainWindow", u"Guardar Archivo", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar_Archivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbrir_Archivo.setText(QCoreApplication.translate("MainWindow", u"Abrir Archivo", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir_Archivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Empresa :", None))
        self.actividad4_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba la actividad 4...", None))
        self.celular_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite el celular...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.producto6_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba el producto 6...", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Oficio 6 :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Producto 3 :", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ciudad :", None))
        self.ciudad_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba la ciudad...", None))
        self.producto4_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba el producto 4...", None))
        self.actividad2_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba la actividad 2...", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Producto 5 :", None))
        self.actividad3_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba la actividad 3...", None))
        self.producto3_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba el producto 3...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Producto 4 :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Producto 1 :", None))
        self.actividad1_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ejemplo. Fontanero", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Oficio 1 :", None))
        self.recomienda_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Persona que lo recomienda...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Producto 2 :", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Celular :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Oficio 3 :", None))
        self.telefono_de_oficina_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite el telefono de oficina", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Oficio 5 :", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Producto 6 :", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Oficio 4 :", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Recomienda :", None))
        self.estado_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba el estado...", None))
        self.nombre_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escribe el nombre completo...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Estado :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n :", None))
        self.actividad6_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba la actividad 6...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nombre :", None))
        self.producto1_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ejemplo. Fabuloso", None))
        self.producto5_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba el producto 5...", None))
        self.empresa_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba el nombre de la empresa...", None))
        self.producto2_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba el producto 2...", None))
        self.actividad5_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba la actividad 5...", None))
        self.agregar_guardar_pushbutton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"de oficina", None))
        self.direccion_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ejmplo. Calle Miguel #928", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Servicios", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Oficio 2 :", None))
        self.agregar_mostrar_todos_los_proveedores_pushbutton.setText(QCoreApplication.translate("MainWindow", u"MOSTRAR TODOS LOS PROVEEDORES", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Link:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Correo electr\u00f3nico:", None))
        self.correo_electronico_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ejemplo123@gmail.com", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Colonia:", None))
        self.colonia_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba la colonia", None))
        self.label_21.setText("")
        self.label_22.setText("")
        self.label_30.setText("")
        self.label_31.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.busqueda_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por oficio, producto, colonia, ciudad o estado, persona que lo recomienda...", None))
        self.buscar_pushbutton.setText("")
        self.reestablecer_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Reestablecer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Buscar por Actividad", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Buscar por Actividad", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Buscar por Actividad", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Buscar por Actividad", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Buscar por Actividad", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"Buscar por Actividad", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Buscar por Oficio", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Buscar por Actividad", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Buscar por Actividad", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"Buscar por Actividad", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Buscar por Servicios", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"Buscar por Actividad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

