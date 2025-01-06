import csv
import frappe

def execute():
    # Path to the CSV file within your app
    file_path = frappe.get_app_path("custom_frappe", "data", "user_fields.csv")

    # Read the CSV file
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Check if the field already exists
            if not frappe.db.exists("DocField", {"parent": "User", "fieldname": row["fieldname"]}):
                # Add the field to the User doctype
                frappe.get_doc({
                    "doctype": "DocField",
                    "parent": "User",
                    "fieldname": row["fieldname"],
                    "fieldtype": row["fieldtype"],
                    "label": row["label"],
                    "reqd": int(row.get("reqd", 0)),  # Handle null values
                    "read_only": int(row.get("read_only", 0)),  # Handle null values
                    "options": row.get("options", ""),
                    "insert_after": row.get("insert_after", "")
                }).insert()

    frappe.db.commit()
    print("User fields imported successfully.")

