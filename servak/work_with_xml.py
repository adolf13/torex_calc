import os
import xml.etree.ElementTree as ET
import configparser
from typing import Tuple, List, Dict, Union, Any, Optional
from xml.etree.ElementTree import Element


def get_models_list(target_series: str) -> list:
    # Получаем серию, по ней ищем все модели
    xml_file =str(os.path.dirname(os.path.abspath(__file__))) + '\\Assortment-TOREX.xml'

    tree = ET.parse(xml_file)
    root = tree.getroot()
    models = []

    # Проходим по всем элементам Номенклатура
    for nomenclature in root.findall('.//Номенклатура'):
        series = nomenclature.get('Серия')
        model = nomenclature.get('Модель')

        # Проверяем, совпадает ли текущая серия с искомой
        if series == target_series and model:
            models.append(model)
    return models


def get_variants(target_series: str, target_model: str) -> list:
    # Загружаем XML-файл
    xml_file =str(os.path.dirname(os.path.abspath(__file__))) + '\\Assortment-TOREX.xml'
    tree = ET.parse(xml_file)
    root = tree.getroot()
    variants = []

    # Проходим по всем элементам Номенклатура
    for nomenclature in root.findall('.//Номенклатура'):
        if nomenclature.get('Серия') == target_series and nomenclature.get('Модель') == target_model:
            for variant in nomenclature.findall('ВариантИсполнения'):
                unic_sochetanie = variant.get('УникальноеСочетание')
                variants.append(unic_sochetanie)

    return variants


def get_characteristics(target_series: str, target_model: str, target_variant: str):
    # Загружаем XML-файл
    xml_file =str(os.path.dirname(os.path.abspath(__file__))) + '\\Assortment-TOREX.xml'
    tree = ET.parse(xml_file)
    root = tree.getroot()
    characteristics = {}
    char_dict = []

    # ПроNavig по всем элементам Номенклатура
    for nomenclature in root.findall('.//Номенклатура'):
        if nomenclature.get('Серия') == target_series and nomenclature.get('Модель') == target_model:
            for variant in nomenclature.findall('ВариантИсполнения'):
                if variant.get('УникальноеСочетание') == target_variant:
                    options = variant.find('ДополнительныеОпции')
                    options_code = [code_option.text for code_option in options.findall('КодОпции')]

                    for characteristic in variant.findall('Характеристика'):
                        properties = characteristic.get('Свойство')[3:]
                        values = [values.text for values in characteristic.findall('Значение')]
                        characteristics[properties] = values
                    char_dict.append(characteristics)

                    options_list = get_options(options_code)
                    return char_dict[0], options_list


def get_options(option_list: list) -> list:
    xml_file =str(os.path.dirname(os.path.abspath(__file__))) + '\\Assortment-TOREX.xml'
    tree = ET.parse(xml_file)
    root = tree.getroot()
    options = []

    for option in root.findall('.//ДопОпция'):
        if option.get('КодОпции') in option_list:
            options.append(option.get('НаименованиеОпции'))
    return options


def parsing_xml(xml_file):
    # Загружаем XML-файл
    tree = ET.parse(xml_file)
    root = tree.getroot()

    config_name = str(os.path.dirname(os.path.abspath(__file__))) + '\\config\\main.ini'
    config = configparser.ConfigParser()
    config.read(config_name, encoding="utf-8")

    series_list = config['main']['series_list'].split(',')

    # Находим элемент Ассортимент
    assortment = root.find('.//Ассортимент')

    # Проверяем, найден ли элемент Ассортимент
    if assortment is not None:
        # Проходим по всем Номенклатура внутри Ассортимент
        for nomenclature in assortment.findall('Номенклатура'):
            series = nomenclature.get('Серия')
            if series in series_list:
                model = nomenclature.get('Модель')
                print(f' Серия: {series}, модель: {model}')


if __name__ == '__main__':
    # parsing_xml('Assortment-TOREX.xml')
    s, op = get_characteristics("SUPER OMEGA", "S.OMEGA PRO MP", 'S.OMEGA PRO MP #1')
    print(s)
