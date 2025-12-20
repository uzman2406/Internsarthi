import csv
import os
import django

# SET DJANGO SETTINGS
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internsarthi.settings")
django.setup()

from home.models import Internship

CSV_FILE = "internship_data.csv"

def run():
    with open(CSV_FILE, encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            Internship.objects.get_or_create(
                internship_id=row["Internship Id"],
                defaults={
                    "role": row["Role"],
                    "company_name": row["Company Name"],
                    "location": row["Location"],
                    "duration": row["Duration"],
                    "stipend": row["Stipend"],
                    "intern_type": row["Intern Type"],
                    "skills": row["Skills"],
                    "perks": row["Perks"],
                    "website_link": row["Website Link"],
                }
            )

    print("✅ Internship data imported successfully")
