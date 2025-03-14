from flask import Flask
import os
import subprocess
import datetime
import pytz

app = Flask(_name_)

@app.route('/ihtop')
def ihtop():
    # Full Name
    full_name = "Your Full Name"  # Replace with your name

    # System Username
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown_user"

    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Top Command Output (First 20 Lines)
    top_output = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True).stdout
    top_output = "\n".join(top_output.split("\n")[:20])  # Show only first 20 lines

    # HTML Response
    return f"""
    <html>
    <body>
        <h1>System Info</h1>
        <b>Name:</b> {full_name}<br>
        <b>Username:</b> {username}<br>
        <b>Server Time (IST):</b> {server_time}<br>
        <h2>TOP Output</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)

    # http://YOUR_PUBLIC_IP:5000/ihtop
