from flask import Flask, render_template
from datetime import datetime

future = Flask(__name__)

@future.route('/')
@future.route('/index')
def countdown():
    target_date = datetime(2024, 8, 16,12,00,00)
    current_date = datetime.now()
    time_remaining = target_date - current_date
    return render_template('countdown.html', time_remaining=time_remaining)

if __name__ == '__main__':
    future.run(debug=True)
