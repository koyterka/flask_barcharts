import flask
from flask import render_template
from table_config import *

app = flask.Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='template')
app.config["DEBUG"] = True

title = 'Voting results'
bar_labels = ['Option A', 'Option B', 'Option C', 'Option D', 'Option E']
bar_values = [967, 1190, 1079, 500, 2500, 660]
background_colors = possible_background_colors[:len(bar_labels)]
border_colors = possible_border_colors[:len(bar_labels)]


@app.route("/results")
def view_resuls():
    return render_template("voting_result.html", title=title,
                           labels=bar_labels, values=bar_values, colors=background_colors, borders=border_colors)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)