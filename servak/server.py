import configparser
import os
from flask import Flask, request, jsonify, send_file
import sqlite3
import json

# os.environ['HTTP_PROXY'] = 'http://1.1.1.40:3128'
# os.environ['HTTPS_PROXY'] = 'http://1.1.1.40:3128'


from work_with_xml import *

app = Flask(__name__)
ENCODING = "utf-8"


@app.route('/get_door_config', methods=['POST'])
def get_door_config():
    try:
        data = request.get_json()
        door_type = data.get('series')

        config_name = str(os.path.dirname(os.path.abspath(__file__))) + '\\config\\' + door_type + '.ini'

        try:
            config = configparser.ConfigParser()
            config.read(config_name, encoding=ENCODING)

            # Convert the configparser object to a dictionary for easier JSON serialization
            config_dict = {}
            for section in config.sections():
                config_dict[section] = dict(config.items(section))

            return jsonify(config_dict)
        except configparser.Error as e:
            return jsonify({'error': f'Error parsing INI file for "{door_type}": {str(e)}'}), 500
        except Exception as e:
            return jsonify({'error': f'An error occurred: {str(e)}'}), 500


    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/out_finish', methods=['POST'])
def out_finish():
    try:
        data = request.get_json()
        door_type = data.get('door_type')
        out_finish = data.get('out_finish')

        config_name = str(os.path.dirname(os.path.abspath(__file__))) + '\\config\\' + door_type + '.ini'

        try:
            config = configparser.ConfigParser()
            config.read(config_name, encoding=ENCODING)

            if out_finish == 'Металл':
                out_color_list = config['out_finish']['out_metal_paint']
                config_dict = {'out_color_list': out_color_list}

            elif out_finish == 'МДФ':
                out_mdf_thick_list = config['out_finish']['out_mdf_thick']
                out_mdf_pvh = config['out_finish']['out_mdf_pvh']
                out_mdf_paint = config['out_finish']['out_mdf_paint']
                out_pic = config['out_finish']['out_pic']
                config_dict = {'out_mdf_thick_list': out_mdf_thick_list,
                               'out_mdf_pvh': out_mdf_pvh,
                               'out_mdf_paint': out_mdf_paint,
                               'out_pic': out_pic}


            elif out_finish == 'Фанера':
                out_mdf_paint = config['out_finish']['out_fanera_paint']
                out_pic = config['out_finish']['out_pic']
                config_dict = {'out_mdf_paint': out_mdf_paint,
                               'out_pic': out_pic}

            else:
                print('Не у далось распознать лицевую отделку!')
                config_dict = False

            return jsonify(config_dict)
        except configparser.Error as e:
            return jsonify({'error': f'Error parsing INI file for "{door_type}": {str(e)}'}), 500
        except Exception as e:
            return jsonify({'error': f'An error occurred: {str(e)}'}), 500


    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/in_finish', methods=['POST'])
def in_finish():
    try:
        data = request.get_json()
        door_type = data.get('door_type')
        in_finish = data.get('in_finish')

        config_name = str(os.path.dirname(os.path.abspath(__file__))) + '\\config\\' + door_type + '.ini'

        try:
            config = configparser.ConfigParser()
            config.read(config_name, encoding=ENCODING)

            if in_finish == 'Металл':
                in_color_list = config['in_finish']['in_metal_paint']
                config_dict = {'in_color_list': in_color_list}

            elif in_finish == 'МДФ':
                in_mdf_thick_list = config['in_finish']['in_mdf_thick']
                in_mdf_pvh = config['in_finish']['in_mdf_pvh']
                in_mdf_paint = config['in_finish']['in_mdf_paint']
                in_pic = config['in_finish']['in_pic']
                config_dict = {'in_mdf_thick_list': in_mdf_thick_list,
                               'in_mdf_pvh': in_mdf_pvh,
                               'in_mdf_paint': in_mdf_paint,
                               'in_pic': in_pic}

            elif in_finish == 'Фанера':
                in_fanera_paint = config['in_finish']['in_fanera_paint']
                in_pic = config['in_finish']['in_pic']
                config_dict = {'in_fanera_paint': in_fanera_paint,
                               'in_pic': in_pic}

            else:
                print('Не у далось распознать лицевую отделку!')
                config_dict = False

            return jsonify(config_dict)
        except configparser.Error as e:
            return jsonify({'error': f'Error parsing INI file for "{door_type}": {str(e)}'}), 500
        except Exception as e:
            return jsonify({'error': f'An error occurred: {str(e)}'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/get_series_list', methods=['GET'])
def get_series_list():
    config_name = str(os.path.dirname(os.path.abspath(__file__))) + '\\config\\main.ini'
    config = configparser.ConfigParser()
    config.read(config_name, encoding=ENCODING)
    series_list = config["main"]["series_list"].split(",")
    return jsonify(series_list)


@app.route('/generate_image', methods=['POST'])
def generate_and_send_image():
    from ImageCreate.make_dxf import make_dxf
    data = request.get_json()
    png_file = make_dxf(data)  # Класс обрабатывает строку, создает дхф
    return send_file(png_file, mimetype='image/jpeg')


@app.route('/get_model_list', methods=['POST'])
def get_model_list():
    data = request.get_json()
    series = data.get('series')
    model_list = get_models_list(series)
    return jsonify(model_list)


@app.route('/get_model_config', methods=['POST'])
def get_model_config():
    data = request.get_json()
    series = data.get('series')


@app.route('/get_variant_list', methods=['POST'])
def get_variant_list():
    data = request.get_json()
    series = data.get('series')
    model = data.get('model')
    variant_list = get_variants(series, model)
    return jsonify(variant_list)


@app.route('/get_characteristics', methods=['POST'])
def get_characteristics_list():
    data = request.get_json()
    series = data.get('series')
    model = data.get('model')
    variant = data.get('variant')
    characteristics_list, options_list = get_characteristics(series, model, variant)

    return jsonify(characteristics_list, options_list)


if __name__ == '__main__':
    app.run(debug=True)  # Remember to set debug=False for production
