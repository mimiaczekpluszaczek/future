from flask import Flask, render_template
from flask_frozen import Freezer
from datetime import datetime

future = Flask(__name__)
freezer = Freezer(future)

@future.route('/')
@future.route('/home')
def countdown():
    target_date = datetime(2024, 8, 16,12,8)
    current_date = datetime.now()
    time_remaining = target_date - current_date
    return render_template('countdown.html', time_remaining=time_remaining)

if __name__ == '__main__':
    freezer.freeze()
    future.run(debug=True)
