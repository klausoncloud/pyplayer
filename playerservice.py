import sys, traceback, json, logging

from playerinterface import Move
from playerinterface import do_error


from flask import request
from flask_api import FlaskAPI
from flask_api import status

app = FlaskAPI(__name__)

player_file = "player"
player_file_ext = ".py"

def getIntQueryParam(name):
    parm_str = request.args.get(name, '')
    return int(parm_str)

def logException(err, tb, message):
    logging.error(message + ": {0}".format(err))
    formatted_lines = tb.splitlines()
    for line in formatted_lines:
        logging.error(line)

@app.route('/isRunning', methods = ['GET'])
def is_running():
    return "True", status.HTTP_200_OK

@app.route('/startGame', methods = ['GET'])
def start_game():
    try:
        boardCols = getIntQueryParam('boardX')
        boardRows = getIntQueryParam('boardY')
        numPlayers = getIntQueryParam('numPlayers')
        playerId = getIntQueryParam('playerId')
        """ToDo: Handle incorrect calls gracefully. """

        global player_mod
        global player

        player_mod = __import__(player_file)
        player = player_mod.Player()
    
        r = player.start_game(boardCols, boardRows, numPlayers, playerId).marshal()
        print(json.dumps(r))
        return json.dumps(r)

    except Exception as err:
        tb = traceback.format_exc()
        r = do_error(tb).marshal()

        logException(err, tb, "Exeption in start_game")
        return json.dumps(r)

@app.route('/nextMove', methods = ['GET'])
def next_move():
    try:
        global player
        r = player.next_move().marshal()

        return json.dumps(r)

    except Exception as err:
        tb = traceback.format_exc()
        r = do_error(tb).marshal()

        logException(err, tb, "Exeption in next_move")
        return json.dumps(r)

@app.route('/setCode', methods = ['POST'])
def set_code():
    try:
        with open(player_file + player_file_ext, 'w') as f:
            code = str(request.data.get('code', ''))
            print(code)
            f.write(code);

        print("Wrote file")
        return "Code set.", status.HTTP_200_OK

    except Exception as err:
        tb = traceback.format_exc()
        logException(err, tb, "Exeption in set_code")
        return "Exception in setCode", status.HTTP_500_INTERNAL_SERVER_ERROR

@app.route('/moveNotification', methods=['POST'])
def move_notification():
    return 'NOP'

@app.route('/endOfGame', methods=['POST'])
def end_game():
    return 'NOP'

if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=80)