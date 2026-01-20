import os
import urllib.request

BASE_DIR = r"c:/Users/blaze/Downloads/essence---free-bootstrap-4-one-page-template/essence-free-ud/img"

badges = {
    "clients/img1.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/ISO_9001-2015.svg/512px-ISO_9001-2015.svg.png",
    "clients/img2.png": "https://upload.wikimedia.org/wikipedia/commons/c/c2/EU_gdpr.jpg",
    "clients/img3.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/ISO_9001-2015.svg/512px-ISO_9001-2015.svg.png",
    "clients/img4.png": "https://upload.wikimedia.org/wikipedia/commons/c/c2/EU_gdpr.jpg",
    "clients/img5.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/ISO_9001-2015.svg/512px-ISO_9001-2015.svg.png",
    "clients/img6.png": "https://upload.wikimedia.org/wikipedia/commons/c/c2/EU_gdpr.jpg",
    "clients/img7.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/ISO_9001-2015.svg/512px-ISO_9001-2015.svg.png",
    "clients/img8.png": "https://upload.wikimedia.org/wikipedia/commons/c/c2/EU_gdpr.jpg"
}

def download_file(url, path):
    full_path = os.path.join(BASE_DIR, path)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=30) as response, open(full_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"PASS: {path}")
    except Exception as e:
        print(f"FAIL: {path} ({e})")

if __name__ == "__main__":
    print("Downloading trust badges...")
    for path, url in badges.items():
        download_file(url, path)
    print("Trust badges downloaded.")
