from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

pomodoro_minutes = 25
short_break_minutes = 5
long_break_minutes = 15
is_running = False

start_time = 0
end_time = 0
remaining_time = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_timer', methods=['POST'])
def start_timer():
    global is_running, start_time, end_time, remaining_time

    if not is_running:
        start_time = time.time()
        end_time = start_time + (pomodoro_minutes * 60)
        remaining_time = end_time - time.time()
        is_running = True

    return jsonify({'is_running': is_running, 'remaining_time': remaining_time})

@app.route('/stop_timer', methods=['POST'])
def stop_timer():
    global is_running, remaining_time

    if is_running:
        is_running = False
        remaining_time = end_time - time.time()

    return jsonify({'is_running': is_running, 'remaining_time': remaining_time})

if __name__ == '__main__':
    app.run(debug=True)
