from msilib.schema import LockPermissions
from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


text = ["Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dignissimos pariatur harum architecto fugit sunt quasi voluptatem iusto placeat, repudiandae, minus cupiditate asperiores exercitationem totam saepe eos ut repellendus veniam! Voluptatibus!"]

@app.route("/one")
def one():
    return texts[0]
