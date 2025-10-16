import logging
from flask import Flask

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def home():
    logging.info("Home route was accessed.")
    return "Log Analyzer app is running."

@app.route('/error')
def error_route():
    try:
        result = 1/0
    except Exception:
        logging.error("An error was triggered in the /error route.", exc_info=True)
        return ("An internal error occurred", 500)


if __name__ == "__main__":
    app.run(debug=True)
