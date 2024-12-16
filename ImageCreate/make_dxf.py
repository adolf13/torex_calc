import os

import ezdxf
import sys
import matplotlib.pyplot as plt
from ezdxf import recover
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
import datetime

from ImageCreate.add_entities import insert_dxf_entities
from ImageCreate.scaling import scale_dxf


def file_name():
    """
    Сочиняем имя для DXF и PNG
    :return:
    """
    now = datetime.datetime.now()
    dxf_name = now.strftime("%Y%m%d_%H%M%S.dxf")
    return dxf_name


def dxf_to_jpg(dxf_file) -> str:
    """
    Модуль переводит файл DXF в JPG
    :param dxf_file:
    :return: png filename
    """
    try:
        doc, auditor = recover.readfile(dxf_file)
    except IOError:
        return f'Not a DXF file or a generic I/O error.'
    except ezdxf.DXFStructureError:
        return f'Invalid or corrupted DXF file.'

    jpg_filepath = dxf_file[:-4] + '.png'

    if not auditor.has_errors:
        fig = plt.figure(figsize=(10, 10), facecolor='white')
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_facecolor('white')  # Set axes background to white
        ctx = RenderContext(doc)
        out = MatplotlibBackend(ax)
        Frontend(ctx, out).draw_layout(doc.modelspace(), finalize=True)
        ax.set_axis_off()
        fig.savefig(jpg_filepath, dpi=300, facecolor=fig.get_facecolor())
    return jpg_filepath


def make_dxf(string_for_dxf: dict):
    """
    Модуль создает DXFl, В конце он переводит его в PNG с помощью dxf_to_jpg
    и возвращает имя PNG-файла
    
    Нужно взять базовый DXF для определенной модели и накидать туда блоков
    Блок Основного замка (ручка)
    Блок Дополнительного замка
    Блок задвижки
    Блок Глазка
    Блок Рисунка Нар нкакладки
    Блок рисунка Внутренней накладки
    
    Модуль должен рассчитать точки для вставки блоков и передать его в блок
    Так же модуль должен получить типы этих элементов(анзвания замков, рисунков, глазков)
    """

    peep = string_for_dxf['peep']
    peep_offset = string_for_dxf['peep_offset']
    main_lock = string_for_dxf['main_lock']
    adv_lock = string_for_dxf['adv_lock']
    latch = string_for_dxf['latch']
    side = string_for_dxf['side']
    furniture = string_for_dxf['furniture']
    out_pic = string_for_dxf['out_pic']
    in_pic = string_for_dxf['in_pic']
    width = string_for_dxf['width']
    height = string_for_dxf['height']

    if out_pic == '-' or 'Без рисунка' in out_pic:
        out_pic = False
    if in_pic == '-' or 'Без рисунка' in in_pic:
        in_pic = False

    if adv_lock == 'Без ДопЗамка':
        adv_lock = False
    if latch == 'Без Задвижки':
        latch = False
    if peep == 'Без Глазка':
        peep = False
        peep_offset = False

    now = datetime.datetime.now()

    # Открываем базовый файл
    model = string_for_dxf['series']
    side = string_for_dxf['side']
    dxf_name = os.path.dirname(os.path.abspath(__file__)) + f'\\blocks\\{model}_{side}.dxf'

    doc = ezdxf.readfile(dxf_name)
    msp = doc.modelspace()

    # Какие блоки надо добавить

    # сохраняем
    now = datetime.datetime.now()
    dxf_name = now.strftime("%Y%m%d_%H%M%S.dxf")
    doc.saveas(dxf_name)

    # Out picture
    y = 0
    if out_pic:
        source_dxf = os.path.dirname(os.path.abspath(__file__)) + f'\\blocks\\Pic\\{out_pic}.dxf'
        x = 1083 / 2
        insert_dxf_entities(dxf_name, source_dxf, offset=(x, y, 0))

    # in picture
    if in_pic:
        source_dxf = os.path.dirname(os.path.abspath(__file__)) + f'\\blocks\\Pic\\{in_pic}.dxf'
        x = 1083 + 246 + 1083 / 2
        insert_dxf_entities(dxf_name, source_dxf, offset=(x, y, 0))

    # После наложения рисунка масштабируем:
    x_scale = int(width) / 950
    y_scale = int(height) / 2050
    scaling_dxf = scale_dxf(dxf_name, x_scale, y_scale)

    # Latch ===================================================================================

    source_dxf = os.path.dirname(os.path.abspath(__file__)) + f'\\blocks\\Latch\\{latch}.dxf'
    x = 1083 + 246 + 1083 - 173 if side == 'r' else 1083 + 246 + 173
    insert_dxf_entities(scaling_dxf, source_dxf, offset=(x * x_scale, 1199, 0))
    #  ===================================================================================

    # Furniture ===================================================================================

    # Наружная фурнитура основного замка
    y = 1000
    source_dxf = os.path.dirname(os.path.abspath(__file__)) + f'\\blocks\\Locks\\{furniture}_N_{side}.dxf'
    x = 174 if side == 'r' else 1083 - 174

    insert_dxf_entities(scaling_dxf, source_dxf, offset=(x * x_scale, y, 0))
    # Внутренняя фурнитура основного замка
    x = 1083 + 246 + 1083 - 173 if side == 'r' else 1083 + 246 + 173

    source_dxf = os.path.dirname(os.path.abspath(__file__)) + f'\\blocks\\Locks\\{furniture}_v_{side}.dxf'
    insert_dxf_entities(scaling_dxf, source_dxf, offset=(x * x_scale, y, 0))

    # Наружная фурнитура доп замка
    if adv_lock:
        y = 1353
        source_dxf = os.path.dirname(os.path.abspath(__file__)) + f'\\blocks\\Adv_locks\\{furniture}.dxf'
        # Наружная
        x = 174 if side == 'r' else 1083 - 174
        insert_dxf_entities(scaling_dxf, source_dxf, offset=(x * x_scale, y, 0))
        # Внутренняя фурнитура доп замка
        x = 1083 + 246 + 1083 - 173 if side == 'r' else 1083 + 246 + 173
        insert_dxf_entities(scaling_dxf, source_dxf, offset=(x * x_scale, y, 0))

    #  ===================================================================================
    # Глазок:
    if peep:
        height = 1500
        source_dxf = os.path.dirname(os.path.abspath(__file__)) + f'\\blocks\\Peep\\peep20.dxf'
        if not peep_offset:
            out_x = 1083 / 2
            in_x = 1083 + 246 + 1083 / 2
        else:
            if side == 'r':
                out_x = 174
                in_x = 1083 + 246 + 1083 - 173
            else:
                out_x = 1083 - 174
                in_x = 1083 + 246 + 173
            # out_peep
        insert_dxf_entities(scaling_dxf, source_dxf, offset=(out_x * x_scale, height, 0))
        # in peep
        insert_dxf_entities(scaling_dxf, source_dxf, offset=(in_x * x_scale, height, 0))

    # сохраняем как png
    png_name = dxf_to_jpg(scaling_dxf)  # os.path.dirname(os.path.abspath(__file__)) + f'\\blocks\\{dxf_to_jpg(dxf_name)}'
    print(scaling_dxf, dxf_name, os.path.dirname(os.path.abspath(__file__)))
    os.remove(os.path.dirname(os.path.abspath(__file__))+'\\'+scaling_dxf)
    os.remove(os.path.dirname(os.path.abspath(__file__))+'\\'+dxf_name)
    return png_name


if __name__ == '__main__':
    string = {'series': 'DELTA',
              'model': 'DELTA PRO MP',
              'variant': 'DELTA PRO MP #21',
              'out_pic': 'D25',
              'out_pvh': 'темно-серый букле графит',
              'in_pvh': 'ПВХ Дуб крафт золотой',
              'in_pic': 'D6-25',
              'side': 'r',
              'width': '880',
              'height': '2050',
              'peep': 'G20',
              'peep_offset': False,
              'main_lock': 'Border15',
              'adv_lock': 'Border1',
              'latch': 'Latch',
              'furniture': 'черн квадр'}

    png_name = make_dxf(string)
