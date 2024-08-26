import json
import requests

base_url = "https://www.york.cuny.edu/++api++/"

def get_event_list(endpoints):
    responses = []

    for endpoint in endpoints:
        try:
            response = requests.get(base_url + endpoint)
            response.raise_for_status()
            data = response.json()
            responses.append(data)
        except requests.RequestException as e:
            print(f"Error fetching data from {endpoint}: {e}")
            continue
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {endpoint}: {e}")
            continue

    return responses

def find_values(json_obj, *keys):
    values = []

    if isinstance(json_obj, dict):
        for k, v in json_obj.items():
            if k in keys:
                if isinstance(v, str):
                    trimmed_value = v.strip()
                    if trimmed_value.endswith('.'):
                        values.append(trimmed_value)
            if isinstance(v, (dict, list)):
                values.extend(find_values(v, *keys))
    elif isinstance(json_obj, list):
        for item in json_obj:
            values.extend(find_values(item, *keys))

    return values

endpoints = [
    "academics",
    "academics/departments",
    "academics/honors",
    "academics/integrity",
    "academics/integrity/academic-integrity-committee",
    "academics/policies",
    "academics/college-now",
    "academics/york-stem-academy",
    "admissions",
    "admissions/new",
    "admissions/freshman",
    "admissions/transfer",
    "admissions/graduate",
    "admissions/international",
    "admissions/international/accepted",
    "admissions/international/cardinal-buddy",
    "admissions/international/graduate-international-admissions",
    "admissions/international/apply-now",
    "admissions/others",
    "welcome-center",
    "academic-affairs",
    "academics/navigate",
    "welcome-center/faqs",
    "cuny-explorers",
    "undergraduate-research",
    "university-skills-immersion-program",
    "news/2018/the-york-college-online-bookstore",
    "advisement",
    "advisement/degreeworks",
    "registrar",
    "registrar/instructions/schedule-builder",
    "scholarship",
    "scholarship/overview",
    "scholarship/dream-us",
    "scholarship/new-york-state-excelsior-scholarship",
    "arts-and-sciences",
    "current-student",
    "osas",
    "osas/committee-on-academic-policy-and-standards",
    "osas/petitions-appeals",
    "osas/sap",
    "osas/deadlines",
    "summer",
    "aviation-institute",
 
]

responses = get_event_list(endpoints)

all_values = []
for response in responses:
   desc = find_values(response, 'description', 'title')
   plaintext = find_values(response, 'plaintext', 'title')
   all_values.extend(desc)
   all_values.extend(plaintext)

print(all_values)
