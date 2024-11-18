import configparser
import os

from flask import Flask, request, jsonify
import sqlite3
import json

app = Flask(__name__)
ENCODING = "utf-8"


@app.route('/get_door_config', methods=['POST'])
def get_door_config():
    data = request.get_json()
    try:
        data = request.get_json()
        door_type = data.get('type')

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


@app.route('/get_model_list', methods=['GET'])
def get_model_list():
    config_name = str(os.path.dirname(os.path.abspath(__file__))) + '\\config\\main.ini'
    print('HERE', config_name)
    config = configparser.ConfigParser()
    config.read(config_name, encoding=ENCODING)
    model_list = config["main"]["list_models"].split(",")
    print(model_list)
    return jsonify(model_list)


if __name__ == '__main__':
    app.run(debug=True)  # Remember to set debug=False for productio
n
