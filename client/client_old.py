import requests
import os
import sys
import configparser

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime, QRect, Qt, QProcess
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMessageBox, QCalendarWidget, QDialog, QVBoxLayout, QTimeEdit, QPushButton, \
    QLabel

from GUI.gui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.options_list = None  # Сюда получаем список опций
        self.characteristics_list = None  # Сюда получаем список характеристик
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Скрываем чекбоксы опций
        checkbox_names = [f"option_check_{i}" for i in range(1, 16)]
        for name in checkbox_names:
            getattr(self.ui, name).setHidden(True)

        # CONFIG
        conf = configparser.ConfigParser()
        conf_path = os.path.dirname(os.path.abspath(__file__)) + '\\main.ini'
        conf.read(conf_path, encoding="utf-8-sig")
        #self.url = conf['main']['url']
        #self.url='http://1.1.0.129:5000/'
        self.url='http://127.0.0.1:5000/'

        url = self.url + 'get_series_list'
        response = requests.get(url)
        series = response.json()
        self.ui.series_combo.addItems(series)  # Получили серию

        # Теперь нужно заполнить список Models
        self.ui.series_combo.currentTextChanged.connect(self.show_model_list)

        # Теперь при выборе модели нужно получить список вариантов исполнения для данной модели.
        self.ui.model_combo.currentTextChanged.connect(self.show_variant_list)

        # Теперь при выборе варианта исполнения нужно получить список характеристик.
        self.ui.version_combo.currentTextChanged.connect(self.get_characteristics_list)

        # Теперь при получении харастеристик и опций заполняем поля отделки.
        self.ui.version_combo.currentTextChanged.connect(self.show_out_finish)
        self.ui.version_combo.currentTextChanged.connect(self.show_in_finish)
        self.ui.version_combo.currentTextChanged.connect(self.show_options)

        # кнопка проверки результатов
        self.ui.check_but.clicked.connect(self.text_update)
        self.img_text = False

        # кнопка Эскиз
        self.ui.image_but.clicked.connect(self.show_image)



    def show_image(self):

        url = self.url + "generate_image"

        # Отправляем запрос
        if self.get_all_data():
            data = self.get_all_data()
            options_list = {'options_list': self.get_options()}
            data.update(options_list)

            response = requests.post(url, json=data, stream=True)

            with open("out_pic.jpg", "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):  # Process in chunks
                    f.write(chunk)

            filepath = 'out_pic.jpg'
            pixmap = QPixmap(filepath)
            pixmap = pixmap.scaled(self.ui.img_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.img_label.setPixmap(pixmap)

            # process = QProcess()
            # process.startDetached(filepath)  # startDetached is crucial for not blocking the GUI

        # pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # self.image_label.setPixmap(pixmap)
        #
        # # Show image in a separate window
        # if self.img_window is not None:
        #     self.img_window.close()  # Close existing window if one is open
        # self.img_window = ImageWindow(pixmap)
        # self.img_window.show()

    def show_model_list(self):
        # Получаем от сервера список моделей для данной серии
        self.ui.model_combo.clear()
        series = self.ui.series_combo.currentText()
        response = requests.post(url=self.url + '/get_model_list', json={'series': series})
        models_list = response.json()
        self.ui.model_combo.addItems(models_list)

    def show_variant_list(self):
        # Получаем от сервера список вариантов исполнения для данной модели

        self.ui.version_combo.clear()
        series = self.ui.series_combo.currentText()
        model = self.ui.model_combo.currentText()
        response = requests.post(url=self.url + 'get_variant_list', json={'series': series, 'model': model})
        variant_list = response.json()
        self.ui.version_combo.addItems(variant_list)

    def get_characteristics_list(self):
        """
        Здесь получаем список характеристик и допопций
        :return:
        """
        # Получаем от сервера список характеристик для данной варианта исполнения
        series = self.ui.series_combo.currentText()
        model = self.ui.model_combo.currentText()
        variant = self.ui.version_combo.currentText()

        if series and model and variant:
            response = requests.post(url=self.url + 'get_characteristics', json={'series': series,
                                                                                 'model': model,
                                                                                 'variant': variant})
            # Получили список характеристик
            self.characteristics_list, self.options_list = response.json()

    def show_out_finish(self):
        self.ui.out_pic.clear()
        self.ui.out_pvh.clear()

        if self.characteristics_list:
            out_pic_list = self.characteristics_list['Лицо (рисунок)']
            self.ui.out_pic.addItems(out_pic_list)
            out_pvh_list = self.characteristics_list['Лицо (цвет)']
            self.ui.out_pvh.addItems(out_pvh_list)

    def show_in_finish(self):
        self.ui.in_pic.clear()
        self.ui.in_pvh.clear()
        if self.characteristics_list:
            in_pic_list = self.characteristics_list['Внутр. отделка (рисунок)']
            self.ui.in_pic.addItems(in_pic_list)
            in_pvh_list = self.characteristics_list['Внутр. отделка (цвет)']
            self.ui.in_pvh.addItems(in_pvh_list)

    def show_options(self):
        # Показываем опции
        checkbox_names = [f"option_check_{i}" for i in range(1, 16)]
        for name in checkbox_names:
            getattr(self.ui, name).setHidden(True)
            getattr(self.ui, name).setText('')
            getattr(self.ui, name).setChecked(False)

        if self.options_list:
            checkbox_names = [f"option_check_{i}" for i in range(1, len(self.options_list) + 1)]
            for count, name in enumerate(checkbox_names):
                getattr(self.ui, name).setHidden(False)
                getattr(self.ui, name).setText(self.options_list[count])

    def text_update(self):
        text_dict = self.get_all_data()
        text = f'Серия: {text_dict["series"]}\n' \
               f'Модель: {text_dict["model"]}\n' \
               f'Ширина: {text_dict["width"]}\n' \
               f'Высота: {text_dict["height"]}\n' \
               f'Рисунок лицо: {text_dict["out_pic"]}\n' \
               f'Цвет лицо: {text_dict["out_pvh"]}\n' \
               f'Рисунок внутр: {text_dict["in_pic"]}\n' \
               f'Цвет внутр: {text_dict["in_pvh"]}\n'

        options = self.get_options()
        for option in options:
            text += f'{option}\n'

        if text_dict['width'].isdigit() and text_dict['height'].isdigit():
            self.ui.text_info.setText(text)
            self.img_text = text
        else:
            self.ui.text_info.setText('')
            self.img_text = False

    def get_options(self):
        self.options_list = []
        checkbox_names = [f"option_check_{i}" for i in range(1, 16)]
        for name in checkbox_names:
            check = getattr(self.ui, name).isChecked()
            if check:
                self.options_list.append(getattr(self.ui, name).text())
        return self.options_list

    def get_all_data(self):
        series = self.ui.series_combo.currentText()
        model = self.ui.model_combo.currentText()
        variant = self.ui.version_combo.currentText()
        out_pic = self.ui.out_pic.currentText()
        out_pvh = self.ui.out_pvh.currentText()
        in_pvh = self.ui.in_pvh.currentText()
        in_pic = self.ui.in_pic.currentText()
        width = self.check_width()
        height = self.check_height()

        return_dict = {'series': series,
                       'model': model,
                       'variant': variant,
                       'out_pic': out_pic,
                       'out_pvh': out_pvh,
                       'in_pvh': in_pvh,
                       'in_pic': in_pic,
                       'width': str(width),
                       'height': str(height)}

        return return_dict

    def check_width(self):
        width = self.ui.width_inp.text()
        try:
            width = int(width)
        except ValueError:
            self.show_msg('Ширина должна быть числом')
            return

        max_width = int(self.characteristics_list['Ширина'][-1])
        min_width = int(self.characteristics_list['Ширина'][0])
        if width > max_width:
            self.show_msg(f'Ширина не может быть больше {max_width}')
            return
        elif width < min_width:
            self.show_msg(f'Ширина не может быть меньше {min_width}')
            return
        return width

    def check_height(self):
        height = self.ui.height_inp.text()

        try:
            height = int(height)
        except ValueError:
            self.show_msg('Высота должна быть числом')
            return

        max_height = int(self.characteristics_list['Высота'][-1])
        min_height = int(self.characteristics_list['Высота'][0])
        if height > max_height:
            self.show_msg(f'Высота не может быть больше максимальной {max_height}')
            return
        elif height < min_height:
            self.show_msg(f'Высота не может быть меньше минимальной {min_height}')
            return
        return height

    def show_msg(self, msg):
        QMessageBox.critical(self, "Ошибка", msg, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
