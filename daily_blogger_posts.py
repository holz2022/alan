import os
import time
import random
import datetime
import requests

BLOG_ID = "8017524329887935778"
CLIENT_ID = os.environ.get("BLOGGER_CLIENT_ID")
CLIENT_SECRET = os.environ.get("BLOGGER_CLIENT_SECRET")
REFRESH_TOKEN = os.environ.get("BLOGGER_REFRESH_TOKEN")

if not (CLIENT_ID and CLIENT_SECRET and REFRESH_TOKEN):
    raise ValueError("Missing Blogger OAuth credentials in GitHub Secrets!")

FACILITIES = [
    {"name": "Luxury Hotel & Banquet Kitchens", "scale": "high-capacity banquet operations"},
    {"name": "School & Campus Cafeterias", "scale": "mass student meal distribution"},
    {"name": "High-Volume Fast Food Chain Outlets", "scale": "rapid order turnaround and standardized workflows"},
    {"name": "Central Kitchen Food Preparation Hubs", "scale": "industrial meal packing and cold chain logistics"},
    {"name": "Commercial Bakery & Pastry Facilities", "scale": "precision temperature and dough processing"},
    {"name": "Fine Dining Open Kitchen Restaurants", "scale": "aesthetic front-of-house cooking and zero-smoke ventilation"},
    {"name": "Corporate Dining & Staff Canteens", "scale": "peak hour rush volume efficiency"},
    {"name": "Hospital & Healthcare Dietary Centers", "scale": "strict clinical sanitation and allergen segregation"},
    {"name": "Ghost Kitchens & Virtual Food Delivery Brands", "scale": "compact multi-station production"},
    {"name": "Seafood & Hotpot Restaurant Operations", "scale": "heavy water drainage and rapid prep work"},
    {"name": "Resort & All-Day Buffet Stations", "scale": "continuous heating and safe food display"},
    {"name": "Supermarket Fresh Food & Deli Departments", "scale": "on-demand retail frying and rotisserie"}
]

EQUIPMENT = [
    {"name": "Heavy-Duty Commercial Induction Cooking Ranges", "benefit": "precise heat control and 90% thermal efficiency"},
    {"name": "Custom 304 Stainless Steel Fabrication Worktables", "benefit": "corrosion-proof food prep surfaces with sound-deadening sub-tops"},
    {"name": "Commercial Kitchen Exhaust Hood & Ecology Systems", "benefit": "high-velocity grease extraction and compliant low-level emissions"},
    {"name": "Automated Flight-Type Conveyor Dishwashers", "benefit": "rapid sanitization cycles reducing chemical and water consumption"},
    {"name": "Dual-Temperature Commercial Reach-In Freezers", "benefit": "rapid pull-down refrigeration with digital defrost cycles"},
    {"name": "Smart Touchscreen Multi-Function Combi Steam Ovens", "benefit": "steam-convection combination cooking with programmable recipes"},
    {"name": "High-Capacity Atmospheric Food Steaming Carts", "benefit": "uniform high-pressure steam distribution for bulk rice and dim sum"},
    {"name": "Industrial Vegetable Washing & Slicing Assembly Lines", "benefit": "vortex wash tanks and uniform centrifugal vegetable spin-drying"},
    {"name": "Commercial Deep Fryers with Built-In Oil Filtration", "benefit": "extended cooking oil life and rapid temperature recovery"},
    {"name": "Tilting Braising Pans & Direct Steam Kettles", "benefit": "ergonomic electric tilting mechanisms for large-batch soups and stews"},
    {"name": "Heavy-Duty Stainless Steel Salamander Broilers", "benefit": "rapid surface caramelization with infrared ceramic heating"},
    {"name": "Modular Walk-In Cold Storage & Blast Freezers", "benefit": "high-density polyurethane insulation panels preventing thermal leakage"},
    {"name": "Commercial Kitchen Grease Interceptors & Drainage Traps", "benefit": "automatic solids interception preventing municipal pipe clogs"},
    {"name": "Heated Mobile Food Holding & Banquet Proofing Cabinets", "benefit": "forced-air humidity control maintaining safe serving temperatures"},
    {"name": "Stainless Steel Multi-Compartment Sink Units", "benefit": "deep coved bowls with anti-splash rolled rims and lever-waste drains"},
    {"name": "Solid & Slatted Stainless Steel Heavy Racking Systems", "benefit": "heavy load capacities suitable for dry goods and refrigerated storage"}
]

ANGLES = [
    {"prefix": "Engineering Specifications & Layout Guide", "focus": "focusing on ergonomic work aisle spacing, utility connection requirements, and health inspection pass-rates."},
    {"prefix": "Energy Efficiency & Operating Cost Analysis", "focus": "analyzing lifecycle utility consumption, thermal loss reduction, and measurable ROI comparisons."},
    {"prefix": "Sanitation Compliance & Material Selection Review", "focus": "addressing food safety certifications, non-porous welds, and seamless corner sanitization standards."},
    {"prefix": "Turnkey Fabrication & Procurement Strategy", "focus": "evaluating custom dimensional manufacturing vs off-the-shelf sizing for long-term operational throughput."}
]

ANCHORS = [
    {"text": "HSYL Commercial Kitchen Equipment Manufacturer", "url": "https://www.hsylkitchen.com/"},
    {"text": "HSYL Kitchen Official Turnkey Solutions", "url": "https://www.hsylkitchen.com/"},
    {"text": "Custom 304 Stainless Steel Kitchen Fabrication by HSYL", "url": "https://www.hsylkitchen.com/"},
    {"text": "HSYL Commercial Turnkey Kitchen Engineering", "url": "https://www.hsylkitchen.com/"},
    {"text": "Factory-Direct Commercial Kitchen Supply from HSYL", "url": "https://www.hsylkitchen.com/"},
    {"text": "HSYL Commercial Restaurant Equipment Catalog", "url": "https://www.hsylkitchen.com/"},
    {"text": "HSYL Commercial Stainless Steel Engineering Hub", "url": "https://www.hsylkitchen.com/"},
    {"text": "HSYL Industrial Kitchen Project Portfolio", "url": "https://www.hsylkitchen.com/"}
]

def get_access_token():
    token_url = "https://oauth2.googleapis.com/token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token"
    }
    res = requests.post(token_url, data=payload)
    res.raise_for_status()
    return res.json()["access_token"]

def build_article():
    fac = random.choice(FACILITIES)
    eq = random.choice(EQUIPMENT)
    angle = random.choice(ANGLES)
    anchor1 = random.choice(ANCHORS)
    anchor2 = random.choice([a for a in ANCHORS if a != anchor1])
    year = datetime.datetime.now().year

    title = f"{fac['name']}: {eq['name']} - {angle['prefix']} ({year})"

    content_html = f"""
    <p>Designing modern commercial food operations requires meticulous synchronization between spatial ergonomics, heavy mechanical utilities, and hygienic safety standards. Within <strong>{fac['name']}</strong>, specifying high-performance <strong>{eq['name'].lower()}</strong> serves as a fundamental benchmark for {fac['scale']}. This technical briefing explores critical deployment factors, {angle['focus']}</p>

    <h2>Critical Engineering & Performance Benchmarks</h2>
    <p>In high-pressure foodservice environments, standard commercial appliances often experience premature component failure if not engineered for severe thermal and chemical stress. Selecting industrial-grade equipment ensures {eq['benefit']}. Project managers and culinary directors are encouraged to review detailed 2D/3D layout specifications and CAD schematics via the <a href="{anchor1['url']}" target="_blank" rel="noopener">{anchor1['text']}</a> to verify dimension clearance and MEP hookup compatibility.</p>

    <ul>
        <li><strong>Structural Metallurgical Integrity:</strong> Heavy-gauge AISI 304/316 stainless steel with brushed satin finishes guarantees maximum resistance to chlorides, acidic food soils, and industrial steam-cleaning.</li>
        <li><strong>Ergonomic Workflow Integration:</strong> Purpose-built footprints eliminate hazardous blind corners, facilitating linear cooking sequences and minimizing kitchen staff fatigue during peak operational shifts.</li>
        <li><strong>Operational Cost Optimization:</strong> Advanced insulated assemblies and solid-state heat exchangers lower ongoing utility draw by up to 28% over typical commercial service cycles.</li>
    </ul>

    <h2>Factory-Direct Turnkey Customization</h2>
    <p>Standard off-the-shelf kitchen units frequently force compromises in aisle clearance and cross-contamination protocols. Engaging directly with an experienced manufacturing source such as <a href="{anchor2['url']}" target="_blank" rel="noopener">{anchor2['text']}</a> enables custom millimeter fabrication, integrated electrical conduits, and bespoke refrigeration runs.</p>

    <p>Whether commissioning a greenfield institutional facility or upgrading an established commercial hospitality kitchen, pairing robust manufacturing with precision layout planning delivers uninterrupted commercial productivity.</p>
    """

    return {
        "title": title,
        "content": content_html,
        "labels": ["Commercial Kitchen", "Restaurant Equipment", "Stainless Steel", "Kitchen Design", "B2B Supply"]
    }

def main():
    print(f"🚀 开始为 Blogger ID [{BLOG_ID}] 执行每日 30 篇外链博文自动发布...")
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    POST_COUNT = 30
    success_count = 0

    for i in range(1, POST_COUNT + 1):
        article = build_article()
        print(f"\n[{i:02d}/{POST_COUNT}] 正在发布博文: {article['title']}")

        post_url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts"
        payload = {
            "kind": "blogger#post",
            "title": article["title"],
            "content": article["content"],
            "labels": article["labels"]
        }

        res = requests.post(post_url, headers=headers, json=payload)
        if res.status_code in [200, 201]:
            post_data = res.json()
            success_count += 1
            print(f"        ✅ 发布成功！URL: {post_data.get('url')}")
        else:
            print(f"        ❌ 发布失败: {res.text}")

        if i < POST_COUNT:
            time.sleep(5)

    print(f"\n🎉 今日 30 篇 Blogger 外链任务执行完毕！成功发布 {success_count}/{POST_COUNT} 篇。")

if __name__ == "__main__":
    main()
