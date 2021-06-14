from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/theory')
def theory():
    return render_template('theory.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/MDP')
def mdp():
    return render_template('Markov Decision Process.html')


@app.route('/QL')
def ql():
    return render_template('QLearning.html')


@app.route('/DQL')
def dql():
    return render_template('Deep QLearning.html')


@app.route('/frozen')
def frozen():
    return render_template('FrozenLake Example.html')


@app.route('/CP')
def cp():
    return render_template('CartPole-v1.html')


@app.route('/breakout')
def breakout():
    return render_template('Breakout.html')


@app.route('/AD')
def adriving():
    return render_template('Autonomous Driving.html')


if __name__ == '__main__':
    app.run(debug=True)
