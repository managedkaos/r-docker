from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    process = subprocess.Popen(['Rscript', 'hello.r'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE)
    out, err = process.communicate()
    print(out)
    print(err)
    return out

if __name__ == "__main__" :
    app.run()
