from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def get_home():
    prompts = silly_story.prompts
    print(silly_story.prompts)
    # html = render_template('questions.html')
    return render_template("questions.html", prompts=prompts)


# grab words from the silly_story class -> save it in a variable

# loop over the list

# inject each element to questions.html template as input in the label

@app.get("/results")
def get_result():
    story = silly_story.get_result_text(request.args)

    # print("request.ars", request.args)
    return render_template("results.html",story=story )
# gather the information from the form
