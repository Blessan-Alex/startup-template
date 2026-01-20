
import urllib.request
import os

url = "https://images.pexels.com/photos/186461/pexels-photo-186461.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200"
path = r"c:/Users/blaze/Downloads/essence---free-bootstrap-4-one-page-template/essence-free-ud/img/bg/bg-cta.jpg"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req) as response, open(path, 'wb') as out_file:
        out_file.write(response.read())
    print("Successfully downloaded bg-cta.jpg")
except Exception as e:
    print(f"Failed to download: {e}")
