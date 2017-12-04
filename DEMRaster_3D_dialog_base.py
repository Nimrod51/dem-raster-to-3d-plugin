# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DEMRaster_3D_dialog_base.ui'
#
# Created: Sun Aug 13 12:30:06 2017
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DEMRasterTo3DDialogBase(object):
    def setupUi(self, DEMRasterTo3DDialogBase):
        DEMRasterTo3DDialogBase.setObjectName(_fromUtf8("DEMRasterTo3DDialogBase"))
        DEMRasterTo3DDialogBase.resize(400, 300)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 240, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 240, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 240, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 240, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        DEMRasterTo3DDialogBase.setPalette(palette)
        self.label_3 = QtGui.QLabel(DEMRasterTo3DDialogBase)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 71, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(DEMRasterTo3DDialogBase)
        self.lineEdit.setGeometry(QtCore.QRect(110, 140, 181, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.toolButton = QtGui.QToolButton(DEMRasterTo3DDialogBase)
        self.toolButton.setGeometry(QtCore.QRect(300, 140, 27, 22))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.label_2 = QtGui.QLabel(DEMRasterTo3DDialogBase)
        self.label_2.setGeometry(QtCore.QRect(10, 240, 387, 38))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_5 = QtGui.QLabel(DEMRasterTo3DDialogBase)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 341, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(DEMRasterTo3DDialogBase)
        self.label.setGeometry(QtCore.QRect(50, 90, 281, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(DEMRasterTo3DDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(150, 180, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(DEMRasterTo3DDialogBase)
        QtCore.QMetaObject.connectSlotsByName(DEMRasterTo3DDialogBase)

    def retranslateUi(self, DEMRasterTo3DDialogBase):
        DEMRasterTo3DDialogBase.setWindowTitle(_translate("DEMRasterTo3DDialogBase", "DEM Raster to 3D Plot", None))
        self.label_3.setText(_translate("DEMRasterTo3DDialogBase", "Input Raster:", None))
        self.toolButton.setText(_translate("DEMRasterTo3DDialogBase", "...", None))
        self.label_2.setText(_translate("DEMRasterTo3DDialogBase", "<html><head/><body><p align=\"justify\">*Depending on your raster file, this may take a long time. </p><p align=\"justify\">It is suggested to lower the resolution of your raster file to increase the cell size.</p></body></html>", None))
        self.label_5.setText(_translate("DEMRasterTo3DDialogBase", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Raster DEM as 3D Flying Carpet</span></p></body></html>", None))
        self.label.setText(_translate("DEMRasterTo3DDialogBase", "Enter the directory to your raster DEM file and press Run!", None))
        self.pushButton.setText(_translate("DEMRasterTo3DDialogBase", "Run!", None))

