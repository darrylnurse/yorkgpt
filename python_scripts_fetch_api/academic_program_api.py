import requests
import json
import os

def get_event_list(endpoints):
    combined_response = {}

    for endpoint in endpoints:
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            data = response.json()
            combined_response.update(data)
        except requests.RequestException as e:
            print(f"Error fetching data from {endpoint}: {e}")
            continue
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {endpoint}: {e}")
            continue

    items = combined_response.get("items", [])
    print("Initial API response items:", items)
    if not items:
        print("No events found.")
        return [], []

    event_list = [item['@id'] for item in items]
    if event_list:
        event_list.pop(0)  # Remove the first item if necessary

    return event_list, items

def fetch_details(data):
    details = []
    if "navigation" in data and "items" in data["navigation"]:
        for item in data["navigation"]["items"]:
            detail = {
                "id": item.get("@id", "No ID provided"),
                "description": item.get("description", "No description provided"),
                "title": item.get("title", "No title provided")
            }
            details.append(detail)
            # Recursively fetch details for nested items
            if item.get("items"):
                details.extend(fetch_details({"navigation": {"items": item["items"]}}))
    return details

def get_event_details(event_list, items):
    event_details = []
    for event_id in event_list:
        event_data = next((item for item in items if item['@id'] == event_id), {})
        if not event_data:
            continue

        description = event_data.get("description", "No description provided")
        title = event_data.get("title", "No title provided")
        context = f"ID: {event_id}, Title: {title}, Description: {description}"
        question = f"Provide details about {title}."
        event_detail = {
            "answers": [
                {
                    "text": [description],
                    "answer_start": [context.find(description)]
                }
            ],
            "context": context,
            "id": event_id,
            "question": question,
            "title": title
        }

        event_details.append(event_detail)

        # Recursively fetch details for nested items
        if event_data.get("items"):
            nested_event_list = [item['@id'] for item in event_data["items"]]
            nested_details = get_event_details(nested_event_list, event_data["items"])
            event_details.extend(nested_details)

    return event_details

endpoints = [
    "https://www.york.cuny.edu/++api++/admissions/program",
    "https://www.york.cuny.edu/++api++/",
]

event_list, items = get_event_list(endpoints)
if event_list:
    event_details = get_event_details(event_list, items)
    # Extract additional details from navigation if available
    additional_details = fetch_details({"navigation": {"items": items}})
    event_details.extend(additional_details)
    # Ensure the directory exists
    output_directory = "api_json"
    os.makedirs(output_directory, exist_ok=True)
    # Save event details to a JSON file
    output_file = os.path.join(output_directory, "academic-program.json")
    with open(output_file, "w") as f:
        json.dump(event_details, f, indent=4)
    print(f"Event details have been saved to {output_file}")
else:
    print("No event details to save.")
