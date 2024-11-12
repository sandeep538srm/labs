from django.http import HttpResponse
import os
import datetime
import subprocess

def htop(request):
    name = "Yaram Sandeep Reddy"
    username = os.getlogin()
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput("top -b -n 1 | head -n 10")

    html_content = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return HttpResponse(html_content)
