from flask import Flask

app = Flask(__name__)
@app.route('/stress')
def index():
    count = 0
    for i in range(5000000):
       count= count+1

    return "count is "+str(count)



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=9090)