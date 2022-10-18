import utils
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    candidates = utils.load_candidates_from_json()
    return candidates


@app.route('/candidate/<int:pk>')
def get_candidate(pk):
    pass


@app.route('/candidate/<skill>')
def get_candidates_by_skill(skill):
    pass


@app.route('/search/<candidate_name>')
def get_candidates_by_name(name):
    pass


app.run()
