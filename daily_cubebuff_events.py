import os
import time
import random
import datetime
import requests

CAL_API_KEY = os.environ.get("CUBEBUFF_CAL_API_KEY")
if not CAL_API_KEY:
    raise ValueError("Missing CUBEBUFF_CAL_API_KEY in GitHub Secrets!")

# Cal.com API v2
API_BASE = "https://api.cal.com/v2"
HEADERS = {
    "Authorization": f"Bearer {CAL_API_KEY}",
    "cal-api-version": "2024-06-14",
    "Content-Type": "application/json"
}

# ========== 12 大热门乐高系列与收藏品场景 ==========
THEMES = [
    {"name": "LEGO Star Wars UCS & Starships", "slug": "star-wars-ucs"},
    {"name": "LEGO Technic Supercars & Hypercars", "slug": "technic-supercars"},
    {"name": "LEGO Icons & Modular Buildings", "slug": "icons-modulars"},
    {"name": "LEGO Minifigures & Figurine Series", "slug": "minifigures-collection"},
    {"name": "LEGO Harry Potter & Hogwarts Castles", "slug": "harry-potter-castles"},
    {"name": "LEGO Speed Champions & Motorsport", "slug": "speed-champions"},
    {"name": "LEGO Marvel & DC Superhero Sets", "slug": "superheroes-dioramas"},
    {"name": "LEGO NASA & Space Exploration Models", "slug": "space-nasa-sets"},
    {"name": "LEGO Architecture & Landmark Series", "slug": "architecture-landmarks"},
    {"name": "Custom Anime Figures & Collectibles", "slug": "anime-collectibles"},
    {"name": "Diecast Scale Models & Race Cars", "slug": "diecast-models"},
    {"name": "LEGO Botanical & Floral Art Displays", "slug": "botanical-displays"}
]

# ========== 10 大核心展示盒与墙面挂框产品 ==========
PRODUCTS = [
    {"name": "Dustproof Clear Acrylic Display Case with Black Base", "slug": "clear-acrylic-case"},
    {"name": "Magnetic Wall-Mount Display Frame with UV Shield", "slug": "wall-mount-frame"},
    {"name": "Integrated Multi-Color LED Illuminated Showcase", "slug": "led-showcase"},
    {"name": "Multi-Tiered Stepped Acrylic Minifigure Display Case", "slug": "tiered-minifigure-case"},
    {"name": "Floating Wall Display Mount with Scratch-Resistant Acrylic", "slug": "floating-wall-mount"},
    {"name": "Mirror-Backing High-Gloss Collectible Display Box", "slug": "mirror-back-box"},
    {"name": "Custom Cut-to-Size UV-Filtering Acrylic Display Cabinet", "slug": "custom-cut-cabinet"},
    {"name": "Heavy-Duty Angled Display Stand & Pedestal", "slug": "angled-display-stand"},
    {"name": "Ultra-Clear Frameless Museum-Grade Display Showcase", "slug": "museum-grade-case"},
    {"name": "Vertical Wall-Hanging Showcase for Vehicle Models", "slug": "vertical-wall-showcase"}
]

# ========== 8 大产品咨询与选型服务意图 ==========
INTENTS = [
    {"name": "Set Number Compatibility & Sizing Consultation", "len": 15},
    {"name": "Custom Dimension Acrylic Case Fabrication Review", "len": 20},
    {"name": "Wall Mount Installation & Stud Alignment Discussion", "len": 20},
    {"name": "Bulk Collector Order & Wholesale Quotation", "len": 30},
    {"name": "Integrated LED Lighting & Power Cable Routing Guide", "len": 15},
    {"name": "Collector Room & Studio Wall Display Planning", "len": 30},
    {"name": "New Set Release Pre-Order & Showcase Matching", "len": 15},
    {"name": "Museum-Grade UV Protection & Dust Resistance Review", "len": 20}
]

# ========== 10 种指向 www.cubebuff.com 的自然英文产品锚文本 ==========
ANCHOR_TEXTS = [
    "CubeBuff Official Website",
    "CubeBuff Acrylic Display Cases for LEGO",
    "CubeBuff Wall Mount Display Frames",
    "CubeBuff Custom LEGO Display Solutions",
    "CubeBuff Dustproof LEGO Showcases",
    "CubeBuff Premium Collectibles Display Cases",
    "CubeBuff LEGO Star Wars & Technic Display Boxes",
    "CubeBuff UV-Protected Acrylic Cases",
    "CubeBuff Wall-Mounted Showcase Frames",
    "CubeBuff Acrylic Model Display Systems"
]

def generate_100_cubebuff_events():
    """Generates 100 unique product-focused English meeting types for CubeBuff"""
    today_str = datetime.datetime.now().strftime("%Y%m%d")
    combos = []

    # 全量排列 (12 * 10 * 8 = 960 种组合)
    for t in THEMES:
        for p in PRODUCTS:
            for i in INTENTS:
                combos.append((t, p, i))
    
    # 随机打乱抽取 100 条不重复组合
    random.seed(int(today_str) + int(time.time()))
    selected = random.sample(combos, 100)

    events_payload = []
    for idx, (t, p, i) in enumerate(selected, 1):
        title = f"{t['name']}: {p['name']} - {i['name']}"
        slug = f"cubebuff-{t['slug']}-{p['slug']}-{today_str}-{idx:03d}"
        anchor = random.choice(ANCHOR_TEXTS)
        
        description = (
            f"Looking for the perfect display solution for your **{t['name']}**?\n\n"
            f"This session focuses on our **{p['name']}**, tailored specifically to your collection setup and **{i['name']}**.\n\n"
            f"Note: Browse our purpose-built display cases and wall mounts directly by LEGO set number on the [{anchor}](https://www.cubebuff.com/).\n\n"
            f"Please have your LEGO set number or display wall dimensions ready for a productive consultation."
        )

        events_payload.append({
            "title": title,
            "slug": slug,
            "lengthInMinutes": i["len"],
            "description": description
        })
    return events_payload

def main():
    print("🚀 Starting daily batch creation of 100 CubeBuff product matrix links (API v2)...")
    events = generate_100_cubebuff_events()
    success_count = 0

    for idx, ev in enumerate(events, 1):
        print(f"\n[{idx}/100] Publishing: {ev['title']}")
        print(f"        Slug: /{ev['slug']}")

        res = requests.post(
            f"{API_BASE}/event-types",
            headers=HEADERS,
            json=ev
        )

        if res.status_code in [200, 201]:
            success_count += 1
            print("        ✅ Success!")
        else:
            print(f"        ❌ Failed: {res.text}")

        # 间隔 1.2 秒限频保护
        time.sleep(1.2)

    print(f"\n🎉 Finished! Successfully published {success_count}/100 CubeBuff product links to Cal.com.")

if __name__ == "__main__":
    main()
