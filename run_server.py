#!/usr/bin/env python3
"""
Simple HTTP Server for Medical Research Finder
-----------------------------------------------
This script starts a local web server to run the Medical Research Finder app.
Using a local server avoids CORS issues that occur when opening HTML files directly.

Usage:
    python run_server.py

Then open your browser to: http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    # Change to that directory
    os.chdir(script_dir)
    
    print("=" * 60)
    print("🔬 Medical Research Finder - Local Server")
    print("=" * 60)
    print(f"\n✓ Server starting on port {PORT}...")
    print(f"✓ Serving files from: {script_dir}\n")
    
    Handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/medical-research-finder-v2.html"
        print(f"🌐 Open in your browser:")
        print(f"   {url}\n")
        print("Press Ctrl+C to stop the server\n")
        print("=" * 60)
        
        # Try to open browser automatically
        try:
            webbrowser.open(url)
            print("✓ Browser opened automatically\n")
        except:
            print("⚠ Could not open browser automatically")
            print(f"  Please open manually: {url}\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✓ Server stopped")
            print("=" * 60)

if __name__ == "__main__":
    main()
