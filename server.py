from flask import Flask
from flask_cors import CORS
from flask import render_template
import lxml

from engine.routes.matcher import bp as MATCHER_BP
from engine.routes.setting import bp as SYSTEM_BP
from engine.utils.common import build_json, API_OK


app = Flask(__name__, static_url_path="/assets", static_folder="assets")
app.config["SECRET_KEY"] = "whatisit?"

CORS(app)


@app.route("/")
def index():
    return build_json(API_OK, {"server-alive": True})


@app.route("/client")
def s():
    return render_template("index.html")


app.register_blueprint(MATCHER_BP)
app.register_blueprint(SYSTEM_BP)


app.run(debug=False, port="57621", host="0.0.0.0")
