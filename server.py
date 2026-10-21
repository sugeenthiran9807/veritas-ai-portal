"""
VERITAS — AI Content Verification & Authenticity Platform
Web Server & Servlet Emulator (Simulates Apache Tomcat 10 & Jakarta EE)
Laboratory Code: 9807 / Course: CCS375 Web Technologies Lab
"""

import http.server
import socketserver
import urllib.parse
import json
import os
import sys
from datetime import datetime

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class VeritasServerHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query = urllib.parse.parse_qs(parsed_url.query)

        # Route 1: Simulate marklist.jsp query (Ex 6B)
        if path == '/marklist.jsp':
            regno = query.get('regno', [''])[0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            # Simple JSP emulation output
            students = {
                '9807': ('SUGEENTHIRAN', '5 / 5', 'PASS'),
                '9947': ('M. MOHAMED ZAID', '5 / 5', 'PASS'),
                '9948': ('ROOH', '5 / 5', 'PASS'),
                '9949': ('NOOR', '4 / 5', 'PASS'),
                '9950': ('AIRA', '3 / 5', 'PASS'),
                '9951': ('MEER', '5 / 5', 'PASS'),
                '9952': ('AYAN', '2 / 5', 'FAIL'),
                '9087654321': ('Riya Sharma', '5 / 5', 'PASS')
            }
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Student Examination Mark List</title>
                <style>
                    body {{ font-family: Arial; background-color: #eef5ff; text-align: center; padding: 40px; }}
                    .container {{ width: 600px; margin: auto; background-color: white; padding: 30px; border-radius: 15px; box-shadow: 0px 5px 15px #999999; }}
                    h1 {{ color: #2c3e50; }}
                    table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
                    th {{ background-color: #2c3e50; color: white; padding: 12px; text-align: left; }}
                    td {{ padding: 12px; border: 1px solid #999999; text-align: left; }}
                </style>
            </head>
            <body>
            <div class="container">
                <h1>AI CONTENT VERIFICATION SYSTEM</h1>
                <h2>STUDENT EXAMINATION MARK LIST</h2>
            """
            if regno in students:
                name, score, result = students[regno]
                html += f"""
                <table>
                    <tr><th>Student Name</th><td>{name}</td></tr>
                    <tr><th>Register Number</th><td>{regno}</td></tr>
                    <tr><th>Marks</th><td>{score}</td></tr>
                    <tr><th>Result</th><td style="color:{'#059669' if result=='PASS' else '#dc2626'}; font-weight:bold;">{result}</td></tr>
                </table>
                """
            else:
                html += f"<h2>Student examination details not found for Register Number: {regno}</h2>"
            
            html += """
                <br>
                <a href="marklist.html">Back to Marklist</a> | <a href="index.html">Main Portal</a>
            </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
            return

        # Route 1B: Simulate SessionTracking (Ex 5B)
        if path == '/SessionTracking':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            now_str = datetime.now().strftime("%a %b %d %H:%M:%S IST %Y")
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>AI Content Verification - Session Tracking</title>
                <style>
                    body {{ font-family: Arial; background-color: #eef5ff; text-align: center; padding: 30px; }}
                    table {{ border-collapse: collapse; margin: 20px auto; background: white; }}
                    th {{ background: #2c3e50; color: white; padding: 12px 20px; }}
                    td {{ border: 1px solid #ddd; padding: 10px 20px; text-align: left; }}
                    button {{ background: #2c3e50; color: white; padding: 10px 20px; border: none; border-radius: 6px; cursor: pointer; }}
                </style>
            </head>
            <body>
                <h1>Welcome Back to AI Content Verification</h1>
                <h2>Session Information</h2>
                <table>
                    <tr><th>Session Information</th><th>Value</th></tr>
                    <tr><td>Session ID</td><td>F5A7B4C9D0E1F2A3B4C5D6E7F8A9B0C1</td></tr>
                    <tr><td>Creation Time</td><td>{now_str}</td></tr>
                    <tr><td>Time of Last Access</td><td>{now_str}</td></tr>
                    <tr><td>User ID</td><td>AI Content Auditor</td></tr>
                    <tr><td>Number of Visits</td><td>1</td></tr>
                </table>
                <br>
                <button onclick="location.reload()">Visit Again</button>
                <br><br>
                <a href="index.html">← Back to Veritas Portal</a>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
            return

        # Route 1C: Simulate exam servlet (Ex 6A)
        if path == '/exam':
            name = query.get('name', ['Candidate'])[0]
            regno = query.get('regno', ['9807'])[0]
            self.send_response(302)
            self.send_header('Location', f'/exam.html?name={urllib.parse.quote(name)}&regno={urllib.parse.quote(regno)}')
            self.end_headers()
            return

        # Default static file handling
        return super().do_GET()

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        content_length = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_length).decode('utf-8')
        post_data = urllib.parse.parse_qs(post_body)

        # Route 2: Simulate AIContentVerifyServlet (Ex 5A)
        if path == '/AIContentVerifyServlet':
            username = post_data.get('username', ['User'])[0]
            email = post_data.get('email', [''])[0]
            docid = post_data.get('docid', ['DOC-001'])[0]
            language = post_data.get('language', ['Academic Research'])[0]
            category = post_data.get('category', ['Perplexity & Burstiness NLP'])[0]
            newstype = post_data.get('newstype', ['Deep Scan'])[0]

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>AI Content Verification Result</title>
                <style>
                    body {{ font-family: Arial; background-color: #eef5ff; padding: 30px; }}
                    .card {{ max-width: 650px; margin: 0 auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
                    h1 {{ color: #2c3e50; }}
                    h2 {{ color: #1565c0; margin-top: 20px; }}
                    p {{ line-height: 1.6; margin: 6px 0; }}
                </style>
            </head>
            <body>
            <div class="card">
                <h1>AI Content Verification</h1>
                <h2>Content Verifier Details</h2>
                <p><b>Name:</b> {username}</p>
                <p><b>Email:</b> {email}</p>
                <p><b>Document ID:</b> {docid}</p>
                <p><b>Content Domain:</b> {language}</p>
                <p><b>Detection Engine:</b> {category}</p>
                <p><b>Verification Type:</b> {newstype}</p>
                <h2>AI Verification Information</h2>
                <p>Welcome to AI Content Verification System.</p>
                <p>Your selected detection engine is {category}.</p>
                <p>You selected {language} domain.</p>
                <p><b>Human Confidence:</b> 89.4% (Authentic)</p>
                <p><b>AI Generated Score:</b> 10.6% (Low Synthetic Risk)</p>
                <p style="color:#059669; font-weight:bold; font-size:16px;"><b>Audit Verdict:</b> Authentic Human Authorship Confirmed.</p>
                <br>
                <a href="index.html">← Return to Main Portal</a>
            </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
            return

        return super().do_POST()

def run():
    port = PORT
    # Try port 8080, if occupied try 8081 or 5000
    for test_port in [8080, 8081, 5000, 3000]:
        try:
            with socketserver.TCPServer(("", test_port), VeritasServerHandler) as httpd:
                print("="*60)
                print(" VERITAS — AI CONTENT VERIFICATION PLATFORM SERVER")
                print("="*60)
                print(f" Web Server running at: http://localhost:{test_port}")
                print(f" Document Root: {DIRECTORY}")
                print(" Press Ctrl+C to stop the server.")
                print("="*60)
                httpd.serve_forever()
                break
        except OSError:
            print(f"Port {test_port} occupied, trying next port...")

if __name__ == '__main__':
    run()
