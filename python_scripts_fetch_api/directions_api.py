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

    items = combined_response.get("blocks", {})
    print("Initial API response items:", items)
    if not items:
        print("No events found.")
        return []

    event_list = [item_id for item_id in items]
    if event_list:
        event_list.pop(0)  # Remove the first item if necessary
    return event_list, items

def insert_api_name(uri):
    return uri.replace(".edu/", ".edu/++api++/")

def get_event_details(event_list, items):
    event_details = []
    for event_id in event_list:
        event_data = items[event_id]
        title = event_data.get("plaintext", "No title provided")
        children = event_data.get("value", [])
        description = " ".join(child.get("text", "") for child in children[0].get("children", [])) if children else "No description provided"

        context = f"Title: {title}. Description: {description}."
        question = f"Provide details about CUNY York College's {title}."
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
    return event_details

endpoints = [
    "https://www.york.cuny.edu/++api++/about-york/directions"
]

event_list, items = get_event_list(endpoints)
if event_list:
    event_details = get_event_details(event_list, items)
    # Ensure the directory exists
    output_directory = "api_json"
    os.makedirs(output_directory, exist_ok=True)
    # Save event details to a JSON file
    output_file = os.path.join(output_directory, "directions.json")
    with open(output_file, "w") as f:
        json.dump(event_details, f, indent=4)
    print(f"Event details have been saved to {output_file}")
else:
    print("No event details to save.")
