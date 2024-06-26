import requests


def read_url():
    response = requests.get("https://www.york.cuny.edu/++api++/admissions")
    links = response.json()["items"]
    links = [item['@id'] for item in links]
    return links


def get_event_details(event_list):
    event_details = []
    for event in event_list:
        response = requests.get("https://www.york.cuny.edu/++api++/admissions")
        response.raise_for_status()
        event_data = response.json()
        title = event_data["title"]
        description = event_data["description"]

        event_details.append({
            "title": title,
            "description": description,
        })
    return event_details


admissions = read_url()
event_details = get_event_details(admissions)

print(event_details)
