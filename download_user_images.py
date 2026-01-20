
import os
import re
import urllib.request
import urllib.error

# Base directory for images
BASE_DIR = r"c:/Users/blaze/Downloads/essence---free-bootstrap-4-one-page-template/essence-free-ud/img"

# Map of (Relative Path -> Page URL)
# Files without URLs will be skipped by this script (keeping previous auto-generated ones)
url_map = [
    # Root
    ("hero-area.jpg", "https://unsplash.com/photos/a-group-of-people-sitting-around-a-wooden-table-yQ4smaPYgnw"),

    # Slider
    ("slider/bg-1.jpg", "https://www.pexels.com/photo/a-group-of-people-in-a-meeting-using-video-call-7644076/"),
    ("slider/bg-2.jpg", "https://www.pexels.com/photo/checklist-on-a-clipboard-8293635/"),
    ("slider/bg-3.jpg", "https://unsplash.com/photos/low-angle-photography-of-high-rise-building-0Cb2rEs-5ZA"),

    # Backgrounds
    ("bg/video.jpg", "https://www.pexels.com/photo/man-presenting-graphs-in-business-meeting-6285074/"),
    ("bg/hero-area-2.jpg", "https://unsplash.com/photos/a-laptop-computer-sitting-on-top-of-a-wooden-desk-WUYLvaMvcdw"),

    # About
    ("about/img-1.jpg", "https://www.pexels.com/photo/men-in-an-office-sitting-at-a-meeting-and-looking-at-a-whiteboard-6803529/"),
    ("about/img-2.jpg", "https://www.pexels.com/photo/businesswoman-working-on-laptop-in-modern-office-32228055/"),

    # Portfolio
    ("portfolio/img-1.jpg", "https://www.pexels.com/photo/a-woman-standing-beside-the-elderly-man-holding-a-tablet-7551582/"),
    ("portfolio/img-2.jpg", "https://www.pexels.com/photo/business-calculation-with-financial-document-on-desk-33175649/"),
    ("portfolio/img-3.jpg", "https://www.pexels.com/photo/white-dry-erase-board-with-red-diagram-1181311/"),
    ("portfolio/img-4.jpg", "https://www.pexels.com/photo/a-woman-wearing-a-headset-7709252/"),
    ("portfolio/img-5.jpg", "https://www.pexels.com/photo/server-racks-on-data-center-4508751/"),
    ("portfolio/img-6.jpg", "https://www.pexels.com/photo/colorful-office-files-on-a-shelf-34293526/"),
    ("portfolio/img-7.jpg", "https://www.pexels.com/photo/businessman-making-presentation-in-conference-room-4872027/"),

    # Blog
    ("blog/img1.jpg", "https://www.pexels.com/photo/a-to-do-list-on-a-clipboard-7718755/"),
    ("blog/img2.jpg", "https://www.pexels.com/photo/employment-agreement-paper-with-pen-7841420/"),
    ("blog/img3.jpg", "https://www.pexels.com/photo/a-calendar-on-a-table-28353121/"),
    ("blog/blog-1-big.jpg", "https://unsplash.com/photos/a-desk-with-a-notepad-pen-and-glasses-on-it-dnUaK2fQf3w"),

    # Team
    ("team/team1.png", "https://www.pexels.com/photo/professional-headshot-of-businessman-in-suit-32064778/"),
    ("team/team2.png", "https://www.pexels.com/photo/professional-headshot-of-a-young-businesswoman-30468665/"),
    ("team/team3.png", "https://www.pexels.com/photo/professional-headshot-of-smiling-businessman-30004315/"),
    ("team/team4.png", "https://www.pexels.com/photo/portrait-of-a-businesswoman-26728100/"),

    # Testimonials (Reusing Team images as requested by user)
    ("testimonial/img1.jpg", "https://www.pexels.com/photo/professional-headshot-of-businessman-in-suit-32064778/"),
    ("testimonial/img2.jpg", "https://www.pexels.com/photo/professional-headshot-of-a-young-businesswoman-30468665/"),
    ("testimonial/img3.jpg", "https://www.pexels.com/photo/professional-headshot-of-smiling-businessman-30004315/"),
]

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; Bot/0.1; +http://mysite.com)'})
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            # Regex to find <meta property="og:image" content="...">
            match = re.search(r'<meta\s+property=["\']og:image["\']\s+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
            if match:
                return match.group(1)
            # Fallback for Pexels sometimes uses name="twitter:image"
            match_twitter = re.search(r'<meta\s+name=["\']twitter:image["\']\s+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
            if match_twitter:
                return match_twitter.group(1)
            return None
    except Exception as e:
        print(f"Error fetching OG image for {url}: {e}")
        return None

def download_file(url, path):
    full_path = os.path.join(BASE_DIR, path)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response, open(full_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"PASS: {path} <- {url}")
    except Exception as e:
        print(f"FAIL: {path} ({e})")

if __name__ == "__main__":
    print(f"Processing {len(url_map)} images...")
    for idx, (rel_path, page_url) in enumerate(url_map):
        print(f"[{idx+1}/{len(url_map)}] Fetching metadata for {rel_path}...")
        image_url = get_og_image(page_url)
        if image_url:
            # Pexels URL adjustment for size (optional, but OG image is usually good)
            # Unsplash OG image is usually high res enough (1080w)
            download_file(image_url, rel_path)
        else:
            print(f"SKIP: Could not find image URL for {rel_path}")
    print("Optimization complete.")
