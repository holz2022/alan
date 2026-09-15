import os
import time
import random
import datetime
import requests

CAL_API_KEY = os.environ.get("CAL_API_KEY")
if not CAL_API_KEY:
    raise ValueError("Missing CAL_API_KEY in GitHub Secrets!")

# Cal.com 官方最新 API v2
API_BASE = "https://api.cal.com/v2"
HEADERS = {
    "Authorization": f"Bearer {CAL_API_KEY}",
    "cal-api-version": "2024-06-14",
    "Content-Type": "application/json"
}

# ========== 15 大目标行业与客户场景 ==========
SCENES = [
    {"name": "Commercial Hotel Kitchens", "slug": "hotel"},
    {"name": "School & Campus Cafeterias", "slug": "school-cafeteria"},
    {"name": "Quick Service Restaurant Chains", "slug": "qsr-chain"},
    {"name": "Corporate Dining & Staff Canteens", "slug": "corporate-dining"},
    {"name": "Central Kitchen Food Prep Hubs", "slug": "central-kitchen"},
    {"name": "Artisan Bakery & Pastry Studios", "slug": "bakery"},
    {"name": "Fine Dining & Open Kitchen Concepts", "slug": "fine-dining"},
    {"name": "Ghost Kitchens & Cloud Dining Facilities", "slug": "ghost-kitchen"},
    {"name": "Hospital & Healthcare Foodservice", "slug": "hospital-kitchen"},
    {"name": "Supermarket Deli & Fresh Food Prep", "slug": "supermarket-deli"},
    {"name": "Resort & Buffet Dining Operations", "slug": "resort-buffet"},
    {"name": "Marine & Offshore Vessel Galleys", "slug": "marine-galley"},
    {"name": "Food Truck & Mobile Catering Concepts", "slug": "mobile-catering"},
    {"name": "Commercial Brewery & Taproom Kitchens", "slug": "brewery-kitchen"},
    {"name": "Stadium & Event Venue Catering", "slug": "stadium-catering"}
]

# ========== 20 大商业厨房设备与不锈钢定制品类 ==========
PRODUCTS = [
    {"name": "Heavy-Duty Commercial Induction Ranges", "slug": "induction-range"},
    {"name": "Custom 304 Stainless Steel Worktables & Sinks", "slug": "stainless-tables-sinks"},
    {"name": "Commercial Exhaust Hoods & Ecology Systems", "slug": "exhaust-hoods"},
    {"name": "Conveyor & Pass-Through Dishwashers", "slug": "commercial-dishwashers"},
    {"name": "Dual-Temperature Reach-In Refrigerators & Freezers", "slug": "refrigerators-freezers"},
    {"name": "Intelligent Combi Steam Ovens", "slug": "combi-ovens"},
    {"name": "High-Capacity Food Steaming Carts", "slug": "food-steamers"},
    {"name": "Automated Vegetable Washing & Processing Lines", "slug": "veg-prep-lines"},
    {"name": "Commercial Deep Fryers & Pressure Fryers", "slug": "commercial-fryers"},
    {"name": "Heavy-Duty Tilting Braising Pans & Kettles", "slug": "braising-pans"},
    {"name": "Stainless Steel Salamander Broilers & Griddles", "slug": "griddles-broilers"},
    {"name": "Walk-In Cold Rooms & Blast Freezers", "slug": "blast-freezers"},
    {"name": "Commercial Dough Mixers & Spiral Kneaders", "slug": "bakery-mixers"},
    {"name": "Stainless Steel Storage Racks & Shelving Systems", "slug": "storage-racking"},
    {"name": "Automated Dish Sanitizing & Drying Tunnels", "slug": "sanitizing-tunnels"},
    {"name": "Commercial Meat Slicers & Bone Saws", "slug": "meat-processing"},
    {"name": "Buffet Warmers & Bain Marie Serving Stations", "slug": "buffet-stations"},
    {"name": "Commercial Kitchen Waste Disposers & Grease Traps", "slug": "grease-traps"},
    {"name": "Stainless Steel Wall Shelves & Overshelves", "slug": "wall-shelving"},
    {"name": "Hot Food Holding Cabinets & Proofers", "slug": "holding-cabinets"}
]

# ========== 8 大咨询目的与意图 ==========
INTENTS = [
    {"name": "Free Layout Planning & Workflow Consultation", "len": 30},
    {"name": "Equipment Sizing & Project Budget Evaluation", "len": 15},
    {"name": "Factory-Direct Pricing & Bulk Procurement Review", "len": 20},
    {"name": "Kitchen Renovation & Environmental Compliance Meeting", "len": 45},
    {"name": "Custom CAD Drawing & Engineering Review", "len": 30},
    {"name": "Turnkey Project Quotation & Delivery Schedule Alignment", "len": 30},
    {"name": "Energy-Saving & Commercial Induction Conversion", "len": 20},
    {"name": "OEM/ODM Fabrication & Technical Specification Review", "len": 45}
]

# ========== 10 种自然英文锚文本库 (指向 https://www.hsylkitchen.com/) ==========
ANCHOR_TEXTS = [
    "HSYL Kitchen Official Website",
    "HSYL Commercial Kitchen Equipment Catalog",
    "HSYL Kitchen Custom Stainless Steel Fabrication",
    "HSYL Turnkey Kitchen Project Solutions",
    "HSYL Factory-Direct Commercial Kitchen Supply",
    "HSYL Kitchen Engineering Portfolio & Case Studies",
    "HSYL Commercial Restaurant Equipment Manufacturer",
    "HSYL Stainless Steel Kitchen Engineering Center",
    "HSYL Kitchen Turnkey Hospitality Solutions",
    "HSYL Global Commercial Kitchen Supply Hub"
]

def generate_100_events():
    """Generates 100 unique English meeting types from combinatorial matrix"""
    today_str = datetime.datetime.now().strftime("%Y%m%d")
    combos = []

    # 全量排列 (15 * 20 * 8 = 2400 种可能)
    for s in SCENES:
        for p in PRODUCTS:
            for i in INTENTS:
                combos.append((s, p, i))
    
    # 随机打乱并抽取 100 个互不重复的组合
    random.seed(int(today_str) + int(time.time()))
    selected = random.sample(combos, 100)

    events_payload = []
    for idx, (s, p, i) in enumerate(selected, 1):
        # 100% 英文标题
        title = f"{s['name']}: {p['name']} - {i['name']}"
        slug = f"hsyl-{s['slug']}-{p['slug']}-{today_str}-{idx:03d}"
        anchor = random.choice(ANCHOR_TEXTS)
        
        # 100% 英文描述与锚文本嵌入
        description = (
            f"This consultation is designed for **{s['name']}** exploring solutions for **{p['name']}**.\n\n"
            f"Our engineering team will focus on **{i['name']}** tailored to your layout dimensions, utility capacity, and budget.\n\n"
            f"Note: Prior to the meeting, we invite you to review our full equipment specifications, dimensional drawings, and completed projects on the [{anchor}](https://www.hsylkitchen.com/).\n\n"
            f"Please prepare your preliminary kitchen floor plan or equipment list for an efficient session."
        )

        events_payload.append({
            "title": title,
            "slug": slug,
            "lengthInMinutes": i["len"],
            "description": description
        })
    return events_payload

def main():
    print("🚀 Starting daily batch creation of 100 English matrix booking links (API v2)...")
    events = generate_100_events()
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

        # 每次间隔 1.2 秒防封限流（约 50 次/分钟，远低于官方 120次/分钟的上限）
        time.sleep(1.2)

    print(f"\n🎉 Finished! Successfully published {success_count}/100 English matrix links to Cal.com.")

if __name__ == "__main__":
    main()
