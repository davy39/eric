# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsMercurial/LargefilesExtension/LfRevisionsInputDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LfRevisionsInputDialog(object):
    def setupUi(self, LfRevisionsInputDialog):
        LfRevisionsInputDialog.setObjectName("LfRevisionsInputDialog")
        LfRevisionsInputDialog.resize(400, 300)
        LfRevisionsInputDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(LfRevisionsInputDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(LfRevisionsInputDialog)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.revisionsEdit = QtWidgets.QPlainTextEdit(LfRevisionsInputDialog)
        self.revisionsEdit.setTabChangesFocus(True)
        self.revisionsEdit.setObjectName("revisionsEdit")
        self.verticalLayout.addWidget(self.revisionsEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(LfRevisionsInputDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LfRevisionsInputDialog)
        self.buttonBox.accepted.connect(LfRevisionsInputDialog.accept)
        self.buttonBox.rejected.connect(LfRevisionsInputDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LfRevisionsInputDialog)
        LfRevisionsInputDialog.setTabOrder(self.revisionsEdit, self.buttonBox)

    def retranslateUi(self, LfRevisionsInputDialog):
        _translate = QtCore.QCoreApplication.translate
        LfRevisionsInputDialog.setWindowTitle(_translate("LfRevisionsInputDialog", "Revisions Input"))
        self.label.setText(_translate("LfRevisionsInputDialog", "Enter revisions to pull large files for (one per line):"))
        self.revisionsEdit.setToolTip(_translate("LfRevisionsInputDialog", "Enter changesets by number, id, range or revset expression one per line"))

