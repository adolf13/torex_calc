import requests
import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QApplication, QMessageBox, QCalendarWidget, QDialog, QVBoxLayout, QTimeEdit, QPushButton

from GUI.gui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.date_selected = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        response = requests.get('http://127.0.0.1:5000/get_model_list')


        models = response.json()
        self.ui.nomencloture_combo.addItems(models)

        self.ui.nomencloture_combo.currentTextChanged.connect(self.main_logic)



    def main_logic(self):
        model=self.ui.nomencloture_combo.currentText()
        response = requests.post('http://127.0.0.1:5000/get_door_config', json={'type': model})

        config = response.json()
        max_width=config["size"]["max_width"]
        min_width=config["size"]["min_width"]
        max_height=config["size"]["max_height"]
        min_height=config["size"]["min_height"]

        mainlock_list=config["lock_group"]["mainlock_list"].split(",")
        advlock_list=config["lock_group"]["advlock_list"].split(",")
        latch_list=config["lock_group"]["latch_list"].split(",")

        peep_list=config["peep"]["peep_list"].split(",")
        peep_offset=config["peep"]["peep_offset"]

        out_finish_material=config["out_finish"]["out_finish_material"].split(",")
        out_mdf_thick=config["out_finish"]["out_mdf_thick"].split(",")
        out_metal_paint=config["out_finish"]["out_metal_paint"].split(",")
        out_mdf_pvh=config["out_finish"]["out_mdf_pvh"].split(",")

        in_finish_material=config["in_finish"]["in_finish_material"].split(",")
        in_mdf_thick=config["in_finish"]["in_mdf_thick"].split(",")
        in_metal_paint=config["in_finish"]["in_metal_paint"].split(",")
        in_mdf_pvh=config["in_finish"]["in_mdf_pvh"].split(",")

        print(max_height)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
