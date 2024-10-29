import json
from flask import Flask, jsonify

app = Flask(__name__)

from flask_cors import CORS

# Allow CORS for all routes and specify the origin
CORS(app, origins="http://localhost:5173")

class GameState:
    def __init__(self):
        self.player_1_cards
        self.players = []
        self.turn = 0
        self.current_player = None
        self.current_card = None
        self.current_card_index = None
        self.current_card_owner = None



@app.route('/send-image/<string:json_filename>', methods=['GET'])
def send_image(json_filename):

    # Construct the JSON file path
    json_file = f'./cards/evin_deck/{json_filename}'  # Assuming the JSON file is named with the parameter
    
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    return jsonify(data)


if __name__ == '__main__':

    # print(send_image('cards/alice'))

    app.run(debug=True)