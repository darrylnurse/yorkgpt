import requests
import json
import os

def get_event_list(endpoints):

    combined_response = {}

    for endpoint in endpoints:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        combined_response.update(data)

    items = combined_response["items"]
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

        context = f"{title} {description} Start: {start}. End: {end}. Location: {location}."
        question = f"Provide details about CUNY York College's {title}."
        event_detail = {
            "answers": [
                {
                    "text": [description],
                    "answer_start": [context.find(description)]
                }
            ],
            "context": context,
            "id": event_data.get("UID", "No ID provided"),
            "is_impossible": False,
            "plausible_answers": [],
            "question": question,
            "title": title
        }

        event_details.append(event_detail)
    return event_details

endpoints = [
    "https://www.york.cuny.edu/++api++/admissions",
    "https://www.york.cuny.edu/++api++/"
]

event_list = get_event_list(endpoints)
if event_list:
    event_details = get_event_details(event_list)
    # Ensure the directory exists
    output_directory = "api_json"
    os.makedirs(output_directory, exist_ok=True)
    # Save event details to a JSON file
    output_file = os.path.join(output_directory, "york_data.json")
    with open(output_file, "w") as f:
        json.dump(event_details, f, indent=4)
    print(f"Event details have been saved to {output_file}")
else:
    print("No event details to save.")
