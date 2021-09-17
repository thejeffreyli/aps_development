# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple-mask/ui/mask.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1397, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 6, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.btn_editlock = QtWidgets.QPushButton(self.groupBox)
        self.btn_editlock.setObjectName("btn_editlock")
        self.gridLayout_2.addWidget(self.btn_editlock, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 2)
        self.db_ceny = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.db_ceny.setEnabled(False)
        self.db_ceny.setMinimum(-9999.0)
        self.db_ceny.setMaximum(9999.0)
        self.db_ceny.setObjectName("db_ceny")
        self.gridLayout_2.addWidget(self.db_ceny, 3, 2, 1, 1)
        self.db_energy = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.db_energy.setEnabled(False)
        self.db_energy.setObjectName("db_energy")
        self.gridLayout_2.addWidget(self.db_energy, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 7, 0, 1, 2)
        self.db_pix_dim = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.db_pix_dim.setEnabled(False)
        self.db_pix_dim.setDecimals(4)
        self.db_pix_dim.setObjectName("db_pix_dim")
        self.gridLayout_2.addWidget(self.db_pix_dim, 6, 2, 1, 1)
        self.db_det_dist = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.db_det_dist.setEnabled(False)
        self.db_det_dist.setMaximum(99999.0)
        self.db_det_dist.setObjectName("db_det_dist")
        self.gridLayout_2.addWidget(self.db_det_dist, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.db_cenx = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.db_cenx.setEnabled(False)
        self.db_cenx.setMinimum(-9999.0)
        self.db_cenx.setMaximum(9999.0)
        self.db_cenx.setObjectName("db_cenx")
        self.gridLayout_2.addWidget(self.db_cenx, 2, 2, 1, 1)
        self.le_shape = QtWidgets.QLineEdit(self.groupBox)
        self.le_shape.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_shape.sizePolicy().hasHeightForWidth())
        self.le_shape.setSizePolicy(sizePolicy)
        self.le_shape.setObjectName("le_shape")
        self.gridLayout_2.addWidget(self.le_shape, 7, 2, 1, 1)
        self.btn_load = QtWidgets.QPushButton(self.groupBox)
        self.btn_load.setObjectName("btn_load")
        self.gridLayout_2.addWidget(self.btn_load, 1, 0, 1, 1)
        self.fname = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fname.sizePolicy().hasHeightForWidth())
        self.fname.setSizePolicy(sizePolicy)
        self.fname.setReadOnly(True)
        self.fname.setObjectName("fname")
        self.gridLayout_2.addWidget(self.fname, 0, 0, 1, 3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plot_cmap = QtWidgets.QComboBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_cmap.sizePolicy().hasHeightForWidth())
        self.plot_cmap.setSizePolicy(sizePolicy)
        self.plot_cmap.setObjectName("plot_cmap")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.plot_cmap.addItem("")
        self.gridLayout_3.addWidget(self.plot_cmap, 0, 2, 1, 2)
        self.plot_invert = QtWidgets.QCheckBox(self.groupBox_4)
        self.plot_invert.setObjectName("plot_invert")
        self.gridLayout_3.addWidget(self.plot_invert, 2, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.plot_log = QtWidgets.QCheckBox(self.groupBox_4)
        self.plot_log.setChecked(True)
        self.plot_log.setObjectName("plot_log")
        self.gridLayout_3.addWidget(self.plot_log, 2, 2, 1, 2)
        self.plot_rotate = QtWidgets.QCheckBox(self.groupBox_4)
        self.plot_rotate.setObjectName("plot_rotate")
        self.gridLayout_3.addWidget(self.plot_rotate, 3, 0, 1, 1)
        self.plot_center = QtWidgets.QCheckBox(self.groupBox_4)
        self.plot_center.setChecked(True)
        self.plot_center.setObjectName("plot_center")
        self.gridLayout_3.addWidget(self.plot_center, 3, 2, 1, 1)
        self.btn_plot = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_plot.setObjectName("btn_plot")
        self.gridLayout_3.addWidget(self.btn_plot, 4, 2, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cb_selector_type = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_selector_type.setObjectName("cb_selector_type")
        self.cb_selector_type.addItem("")
        self.cb_selector_type.addItem("")
        self.cb_selector_type.addItem("")
        self.cb_selector_type.addItem("")
        self.gridLayout_4.addWidget(self.cb_selector_type, 0, 0, 1, 2)
        self.cb_selector_mode = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_selector_mode.setObjectName("cb_selector_mode")
        self.cb_selector_mode.addItem("")
        self.cb_selector_mode.addItem("")
        self.gridLayout_4.addWidget(self.cb_selector_mode, 0, 2, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)
        self.cb_selector_color = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_selector_color.setObjectName("cb_selector_color")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.cb_selector_color.addItem("")
        self.gridLayout_4.addWidget(self.cb_selector_color, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 1, 2, 1, 1)
        self.plot_width = QtWidgets.QSpinBox(self.groupBox_2)
        self.plot_width.setSpecialValueText("")
        self.plot_width.setMinimum(1)
        self.plot_width.setProperty("value", 3)
        self.plot_width.setObjectName("plot_width")
        self.gridLayout_4.addWidget(self.plot_width, 1, 3, 1, 1)
        self.btn_add_roi = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_add_roi.setObjectName("btn_add_roi")
        self.gridLayout_4.addWidget(self.btn_add_roi, 2, 0, 1, 2)
        self.btn_apply_roi = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_apply_roi.setObjectName("btn_apply_roi")
        self.gridLayout_4.addWidget(self.btn_apply_roi, 2, 2, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.sb_spnum = QtWidgets.QSpinBox(self.groupBox_3)
        self.sb_spnum.setMaximum(9999)
        self.sb_spnum.setProperty("value", 1)
        self.sb_spnum.setObjectName("sb_spnum")
        self.gridLayout_6.addWidget(self.sb_spnum, 2, 1, 1, 1)
        self.btn_compute_qpartition = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_compute_qpartition.setObjectName("btn_compute_qpartition")
        self.gridLayout_6.addWidget(self.btn_compute_qpartition, 4, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 4, 1, 1, 1)
        self.sb_dqnum = QtWidgets.QSpinBox(self.groupBox_3)
        self.sb_dqnum.setProperty("value", 36)
        self.sb_dqnum.setObjectName("sb_dqnum")
        self.gridLayout_6.addWidget(self.sb_dqnum, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.sb_sqnum = QtWidgets.QSpinBox(self.groupBox_3)
        self.sb_sqnum.setMaximum(9999)
        self.sb_sqnum.setProperty("value", 360)
        self.sb_sqnum.setObjectName("sb_sqnum")
        self.gridLayout_6.addWidget(self.sb_sqnum, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 2, 0, 1, 1)
        self.sb_dpnum = QtWidgets.QSpinBox(self.groupBox_3)
        self.sb_dpnum.setMinimum(1)
        self.sb_dpnum.setProperty("value", 1)
        self.sb_dpnum.setObjectName("sb_dpnum")
        self.gridLayout_6.addWidget(self.sb_dpnum, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 3, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName("gridLayout")
        self.plot_index = QtWidgets.QComboBox(self.groupBox_5)
        self.plot_index.setObjectName("plot_index")
        self.plot_index.addItem("")
        self.plot_index.addItem("")
        self.plot_index.addItem("")
        self.plot_index.addItem("")
        self.plot_index.addItem("")
        self.gridLayout.addWidget(self.plot_index, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 1, 1, 1)
        self.infobar = QtWidgets.QLineEdit(self.groupBox_5)
        self.infobar.setObjectName("infobar")
        self.gridLayout.addWidget(self.infobar, 0, 2, 1, 1)
        self.mp1 = ImageViewROI(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mp1.sizePolicy().hasHeightForWidth())
        self.mp1.setSizePolicy(sizePolicy)
        self.mp1.setMinimumSize(QtCore.QSize(600, 0))
        self.mp1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.mp1.setObjectName("mp1")
        self.gridLayout.addWidget(self.mp1, 1, 0, 1, 3)
        self.gridLayout_5.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1397, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.db_cenx, self.db_ceny)
        MainWindow.setTabOrder(self.db_ceny, self.db_energy)
        MainWindow.setTabOrder(self.db_energy, self.db_det_dist)
        MainWindow.setTabOrder(self.db_det_dist, self.db_pix_dim)
        MainWindow.setTabOrder(self.db_pix_dim, self.le_shape)
        MainWindow.setTabOrder(self.le_shape, self.plot_cmap)
        MainWindow.setTabOrder(self.plot_cmap, self.plot_log)
        MainWindow.setTabOrder(self.plot_log, self.plot_invert)
        MainWindow.setTabOrder(self.plot_invert, self.plot_rotate)
        MainWindow.setTabOrder(self.plot_rotate, self.plot_center)
        MainWindow.setTabOrder(self.plot_center, self.btn_plot)
        MainWindow.setTabOrder(self.btn_plot, self.cb_selector_type)
        MainWindow.setTabOrder(self.cb_selector_type, self.cb_selector_mode)
        MainWindow.setTabOrder(self.cb_selector_mode, self.cb_selector_color)
        MainWindow.setTabOrder(self.cb_selector_color, self.plot_width)
        MainWindow.setTabOrder(self.plot_width, self.btn_add_roi)
        MainWindow.setTabOrder(self.btn_add_roi, self.btn_apply_roi)
        MainWindow.setTabOrder(self.btn_apply_roi, self.sb_sqnum)
        MainWindow.setTabOrder(self.sb_sqnum, self.sb_dqnum)
        MainWindow.setTabOrder(self.sb_dqnum, self.sb_spnum)
        MainWindow.setTabOrder(self.sb_spnum, self.sb_dpnum)
        MainWindow.setTabOrder(self.sb_dpnum, self.btn_compute_qpartition)
        MainWindow.setTabOrder(self.btn_compute_qpartition, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.plot_index)
        MainWindow.setTabOrder(self.plot_index, self.infobar)
        MainWindow.setTabOrder(self.infobar, self.fname)
        MainWindow.setTabOrder(self.fname, self.btn_load)
        MainWindow.setTabOrder(self.btn_load, self.btn_editlock)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Input"))
        self.label_6.setText(_translate("MainWindow", "pixel size (mm):"))
        self.label_2.setText(_translate("MainWindow", "center x:"))
        self.btn_editlock.setText(_translate("MainWindow", "edit/lock"))
        self.label_5.setText(_translate("MainWindow", "detor distance (mm):"))
        self.label_4.setText(_translate("MainWindow", "energy (keV):"))
        self.label_7.setText(_translate("MainWindow", "detector shape:"))
        self.label_3.setText(_translate("MainWindow", "center y:"))
        self.btn_load.setText(_translate("MainWindow", "load data"))
        self.fname.setPlaceholderText(_translate("MainWindow", "filename"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Plot"))
        self.plot_cmap.setItemText(0, _translate("MainWindow", "jet"))
        self.plot_cmap.setItemText(1, _translate("MainWindow", "cool"))
        self.plot_cmap.setItemText(2, _translate("MainWindow", "ocean"))
        self.plot_cmap.setItemText(3, _translate("MainWindow", "prism"))
        self.plot_cmap.setItemText(4, _translate("MainWindow", "coolwarm"))
        self.plot_cmap.setItemText(5, _translate("MainWindow", "seismic"))
        self.plot_cmap.setItemText(6, _translate("MainWindow", "gray"))
        self.plot_cmap.setItemText(7, _translate("MainWindow", "viridis"))
        self.plot_cmap.setItemText(8, _translate("MainWindow", "inferno"))
        self.plot_cmap.setItemText(9, _translate("MainWindow", "plasma"))
        self.plot_cmap.setItemText(10, _translate("MainWindow", "magma"))
        self.plot_invert.setText(_translate("MainWindow", "invert"))
        self.label_9.setText(_translate("MainWindow", "cmap:"))
        self.plot_log.setText(_translate("MainWindow", "log scale"))
        self.plot_rotate.setText(_translate("MainWindow", "rotate"))
        self.plot_center.setText(_translate("MainWindow", "show center"))
        self.btn_plot.setText(_translate("MainWindow", "plot"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Mask"))
        self.cb_selector_type.setItemText(0, _translate("MainWindow", "Polygon"))
        self.cb_selector_type.setItemText(1, _translate("MainWindow", "Circle"))
        self.cb_selector_type.setItemText(2, _translate("MainWindow", "Ellipse"))
        self.cb_selector_type.setItemText(3, _translate("MainWindow", "Rectangle"))
        self.cb_selector_mode.setItemText(0, _translate("MainWindow", "exclusive"))
        self.cb_selector_mode.setItemText(1, _translate("MainWindow", "inclusive"))
        self.label_14.setText(_translate("MainWindow", "color:"))
        self.cb_selector_color.setItemText(0, _translate("MainWindow", "green"))
        self.cb_selector_color.setItemText(1, _translate("MainWindow", "yellow"))
        self.cb_selector_color.setItemText(2, _translate("MainWindow", "blue"))
        self.cb_selector_color.setItemText(3, _translate("MainWindow", "red"))
        self.cb_selector_color.setItemText(4, _translate("MainWindow", "cyan"))
        self.cb_selector_color.setItemText(5, _translate("MainWindow", "magenta"))
        self.cb_selector_color.setItemText(6, _translate("MainWindow", "black"))
        self.cb_selector_color.setItemText(7, _translate("MainWindow", "white"))
        self.label_8.setText(_translate("MainWindow", "linewidth:"))
        self.btn_add_roi.setText(_translate("MainWindow", "add roi"))
        self.btn_apply_roi.setText(_translate("MainWindow", "apply roi"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Partition"))
        self.btn_compute_qpartition.setText(_translate("MainWindow", "compute"))
        self.pushButton.setText(_translate("MainWindow", "save"))
        self.label_10.setText(_translate("MainWindow", "dynamic q partition:"))
        self.label.setText(_translate("MainWindow", "static q partition:"))
        self.label_12.setText(_translate("MainWindow", "static phi partition:"))
        self.label_13.setText(_translate("MainWindow", "dynamic phi partition:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Scattering, Mask and Partitions"))
        self.plot_index.setItemText(0, _translate("MainWindow", "scattering"))
        self.plot_index.setItemText(1, _translate("MainWindow", "scattering * mask"))
        self.plot_index.setItemText(2, _translate("MainWindow", "mask"))
        self.plot_index.setItemText(3, _translate("MainWindow", "dynamic_q_partition"))
        self.plot_index.setItemText(4, _translate("MainWindow", "static_q_partition"))
        self.label_11.setText(_translate("MainWindow", "coordinates:"))
from pyqtgraph_mod import ImageViewROI
