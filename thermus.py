from flask import Flask, request

app = Flask(__name__)

@app.route("/secret")
def secret():
    if request.headers.get('User-Agent') == 'BurpSuite':
        return "FLAG-RAID{SPECIAL-AGENT}"
    else:
        return "Access Denied"

if __name__ == "__main__":
    app.run(debug=True)
