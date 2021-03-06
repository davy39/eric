# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Debugger/CallTraceViewer.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CallTraceViewer(object):
    def setupUi(self, CallTraceViewer):
        CallTraceViewer.setObjectName("CallTraceViewer")
        CallTraceViewer.resize(400, 528)
        self.verticalLayout = QtWidgets.QVBoxLayout(CallTraceViewer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startTraceButton = QtWidgets.QToolButton(CallTraceViewer)
        self.startTraceButton.setText("Start")
        self.startTraceButton.setObjectName("startTraceButton")
        self.horizontalLayout.addWidget(self.startTraceButton)
        self.stopTraceButton = QtWidgets.QToolButton(CallTraceViewer)
        self.stopTraceButton.setText("Stop")
        self.stopTraceButton.setObjectName("stopTraceButton")
        self.horizontalLayout.addWidget(self.stopTraceButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.resizeButton = QtWidgets.QToolButton(CallTraceViewer)
        self.resizeButton.setText("Resize")
        self.resizeButton.setObjectName("resizeButton")
        self.horizontalLayout.addWidget(self.resizeButton)
        self.clearButton = QtWidgets.QToolButton(CallTraceViewer)
        self.clearButton.setText("Clear")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.saveButton = QtWidgets.QToolButton(CallTraceViewer)
        self.saveButton.setText("Save")
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.callTrace = QtWidgets.QTreeWidget(CallTraceViewer)
        self.callTrace.setAlternatingRowColors(True)
        self.callTrace.setExpandsOnDoubleClick(False)
        self.callTrace.setObjectName("callTrace")
        self.verticalLayout.addWidget(self.callTrace)

        self.retranslateUi(CallTraceViewer)
        QtCore.QMetaObject.connectSlotsByName(CallTraceViewer)
        CallTraceViewer.setTabOrder(self.startTraceButton, self.stopTraceButton)
        CallTraceViewer.setTabOrder(self.stopTraceButton, self.resizeButton)
        CallTraceViewer.setTabOrder(self.resizeButton, self.clearButton)
        CallTraceViewer.setTabOrder(self.clearButton, self.saveButton)
        CallTraceViewer.setTabOrder(self.saveButton, self.callTrace)

    def retranslateUi(self, CallTraceViewer):
        _translate = QtCore.QCoreApplication.translate
        CallTraceViewer.setWindowTitle(_translate("CallTraceViewer", "Call Trace"))
        self.startTraceButton.setToolTip(_translate("CallTraceViewer", "Press to start tracing calls and returns"))
        self.stopTraceButton.setToolTip(_translate("CallTraceViewer", "Press to stop tracing calls and returns"))
        self.resizeButton.setToolTip(_translate("CallTraceViewer", "Press to resize the columns to their contents"))
        self.clearButton.setToolTip(_translate("CallTraceViewer", "Press to clear the call trace"))
        self.saveButton.setToolTip(_translate("CallTraceViewer", "Press to save the call trace as a text file"))
        self.callTrace.headerItem().setText(1, _translate("CallTraceViewer", "From"))
        self.callTrace.headerItem().setText(2, _translate("CallTraceViewer", "To"))

