
import os
import urllib.request

# Base directory for images
BASE_DIR = r"c:/Users/blaze/Downloads/essence---free-bootstrap-4-one-page-template/essence-free-ud/img"

# Direct URL Map extracted from Browser Agent
direct_url_map = {
    "hero-area.jpg": "https://images.unsplash.com/photo-1683200517782-717f1792fa58?mark=https%3A%2F%2Fimages.unsplash.com%2Fopengraph%2Flogo.png&mark-w=64&mark-align=top%2Cleft&mark-pad=50&h=630&w=1200&crop=faces%2Cedges&blend-w=1&blend=000000&blend-mode=normal&blend-alpha=10&auto=format&fit=crop&q=60&ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzY4OTI1NjA2fA&ixlib=rb-4.1.0",
    "slider/bg-1.jpg": "https://images.pexels.com/photos/7644076/pexels-photo-7644076.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "slider/bg-2.jpg": "https://images.pexels.com/photos/8293635/pexels-photo-8293635.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "slider/bg-3.jpg": "https://images.unsplash.com/photo-1604275359703-8ed6d8862c67?mark=https%3A%2F%2Fimages.unsplash.com%2Fopengraph%2Flogo.png&mark-w=64&mark-align=top%2Cleft&mark-pad=50&h=630&w=1200&crop=faces%2Cedges&blend-w=1&blend=000000&blend-mode=normal&blend-alpha=10&auto=format&fit=crop&q=60&ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzY4OTI1NjA2fA&ixlib=rb-4.1.0",
    "bg/video.jpg": "https://images.pexels.com/photos/6285074/pexels-photo-6285074.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "bg/hero-area-2.jpg": "https://images.unsplash.com/photo-1692385819533-f0707d365ca1?mark=https%3A%2F%2Fimages.unsplash.com%2Fopengraph%2Flogo.png&mark-w=64&mark-align=top%2Cleft&mark-pad=50&h=630&w=1200&crop=faces%2Cedges&blend-w=1&blend=000000&blend-mode=normal&blend-alpha=10&auto=format&fit=crop&q=60&ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzY4OTI1NzI1fA&ixlib=rb-4.1.0",
    "about/img-1.jpg": "https://images.pexels.com/photos/6803529/pexels-photo-6803529.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "about/img-2.jpg": "https://images.pexels.com/photos/32228055/pexels-photo-32228055.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "portfolio/img-1.jpg": "https://images.pexels.com/photos/7551582/pexels-photo-7551582.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "portfolio/img-2.jpg": "https://images.pexels.com/photos/33175649/pexels-photo-33175649.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "portfolio/img-3.jpg": "https://images.pexels.com/photos/1181311/pexels-photo-1181311.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "portfolio/img-4.jpg": "https://images.pexels.com/photos/7709252/pexels-photo-7709252.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "portfolio/img-5.jpg": "https://images.pexels.com/photos/4508751/pexels-photo-4508751.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "portfolio/img-6.jpg": "https://images.pexels.com/photos/34293526/pexels-photo-34293526.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "portfolio/img-7.jpg": "https://images.pexels.com/photos/4872027/pexels-photo-4872027.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "blog/img1.jpg": "https://images.pexels.com/photos/7718755/pexels-photo-7718755.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "blog/img2.jpg": "https://images.pexels.com/photos/7841420/pexels-photo-7841420.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "blog/img3.jpg": "https://images.pexels.com/photos/28353121/pexels-photo-28353121.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "blog/blog-1-big.jpg": "https://images.unsplash.com/photo-1621348016212-535c972093db?mark=https%3A%2F%2Fimages.unsplash.com%2Fopengraph%2Flogo.png&mark-w=64&mark-align=top%2Cleft&mark-pad=50&h=630&w=1200&crop=faces%2Cedges&blend-w=1&blend=000000&blend-mode=normal&blend-alpha=10&auto=format&fit=crop&q=60&ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzY4OTI1NzI1fA&ixlib=rb-4.1.0",
    "team/team1.png": "https://images.pexels.com/photos/32064778/pexels-photo-32064778.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "team/team2.png": "https://images.pexels.com/photos/30468665/pexels-photo-30468665.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "team/team3.png": "https://images.pexels.com/photos/30004315/pexels-photo-30004315.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "team/team4.png": "https://images.pexels.com/photos/26728100/pexels-photo-26728100.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "testimonial/img1.jpg": "https://images.pexels.com/photos/32064778/pexels-photo-32064778.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "testimonial/img2.jpg": "https://images.pexels.com/photos/30468665/pexels-photo-30468665.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200",
    "testimonial/img3.jpg": "https://images.pexels.com/photos/30004315/pexels-photo-30004315.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200"
}

def download_file(url, path):
    full_path = os.path.join(BASE_DIR, path)
    try:
        # Standard headers to mimic browser
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=30) as response, open(full_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"PASS: {path}")
    except Exception as e:
        print(f"FAIL: {path} ({e})")

if __name__ == "__main__":
    print(f"Downloading {len(direct_url_map)} specific user-requested images...")
    for rel_path, url in direct_url_map.items():
        download_file(url, rel_path)
    print("Download process complete.")
