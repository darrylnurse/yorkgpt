const response = await fetch(
    "https://www.york.cuny.edu/++api++/events",
    { method: "GET" }
)

const { items } = await response.json();

const eventList = items.map(item => item["@id"]);
eventList.shift();

const insertApiName = uri => uri.replace(/.edu\//, ".edu/++api++/");

const eventDetails = [];
for(const event of eventList){
  const apiEvent = insertApiName(event);
  const response = await fetch(apiEvent);
  const { title, description, start, end, location } = await response.json();

  eventDetails.push(
      // We have the information from the Endpoint formatted to suit the document store needs of the LLM, so it can understand the context of the information.
      //`On ${new Date(start).toDateString().slice(4)}, there will be the event titled: ${title}, described as ${description}, taking place at ${location}`

      // Object is more readable for us, but might be more difficult for LLM to parse.
      {
        title: title,
        description: description,
        start: start, // It seems that start and end date for API are incorrect, when you compare it to the displayed information on the Website.
        end: end,
        location: location
      }

  );
}

console.log(eventDetails);

