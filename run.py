import subprocess
import time

def execute_scripts():
    # Start flask_spam_class.py in the background
    flask_process = subprocess.Popen(['python', 'flask_spam_class.py'])
    # Wait for 10 seconds
    time.sleep(10)
    # Execute tg.py
    subprocess.run(['python', 'tg.py'])
    # Optionally, you can stop the flask_spam_class.py process after executing tg.py
    flask_process.terminate()

if __name__ == '__main__':
    execute_scripts()

