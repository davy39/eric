# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsMercurial/QueuesExtension/HgQueuesNewPatchDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgQueuesNewPatchDialog(object):
    def setupUi(self, HgQueuesNewPatchDialog):
        HgQueuesNewPatchDialog.setObjectName("HgQueuesNewPatchDialog")
        HgQueuesNewPatchDialog.resize(400, 362)
        HgQueuesNewPatchDialog.setSizeGripEnabled(True)
        self.gridLayout_3 = QtWidgets.QGridLayout(HgQueuesNewPatchDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.nameLabel = QtWidgets.QLabel(HgQueuesNewPatchDialog)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout_3.addWidget(self.nameLabel, 0, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(HgQueuesNewPatchDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout_3.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(HgQueuesNewPatchDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.messageEdit = QtWidgets.QPlainTextEdit(HgQueuesNewPatchDialog)
        self.messageEdit.setTabChangesFocus(True)
        self.messageEdit.setObjectName("messageEdit")
        self.gridLayout_3.addWidget(self.messageEdit, 1, 1, 1, 1)
        self.userGroup = QtWidgets.QGroupBox(HgQueuesNewPatchDialog)
        self.userGroup.setCheckable(True)
        self.userGroup.setChecked(False)
        self.userGroup.setObjectName("userGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.userGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.currentUserCheckBox = QtWidgets.QCheckBox(self.userGroup)
        self.currentUserCheckBox.setObjectName("currentUserCheckBox")
        self.gridLayout.addWidget(self.currentUserCheckBox, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.userGroup)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.userEdit = QtWidgets.QLineEdit(self.userGroup)
        self.userEdit.setObjectName("userEdit")
        self.gridLayout.addWidget(self.userEdit, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.userGroup, 2, 0, 1, 2)
        self.dateGroup = QtWidgets.QGroupBox(HgQueuesNewPatchDialog)
        self.dateGroup.setCheckable(True)
        self.dateGroup.setChecked(False)
        self.dateGroup.setObjectName("dateGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dateGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.currentDateCheckBox = QtWidgets.QCheckBox(self.dateGroup)
        self.currentDateCheckBox.setObjectName("currentDateCheckBox")
        self.gridLayout_2.addWidget(self.currentDateCheckBox, 0, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.dateGroup)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.dateGroup)
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd hh:mm")
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_2.addWidget(self.dateTimeEdit, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(241, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.dateGroup, 3, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgQueuesNewPatchDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 4, 0, 1, 2)

        self.retranslateUi(HgQueuesNewPatchDialog)
        self.buttonBox.accepted.connect(HgQueuesNewPatchDialog.accept)
        self.buttonBox.rejected.connect(HgQueuesNewPatchDialog.reject)
        self.currentUserCheckBox.toggled['bool'].connect(self.userEdit.setDisabled)
        self.currentUserCheckBox.toggled['bool'].connect(self.label_3.setDisabled)
        self.currentDateCheckBox.toggled['bool'].connect(self.label_4.setDisabled)
        self.currentDateCheckBox.toggled['bool'].connect(self.dateTimeEdit.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(HgQueuesNewPatchDialog)
        HgQueuesNewPatchDialog.setTabOrder(self.nameEdit, self.messageEdit)
        HgQueuesNewPatchDialog.setTabOrder(self.messageEdit, self.userGroup)
        HgQueuesNewPatchDialog.setTabOrder(self.userGroup, self.currentUserCheckBox)
        HgQueuesNewPatchDialog.setTabOrder(self.currentUserCheckBox, self.userEdit)
        HgQueuesNewPatchDialog.setTabOrder(self.userEdit, self.dateGroup)
        HgQueuesNewPatchDialog.setTabOrder(self.dateGroup, self.currentDateCheckBox)
        HgQueuesNewPatchDialog.setTabOrder(self.currentDateCheckBox, self.dateTimeEdit)
        HgQueuesNewPatchDialog.setTabOrder(self.dateTimeEdit, self.buttonBox)

    def retranslateUi(self, HgQueuesNewPatchDialog):
        _translate = QtCore.QCoreApplication.translate
        HgQueuesNewPatchDialog.setWindowTitle(_translate("HgQueuesNewPatchDialog", "New Patch"))
        self.nameLabel.setText(_translate("HgQueuesNewPatchDialog", "Name:"))
        self.nameEdit.setToolTip(_translate("HgQueuesNewPatchDialog", "Enter the patch name"))
        self.label_2.setText(_translate("HgQueuesNewPatchDialog", "Message:"))
        self.messageEdit.setToolTip(_translate("HgQueuesNewPatchDialog", "Enter the commit message for the patch"))
        self.userGroup.setToolTip(_translate("HgQueuesNewPatchDialog", "Select to give user information"))
        self.userGroup.setTitle(_translate("HgQueuesNewPatchDialog", "User"))
        self.currentUserCheckBox.setToolTip(_translate("HgQueuesNewPatchDialog", "Select to use the name of the current user"))
        self.currentUserCheckBox.setText(_translate("HgQueuesNewPatchDialog", "Use current user"))
        self.label_3.setText(_translate("HgQueuesNewPatchDialog", "Username:"))
        self.userEdit.setToolTip(_translate("HgQueuesNewPatchDialog", "Enter the user name to be used for the patch"))
        self.dateGroup.setToolTip(_translate("HgQueuesNewPatchDialog", "Select to give date and time information"))
        self.dateGroup.setTitle(_translate("HgQueuesNewPatchDialog", "Date and Time"))
        self.currentDateCheckBox.setToolTip(_translate("HgQueuesNewPatchDialog", "Select to use the current date and time"))
        self.currentDateCheckBox.setText(_translate("HgQueuesNewPatchDialog", "Use current date and time"))
        self.label_4.setText(_translate("HgQueuesNewPatchDialog", "Date/Time:"))
        self.dateTimeEdit.setToolTip(_translate("HgQueuesNewPatchDialog", "Enter the date and time to be used for the patch"))
