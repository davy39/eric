# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Preferences/ConfigurationPages/QtPage.ui'
#
# Created: Tue Nov 18 17:53:56 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QtPage(object):
    def setupUi(self, QtPage):
        QtPage.setObjectName("QtPage")
        QtPage.resize(642, 614)
        self.verticalLayout = QtWidgets.QVBoxLayout(QtPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(QtPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line12 = QtWidgets.QFrame(QtPage)
        self.line12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line12.setObjectName("line12")
        self.verticalLayout.addWidget(self.line12)
        self.groupBox_3 = QtWidgets.QGroupBox(QtPage)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridlayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridlayout.setObjectName("gridlayout")
        self.qt4TransEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.qt4TransEdit.setObjectName("qt4TransEdit")
        self.gridlayout.addWidget(self.qt4TransEdit, 1, 0, 1, 1)
        self.TextLabel1_2_2_5 = QtWidgets.QLabel(self.groupBox_3)
        self.TextLabel1_2_2_5.setObjectName("TextLabel1_2_2_5")
        self.gridlayout.addWidget(self.TextLabel1_2_2_5, 0, 0, 1, 2)
        self.textLabel1_2_4 = QtWidgets.QLabel(self.groupBox_3)
        self.textLabel1_2_4.setWordWrap(True)
        self.textLabel1_2_4.setObjectName("textLabel1_2_4")
        self.gridlayout.addWidget(self.textLabel1_2_4, 2, 0, 1, 2)
        self.qt4TransButton = QtWidgets.QToolButton(self.groupBox_3)
        self.qt4TransButton.setObjectName("qt4TransButton")
        self.gridlayout.addWidget(self.qt4TransButton, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(QtPage)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridlayout1 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridlayout1.setObjectName("gridlayout1")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridlayout1.addWidget(self.label, 0, 0, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.gridlayout1.addWidget(self.label_3, 1, 0, 1, 1)
        self.qt4PrefixEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.qt4PrefixEdit.setObjectName("qt4PrefixEdit")
        self.gridlayout1.addWidget(self.qt4PrefixEdit, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridlayout1.addWidget(self.label_5, 1, 2, 1, 1)
        self.qt4PostfixEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.qt4PostfixEdit.setObjectName("qt4PostfixEdit")
        self.gridlayout1.addWidget(self.qt4PostfixEdit, 1, 3, 1, 1)
        self.qt4SampleLabel = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qt4SampleLabel.sizePolicy().hasHeightForWidth())
        self.qt4SampleLabel.setSizePolicy(sizePolicy)
        self.qt4SampleLabel.setObjectName("qt4SampleLabel")
        self.gridlayout1.addWidget(self.qt4SampleLabel, 1, 4, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(QtPage)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.pyuicIndentSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.pyuicIndentSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pyuicIndentSpinBox.setMinimum(2)
        self.pyuicIndentSpinBox.setMaximum(16)
        self.pyuicIndentSpinBox.setProperty("value", 4)
        self.pyuicIndentSpinBox.setObjectName("pyuicIndentSpinBox")
        self.gridLayout.addWidget(self.pyuicIndentSpinBox, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(448, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.pyuicImportsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.pyuicImportsCheckBox.setObjectName("pyuicImportsCheckBox")
        self.gridLayout.addWidget(self.pyuicImportsCheckBox, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(496, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(QtPage)
        QtCore.QMetaObject.connectSlotsByName(QtPage)
        QtPage.setTabOrder(self.qt4TransEdit, self.qt4TransButton)
        QtPage.setTabOrder(self.qt4TransButton, self.qt4PrefixEdit)
        QtPage.setTabOrder(self.qt4PrefixEdit, self.qt4PostfixEdit)
        QtPage.setTabOrder(self.qt4PostfixEdit, self.pyuicIndentSpinBox)
        QtPage.setTabOrder(self.pyuicIndentSpinBox, self.pyuicImportsCheckBox)

    def retranslateUi(self, QtPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("QtPage", "<b>Configure Qt</b>"))
        self.groupBox_3.setTitle(_translate("QtPage", "Qt Translations Directory"))
        self.qt4TransEdit.setToolTip(_translate("QtPage", "Enter the path of the Qt translations directory."))
        self.TextLabel1_2_2_5.setText(_translate("QtPage", "<font color=\"#FF0000\"><b>Note:</b> This setting is activated at the next startup of the application.</font>"))
        self.textLabel1_2_4.setText(_translate("QtPage", "<b>Note:</b> Leave this entry empty to use the QT4TRANSLATIONSDIR environment variable or the path compiled into the Qt library."))
        self.qt4TransButton.setToolTip(_translate("QtPage", "Press to select the Qt translations directory via a directory selection dialog"))
        self.groupBox_4.setTitle(_translate("QtPage", "Qt Tools"))
        self.label.setText(_translate("QtPage", "The tool executable is composed of the prefix, the tool name and the postfix. For win, the extension is added automatically."))
        self.label_3.setText(_translate("QtPage", "Qt-Prefix:"))
        self.qt4PrefixEdit.setToolTip(_translate("QtPage", "Enter the prefix for the Qt tools name"))
        self.label_5.setText(_translate("QtPage", "Qt-Postfix:"))
        self.qt4PostfixEdit.setToolTip(_translate("QtPage", "Enter the postfix for the Qt tools name"))
        self.qt4SampleLabel.setToolTip(_translate("QtPage", "This gives an example of the complete tool name"))
        self.qt4SampleLabel.setText(_translate("QtPage", "designer"))
        self.groupBox.setTitle(_translate("QtPage", "pyuic / pyside-uic Options"))
        self.label_2.setText(_translate("QtPage", "Indent Width:"))
        self.pyuicIndentSpinBox.setToolTip(_translate("QtPage", "Select the indent width (default: 4)"))
        self.pyuicImportsCheckBox.setText(_translate("QtPage", "Generate imports relative to \'.\'"))
