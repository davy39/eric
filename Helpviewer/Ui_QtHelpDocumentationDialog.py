# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Helpviewer/QtHelpDocumentationDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QtHelpDocumentationDialog(object):
    def setupUi(self, QtHelpDocumentationDialog):
        QtHelpDocumentationDialog.setObjectName("QtHelpDocumentationDialog")
        QtHelpDocumentationDialog.resize(425, 391)
        QtHelpDocumentationDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(QtHelpDocumentationDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(QtHelpDocumentationDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.documentsList = QtWidgets.QListWidget(QtHelpDocumentationDialog)
        self.documentsList.setAlternatingRowColors(True)
        self.documentsList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.documentsList.setObjectName("documentsList")
        self.gridLayout.addWidget(self.documentsList, 0, 0, 3, 1)
        self.addButton = QtWidgets.QPushButton(QtHelpDocumentationDialog)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.removeButton = QtWidgets.QPushButton(QtHelpDocumentationDialog)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 98, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(QtHelpDocumentationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(QtHelpDocumentationDialog)
        self.buttonBox.accepted.connect(QtHelpDocumentationDialog.accept)
        self.buttonBox.rejected.connect(QtHelpDocumentationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QtHelpDocumentationDialog)
        QtHelpDocumentationDialog.setTabOrder(self.documentsList, self.addButton)
        QtHelpDocumentationDialog.setTabOrder(self.addButton, self.removeButton)
        QtHelpDocumentationDialog.setTabOrder(self.removeButton, self.buttonBox)

    def retranslateUi(self, QtHelpDocumentationDialog):
        _translate = QtCore.QCoreApplication.translate
        QtHelpDocumentationDialog.setWindowTitle(_translate("QtHelpDocumentationDialog", "Manage QtHelp Documentation Database"))
        self.label.setText(_translate("QtHelpDocumentationDialog", "Registered Documents"))
        self.documentsList.setSortingEnabled(True)
        self.addButton.setToolTip(_translate("QtHelpDocumentationDialog", "Press to select QtHelp documents to add to the database"))
        self.addButton.setText(_translate("QtHelpDocumentationDialog", "Add..."))
        self.removeButton.setToolTip(_translate("QtHelpDocumentationDialog", "Press to remove the selected documents from the database"))
        self.removeButton.setText(_translate("QtHelpDocumentationDialog", "Remove"))

