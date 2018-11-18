from flask import Flask, render_template
from flask_socketio import SocketIO
from random import randint

# init Flask
# Starts the flask invocation
app = Flask(__name__)
socketio = SocketIO(app)
thread = None


#########################################
# basic url routing

@app.route('/')
def hello():
    return '<br> <br> +++ Foyer: Eingangshalle brennt +++ '


#########################################
# simple polling
@app.route('/pull')
def stock_pull():
    v_google = randint(-200, 200)
    v_hotmail = randint(-200, 200)
    v_yahoo = randint(-200, 200)
    v_netflix = randint(-200, 200)
    return render_template('stockPull.html', p_google=v_google,
                           p_hotmail=v_hotmail, p_yahoo=v_yahoo,
                           p_netflix=v_netflix)


#########################################
# websocket

@app.route('/push')
def stock_push():
    return render_template('stockPush.html')


def background_thread():
    print("> Thread is starting...")
    while True:
        print("> Thread is pushing new data..")
        socketio.sleep(2)
        v_google = randint(-200, 200)
        v_hotmail = randint(-200, 200)
        v_yahoo = randint(-200, 200)
        v_netflix = randint(-200, 200)
        socketio.emit('new_data',
                      {'google': v_google, 'hotmail': v_hotmail,
                       'yahoo': v_yahoo, 'netflix': v_netflix})


@socketio.on('connect')
def new_connection():
    print("> New client connection")
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)


if __name__ == '__main__':
    socketio.run(app, debug=True)

"""
    # Default for 'real' Flask Server without socket support
    app.debug = True
    app.run()
    app.run(debug=True)
"""
