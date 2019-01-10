from flask import Flask, render_template, request
# import game

app = Flask(__name__, template_folder='templates')



@app.route('/', methods=['GET', 'POST'])
def game():
    # player_input = request.form['player_input']
    name = "Player"
    if request.method == 'POST' and 'name' in request.form:
        name = request.form['name']
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)

