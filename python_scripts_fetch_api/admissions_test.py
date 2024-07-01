import requests
import json

def get_event_list():
    response = requests.get("https://www.york.cuny.edu/++api++/admissions")
    response.raise_for_status()
    items = response.json()["items"]
    print("Initial API response items:", items)
    if not items:
        print("No events found.")
        return []
    event_list = [item['@id'] for item in items]
    event_list.pop(0)
    return event_list

def insert_api_name(uri):
    return uri.replace(".edu/", ".edu/++api++/")

def get_event_details(event_list):
    event_details = []
    for event in event_list:
        api_event = insert_api_name(event)
        response = requests.get(api_event)
        response.raise_for_status()
        event_data = response.json()
        title = event_data.get("title", "No title provided")
        description = event_data.get("description", "No description provided")
        start = event_data.get("start", "No start time provided")
        end = event_data.get("end", "No end time provided")
        location = event_data.get("location", "No location provided")


        event_details.append({
            "title": title,
            "description": description,
            "start": start,
            "end": end,
            "location": location
        })
    return event_details

event_list = get_event_list()
if event_list:
    event_details = get_event_details(event_list)
    # Save event details to a JSON file
    output_file = "yorkgpt/api_json/york_events.json"
    with open(output_file, "w") as f:
        json.dump(event_details, f, indent=4)
    print(f"Event details have been saved to {output_file}")
else:
    print("No event details to save.")

