from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index(): 
	return render_template("index.html")

texts = ["Cupidatat elit ex magna magna eu duis deserunt excepteur aliqua dolor fugiat commodo.", "Irure id magna eiusmod ad amet. Exercitation ad laboris laborum tempor culpa dolore exercitation sunt do.", "Amet excepteur eu culpa reprehenderit dolor sunt ex ea laborum do anim eu minim incididunt."]

@app.route("/one")
def one():
	return texts[0]

@app.route("/two")
def two():
	return texts[1]

@app.route("/three")
def three():
	return texts[2]

if __name__ == "__main__":
	app.run(debug=True)

