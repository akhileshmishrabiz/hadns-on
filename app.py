from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_docker():
    return '''

            <h1>Hello, World </h1>
            <P>today this is second run at 7 pm and this is automated third code change</P>
            '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')