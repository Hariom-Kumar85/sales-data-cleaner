import csv
import json

USD_TO_INR = 83

clean_data = []
seen = set()

with open("sales.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print("DEBUG ROW:", row)   # <-- keep this for now

        product_id = row[0].strip()
        product = row[1].replace('"', '').strip()

        price_str = row[2].replace('$', '').strip()
        price_usd = float(price_str)
        price_inr = round(price_usd * USD_TO_INR, 2)

        country = row[3].strip()

        key = (product, price_usd)
        if key in seen:
            continue
        seen.add(key)

        clean_data.append({
            "id": product_id,
            "product": product,
            "price_inr": price_inr,
            "country": country
        })

with open("clean_sales.json", "w", encoding="utf-8") as outfile:
    json.dump(clean_data, outfile, indent=4)

print("clean_sales.json generated successfully!")
