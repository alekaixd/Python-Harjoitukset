from flask import Flask

app = Flask(__name__)


@app.route('/alkuluku/<luku>')
def alkuluku(luku):

    isPrime = True

    if int(luku) <= 1:
        isPrime = False
    else:
        for i in range(2, int(int(luku)**0.5) + 1):
            if int(luku) % i == 0:
                isPrime = False
                break

    output = {
        "number": luku,
        "isPrime": isPrime
    }
    return output


if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
