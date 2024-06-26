import json
import requests

def get_event_list():
    response = requests.get("https://www.york.cuny.edu/++api++/events")
    response.raise_for_status()
    items = response.json()["items"]
    event_list = [item["@id"] for item in items]
    event_list.pop(0)  # Remove the first element
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
        title = event_data["title"]
        description = event_data["description"]
        start = event_data["start"]
        end = event_data["end"]
        location = event_data["location"]

        event_details.append({
            "title": title,
            "description": description,
            "start": start,
            "end": end,
            "location": location
        })
    return event_details


event_list = get_event_list()

event_details = get_event_details(event_list)


pretty_json = json.dumps(event_details, indent=4)
print(pretty_json)