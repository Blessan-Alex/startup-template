
import os
import random
import urllib.request
import urllib.error

# Base directory for images
BASE_DIR = r"c:/Users/blaze/Downloads/essence---free-bootstrap-4-one-page-template/essence-free-ud/img"

# Image Map: (Relative Path, Width, Height, Keywords)
images_to_replace = [
    # Root
    ("hero-area.jpg", 1920, 1080, "corporate,office,meeting"),
    ("intro.png", 500, 500, "workflow,diagram"),
    ("dummy.png", 100, 100, "texture,gray"),
    
    # Slider
    ("slider/bg-1.jpg", 1920, 1080, "business,video_call"),
    ("slider/bg-2.jpg", 1920, 1080, "tablet,checklist,office"),
    ("slider/bg-3.jpg", 1920, 1080, "skyscraper,building"),
    
    # Backgrounds
    ("bg/bg-cta.jpg", 1920, 600, "abstract,navy,technology"),
    ("bg/bg-subs.jpg", 1920, 500, "white,desk,minimal"),
    ("bg/video.jpg", 1920, 1080, "presentation,business"),
    ("bg/hero-area-2.jpg", 1920, 1080, "laptop,dashboard"),
    
    # About
    ("about/img-1.jpg", 600, 400, "whiteboard,planning,team"),
    ("about/img-2.jpg", 600, 400, "working,office,woman"),
    ("about/img1.png", 500, 500, "support,icon"),
    
    # Portfolio
    ("portfolio/img-1.jpg", 800, 600, "nurse,tablet,hospital"),
    ("portfolio/img-2.jpg", 800, 600, "finance,accounting,paper"),
    ("portfolio/img-3.jpg", 800, 600, "flowchart,whiteboard"),
    ("portfolio/img-4.jpg", 800, 600, "customer_service,headset,telemarketer"),
    ("portfolio/img-5.jpg", 800, 600, "server,cloud,security"),
    ("portfolio/img-6.jpg", 800, 600, "files,documents,folders"),
    ("portfolio/img-7.jpg", 800, 600, "meeting,chart,analytics"),
    
    # Team (Use 'face' or 'portrait' specifically)
    ("team/team1.png", 500, 500, "man,suit,business,portrait"),
    ("team/team2.png", 500, 500, "woman,glasses,business,portrait"),
    ("team/team3.png", 500, 500, "man,smile,portrait,business"),
    ("team/team4.png", 500, 500, "woman,laptop,student,portrait"),
    ("team/member-4.png", 500, 500, "woman,portrait,business"),
    
    # Testimonials
    ("testimonial/img1.jpg", 200, 200, "man,ceo,portrait,face"),
    ("testimonial/img2.jpg", 200, 200, "woman,executive,portrait,face"),
    ("testimonial/img3.jpg", 200, 200, "man,manager,portrait,face"),
    
    # Clients (Logos - difficult to generate realistic logos, will use minimal shapes)
    ("clients/img1.png", 200, 80, "logo,tech,minimal"),
    ("clients/img2.png", 200, 80, "logo,security,minimal"),
    ("clients/img3.png", 200, 80, "logo,business,minimal"),
    ("clients/img4.png", 200, 80, "logo,cloud,minimal"),
    ("clients/img5.png", 200, 80, "logo,award,minimal"),
    ("clients/img6.png", 200, 80, "logo,iso,minimal"),
    ("clients/img7.png", 200, 80, "logo,partner,minimal"),
    ("clients/img8.png", 200, 80, "logo,trust,minimal"),
    
    # Blog
    ("blog/img1.jpg", 800, 500, "checklist,clipboard"),
    ("blog/img2.jpg", 800, 500, "contract,signing,paper"),
    ("blog/img3.jpg", 800, 500, "calendar,tablet"),
    ("blog/blog-1-big.jpg", 1000, 600, "desk,laptop,work"),
    ("blog/avater-1.jpg", 100, 100, "man,writer,portrait"),
    ("blog/ta-avater.jpg", 100, 100, "woman,writer,portrait"),
    
    # Instagram
    ("instagram/insta1.jpg", 300, 300, "lunch,team,people"),
    ("instagram/insta2.jpg", 300, 300, "meeting,postit,office"),
    ("instagram/insta3.jpg", 300, 300, "award,employee,trophy"),
    ("instagram/insta4.jpg", 300, 300, "office,coffee,break"),
    ("instagram/insta5.jpg", 300, 300, "training,presentation,class"),
    ("instagram/insta6.jpg", 300, 300, "swag,brand,notebook")
]

def download_image(path, width, height, keywords):
    full_path = os.path.join(BASE_DIR, path)
    # Using loremflickr with random param to avoid caching
    url = f"https://loremflickr.com/{width}/{height}/{keywords}/all?random={random.randint(1, 10000)}"
    
    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        # User agent to ensure we don't get blocked
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
        
        print(f"Downloading {path} from {url}...")
        with urllib.request.urlopen(req, timeout=15) as response, open(full_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"PASS: {path}")
    except Exception as e:
        print(f"FAIL: {path} ({e})")

if __name__ == "__main__":
    print(f"Starting download of {len(images_to_replace)} images to {BASE_DIR}...")
    for item in images_to_replace:
        download_image(item[0], item[1], item[2], item[3])
    print("Download complete.")
