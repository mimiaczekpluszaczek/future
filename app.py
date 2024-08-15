from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def countdown():
    target_date = datetime(2024, 12, 31)  # Ustaw tutaj datę docelową
    current_date = datetime.now()
    time_remaining = target_date - current_date
    return render_template('countdown.html', time_remaining=time_remaining)

if __name__ == '__main__':
    app.run(debug=True)
