import json
import re

def load_knowledge():
    with open("knowledge.json") as f:
        return json.load(f)

def get_pricing_info():
    data = load_knowledge()
    response = ""

    for plan, details in data["plans"].items():
        response += f"\n{plan.upper()} PLAN\n"
        response += f"Price: {details['price']}\n"
        response += "Features:\n"
        for feature in details["features"]:
            response += f"- {feature}\n"

    return response

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)