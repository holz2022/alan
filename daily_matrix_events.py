import os
import time
import random
import datetime
import requests

CAL_API_KEY = os.environ.get("CAL_API_KEY")
if not CAL_API_KEY:
    raise ValueError("Missing CAL_API_KEY in GitHub Secrets!")

API_BASE = "https://api.cal.com/v1"
HEADERS = {"Content-Type": "application/json"}
PARAMS = {"apiKey": CAL_API_KEY}

# ========== 100% ENGLISH MATRIX KEYWORDS ==========

# 1. Target Industries & Facilities
SCENES = [
    {"name": "Commercial Hotel Kitchens", "slug": "hotel"},
    {"name": "School & Campus Cafeterias", "slug": "school-cafeteria"},
    {"name": "Quick Service Restaurant Chains", "slug": "qsr-chain"},
    {"name": "Corporate Dining & Staff Canteens", "slug": "corporate-dining"},
    {"name": "Central Kitchen Food Prep Hubs", "slug": "central-kitchen"},
    {"name": "Artisan Bakery & Pastry Studios", "slug": "bakery"},
    {"name": "Fine Dining & Open Kitchen Concepts", "slug": "fine-dining"},
    {"name": "Ghost Kitchens & Cloud Dining Facilities", "slug": "ghost-kitchen"}
]

# 2. Commercial Kitchen Equipment & Fabrication
PRODUCTS = [
    {"name": "Heavy-Duty Commercial Induction Ranges", "slug": "induction-range"},
    {"name": "Custom 304 Stainless Steel Worktables & Sinks", "slug": "stainless-tables-sinks"},
    {"name": "Commercial Exhaust Hoods & Ecology Systems", "slug": "exhaust-hoods"},
    {"name": "Conveyor & Pass-Through Dishwashers", "slug": "commercial-dishwashers"},
    {"name": "Dual-Temperature Reach-In Refrigerators & Freezers", "slug": "refrigerators-freezers"},
    {"name": "Intelligent Combi Steam Ovens", "slug": "combi-ovens"},
    {"name": "High-Capacity Food Steaming Carts", "slug": "food-steamers"},
    {"name": "Automated Vegetable Washing & Processing Lines", "slug": "veg-prep-lines"}
]

# 3. Consultation Focus & Duration
INTENTS = [
    {"name": "Free Layout Planning & Workflow Consultation", "len": 30},
    {"name": "Equipment Sizing & Project Budget Evaluation", "len": 15},
    {"name": "Factory-Direct Pricing & Bulk Procurement Review", "len": 20},
    {"name": "Kitchen Renovation & Environmental Compliance Meeting", "len": 45},
    {"name": "Custom CAD Drawing & Engineering Review", "len": 30}
]

# 4. English Anchor Texts for https://www.hsylkitchen.com/
ANCHOR_TEXTS = [
    "HSYL Kitchen Official Website",
    "HSYL Commercial Kitchen Equipment Catalog",
    "HSYL Kitchen Custom Stainless Steel Fabrication",
    "HSYL Turnkey Kitchen Project Solutions",
    "HSYL Factory-Direct Commercial Kitchen Supply",
    "HSYL Kitchen Engineering Portfolio & Case Studies"
]

def generate_30_events():
    """Generates 30 unique English meeting types using combinatorial matrix"""
    today_str = datetime.datetime.now().strftime("%Y%m%d")
    combos = []

    for s in SCENES:
        for p in PRODUCTS:
            for i in INTENTS:
                combos.append((s, p, i))
    
    # Shuffle and pick 30 unique combinations
    random.seed(int(today_str) + int(time.time()))
    selected = random.sample(combos, 30)

    events_payload = []
    for idx, (s, p, i) in enumerate(selected, 1):
        # 100% English Title
        title = f"{s['name']}: {p['name']} - {i['name']}"
        slug = f"hsyl-{s['slug']}-{p['slug']}-{today_str}-{idx:02d}"
        anchor = random.choice(ANCHOR_TEXTS)
        
        # 100% English Description with anchor text
        description = (
            f"This consultation is designed for **{s['name']}** exploring solutions for **{p['name']}**.\n\n"
            f"Our engineers will focus on **{i['name']}** tailored to your floor plan, utility requirements, and operational capacity.\n\n"
            f"📌 Prior to the meeting, we invite you to review our full equipment specifications, dimensional drawings, and completed projects on the [{anchor}](https://www.hsylkitchen.com/).\n\n"
            f"Please prepare your preliminary equipment list or layout dimensions for an efficient session."
        )

        events_payload.append({
            "title": title,
            "slug": slug,
            "length": i["len"],
            "description": description
        })
    return events_payload

def main():
    print("🚀 Starting daily batch creation of 30 English matrix booking links...")
    events = generate_30_events()
    success_count = 0

    for idx, ev in enumerate(events, 1):
        print(f"\n[{idx}/30] Publishing: {ev['title']}")
        print(f"       Slug: /{ev['slug']}")

        res = requests.post(
            f"{API_BASE}/event-types",
            headers=HEADERS,
            params=PARAMS,
            json=ev
        )

        if res.status_code in [200, 201]:
            success_count += 1
            print("       ✅ Success!")
        else:
            print(f"       ❌ Failed: {res.text}")

        # Polite delay to prevent rate limits
        time.sleep(1.5)

    print(f"\n🎉 Finished! Successfully published {success_count}/30 English matrix links to Cal.com.")

if __name__ == "__main__":
    main()
