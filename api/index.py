from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello World!</h1>
    <h2>Aplikasi Flask Berhasil di Deploy!</h2>
    <p>Website ini menggunakan Python Flask,
    GitHub, dan Vercel.</p>
    """

if __name__ == "_main_":
    app.run(host="127.0.0.1", port=5000, debug=True)