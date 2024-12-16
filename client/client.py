import sys
import subprocess

import requests
import os
import sys
import configparser
import shutil
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime, QRect, Qt, QProcess
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMessageBox, QCalendarWidget, QDialog, QVBoxLayout, QTimeEdit, QPushButton, \
    QLabel
from requests import RequestException

# os.environ['HTTP_PROXY'] = 'http://1.1.1.40:3128'
# os.environ['HTTPS_PROXY'] = 'http://1.1.1.40:3128'


from GUI.gui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_path = None  # сгенерированный файл картинка
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
        self.url = conf['main']['url']

        # Теперь нужно заполнить список Series
        url = self.url + 'get_series_list'
        response = requests.get(url)
        series = response.json()
        self.ui.series_combo.addItems(series)  # Получили серию

        # Теперь нужно заполнить список Models и получить конфиг на эту серию
        self.ui.series_combo.currentTextChanged.connect(self.show_model_list)
        # Сразу получаем конфиг на серию и показываем оновные опции
        self.ui.series_combo.currentTextChanged.connect(self.show_main_options)

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

        # кнопка PDF
        self.ui.pdf.clicked.connect(self.pdf_render)

        # CONFIG

    def show_out_finish(self):
        if self.characteristics_list:
            self.ui.out_pic.addItems(self.characteristics_list['Лицо (рисунок)'])
            self.ui.out_pvh.addItems(self.characteristics_list['Лицо (цвет)'])

    def show_in_finish(self):
        if self.characteristics_list:
            self.ui.in_pic.addItems(self.characteristics_list['Внутр. отделка (рисунок)'])
            self.ui.in_pvh.addItems(self.characteristics_list['Внутр. отделка (цвет)'])

    def show_image(self):

        url = "http://127.0.0.1:5000/generate_image"
        # Отправляем запрос
        if self.get_all_data():
            data = self.get_all_data()
            options_list = {'options_list': self.get_options()}
            data.update(options_list)

            response = requests.post(url, json=data, stream=True)

            with open("out_pic.jpg", "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):  # Process in chunks
                    f.write(chunk)

            self.image_path = 'out_pic.jpg'
            pixmap = QPixmap(self.image_path)
            pixmap = pixmap.scaled(self.ui.img_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.img_label.setPixmap(pixmap)

    def pdf_render(self):
        # Действуем так: отправляем на сервер картинку и описание(опции) 4 строки
        # и получаем от сервера pdf файл. Открываем папку с ним

        # формируем строки с опциями
        str1 = f'{self.ui.model_combo.currentText()} {self.ui.width_inp.text()} X {self.ui.height_inp.text()} '
        if self.ui.adv_lock.currentText().find('Без ДопЗамка') >= 0:
            str1 = str1 + 'Без ДопЗамка'
        if self.ui.latch.currentText().find('Без Задвижки') >= 0:
            str1 = str1 + 'Без Задвижки'
        if self.ui.peep.currentText().find('Без Глазка') >= 0:
            str1 = str1 + 'Без Глазка'
        if self.ui.peep_offset.isChecked():
            str1 = str1 + 'Глазок сбоку'
        #
        str2 = f'Лицевая отделка - {self.ui.out_pic.currentText()} ({self.ui.out_pvh.currentText()})'
        #
        str3 = f'Внутренняя отделка - {self.ui.in_pic.currentText()} ({self.ui.in_pvh.currentText()})'
        #
        str4 = f'Наличники -'
        #
        str5 = f'Фурнитура - {self.ui.furniture.currentText()}'
        #
        str6 = f'Цвет металла - '
        top_text = [str1, str2, str3, str4, str5, str6]

        if self.image_path:
            png_to_pdf_with_images_and_text(top_text)
            shutil.copy("out_pdf.pdf","PDF/out_pdf.pdf")

            cmd = 'explorer'
            pdf_path = os.path.abspath("PDF/out_pdf.pdf")
            subprocess.call([cmd, pdf_path])

    def show_main_options(self):
        # Показываем основные опции из конфига

        self.ui.peep.addItems(self.config['peep']['peep_list'].split(','))
        self.ui.main_lock.addItems(self.config['lock_group']['mainlock_list'].split(','))
        self.ui.adv_lock.addItems(self.config['lock_group']['advlock_list'].split(','))
        self.ui.latch.addItems(self.config['lock_group']['latch_list'].split(','))
        self.ui.furniture.addItems(self.config['furniture']['furniture_list'].split(','))

    def show_model_list(self):
        # Получаем от сервера список моделей для данной серии
        self.ui.model_combo.clear()
        series = self.ui.series_combo.currentText()
        url = 'http://127.0.0.1:5000/get_model_list'
        response = requests.post(url, json={'series': series})
        models_list = response.json()
        self.ui.model_combo.addItems(models_list)

        # Получаем конфиг на данную серию
        url = 'http://127.0.0.1:5000/get_door_config'
        response = requests.post(url, json={'series': series})
        self.config = response.json()

    def show_variant_list(self):
        # Получаем от сервера список вариантов исполнения для данной модели
        url = 'http://127.0.0.1:5000/get_variant_list'
        self.ui.version_combo.clear()
        series = self.ui.series_combo.currentText()
        model = self.ui.model_combo.currentText()
        response = requests.post(url, json={'series': series, 'model': model})
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

        url = 'http://127.0.0.1:5000/get_characteristics'
        if series and model and variant:
            response = requests.post(url, json={'series': series, 'model': model, 'variant': variant})
            # Получили список характеристик
            self.characteristics_list, self.options_list = response.json()

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

    def side_check(self):
        if self.ui.r_side.isChecked():
            return 'r'
        else:
            return 'l'

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
        side = self.side_check()

        return_dict = {'series': series,
                       'model': model,
                       'variant': variant,
                       'out_pic': out_pic,
                       'out_pvh': out_pvh,
                       'in_pvh': in_pvh,
                       'in_pic': in_pic,
                       'side': side,
                       'width': str(width),
                       'height': str(height),
                       'peep': self.ui.peep.currentText(),
                       'peep_offset': self.ui.peep_offset.isChecked(),
                       'main_lock': self.ui.main_lock.currentText(),
                       'adv_lock': self.ui.adv_lock.currentText(),
                       'latch': self.ui.latch.currentText(),
                       'furniture': self.ui.furniture.currentText()
                       }

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


from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch, mm
from reportlab.lib.utils import ImageReader
import os


def png_to_pdf_with_images_and_text(top_text):
    """
    Adds images and multiline text to a PNG and converts to PDF.  Handles scaling and placement.

    Args:
        png_filepath: Path to input PNG.
        pdf_filepath: Path to output PDF.
        top_text: Multiline text for top (list of strings).
        bottom_text: Multiline text for bottom (list of strings).
        torex_filepath: Path to the image to add to the top left.
        font_size: Font size.
        pagesize: ReportLab pagesize.
    """
    pagesize = A4
    pdf_filepath = 'out_pdf.pdf'
    png_filepath = 'out_pic.jpg'
    bottom_text = ["Подпись заказчика        ______________________________", ""]
    torex_filepath = "torex.jpg"
    font_size = 40
    try:
        img = Image.open(png_filepath)
        img_width, img_height = img.size

        try:
            font = ImageFont.truetype("CeraPro-Light.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()
            print("Warning: Arial font not found. Using default font.")

        text_height_per_line = 35  # font.getsize("A")[1]
        top_text_height = len(top_text) * text_height_per_line + 5
        bottom_text_height = len(bottom_text) * text_height_per_line + 5
        total_text_height = top_text_height + bottom_text_height

        # Load and resize the torex image (adjust max_size as needed)
        torex_img = Image.open(torex_filepath)
        max_size = (400, 400)  # Adjust the maximum size of the torex image
        torex_img.thumbnail(max_size)

        # Create a new image with space for all elements
        new_width = img_width + torex_img.width + 10  # 10px spacing
        new_height = max(img_height + total_text_height, torex_img.height + top_text_height + bottom_text_height)
        new_img = Image.new("RGB", (new_width, new_height), "white")

        # Paste torex image
        new_img.paste(torex_img, (1600, -20))  # 10px padding

        # Paste the main image
        new_img.paste(img, (torex_img.width, top_text_height))  # 20px padding

        draw = ImageDraw.Draw(new_img)

        # Draw top text
        y_offset = 0
        for line in top_text:
            draw.text((torex_img.width, y_offset), line, font=font, fill="black")  # Add padding
            y_offset += text_height_per_line

        # Draw bottom text
        y_offset = top_text_height + img_height
        for line in bottom_text:
            draw.text((torex_img.width, y_offset + 30), line, font=font, fill="black")  # Add padding
            y_offset += text_height_per_line

        new_img.save("temp_image.png")

        page_width, page_height = pagesize
        aspect_ratio = img_width / img_height
        scaled_width = min(page_width, new_width)
        scaled_height = scaled_width * new_height / new_width

        c = canvas.Canvas(pdf_filepath, pagesize=pagesize)
        c.drawImage(ImageReader("temp_image.png"), (page_width - scaled_width) / 2 - 70,
                    (page_height - scaled_height) / 2 + 100, width=scaled_width, height=scaled_height)
        c.save()

        print(f"Successfully converted '{png_filepath}' to '{pdf_filepath}' with added images and text.")
        # Clean up temporary image
        os.remove("temp_image.png")

    except FileNotFoundError:
        print(f"Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    # top_lines = ["Delta PRO PP 950x2050 в наклад, без доп. замка",
    #              "Наружная отделка - МДФ 10 мм ПВХ Оскуро",
    #              "Внутренняя отделка - МДФ 10 мм ПВХ Оскуро.",
    #              "Наличники -НУ1 Оскуро",
    #              "Фурнитура черный квадрат",
    #              "Цвет металла - Черный графит"]
    # torex_image = "torex.jpg"
    # bottom_lines = ["Подпись заказчика        ______________________________", ""]
    # png_to_pdf_with_images_and_text(top_lines)
