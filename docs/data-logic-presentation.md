# Data Logic Presentation

These are three separate layers, each representing different stages in the functionality of an application.

 - **Data Layer** - How and where a system's data is stored, accessed and manipulated. An example of this is a database, but in our case, it can be a dataset.<br/>
 - **Presentation Layer** - The view (or UI) that a user sees and experiences. They can interact with specific data that is appropriately formatted for the applications use case. It is also on this layer that users communicate with the logic. For example, through a form entity a user can send requests to the logic layer for processing.<br/>
- **Logic Layer** - This layer houses the core functionality of the application and often orchestrates communication between the previous two layers. It usually handles usage,transformation and movement of data in both directions, but can also be an LLM - a component which generates text for users.

Let's ignore the Presentation Layer for now (it's no fun) because we want to focus on the Server and LLM (and also because the Presentation Layer is no fun). 

In [this example](../examples/data-logic), we create a simple application to examine the Logic Layer.

It uses Flask as a server to route users request to a module that uses an LLM to generate a response and returns it to the user.

*Slow down dude!*

Okay, okay, let's go over **HTTP** (Hypertext Transfer Protocol) Requests and Responses (lightly).

A user (on the Presentation Layer 😒) says, "Hey it would make me very happy to go to this website!" (Not that we care). User then types "https://example.com" into their dumb browser and - 💥*BAMMFF*💥 - Theyr'e on the illustrious example dot com!

This was their request - "Please big bro can I please go to example.com!!". Begrudgingly, the server created by developers at Examplevidia deems the request acceptable - responding back with a response (😱) and a 200 status code. This was an request-response interaction between the Presentation and Logic layers.

But (unfortunately) there's more!! Our happy-go-lucky user unknowingly made a GET request to Examplevidia's server - one of the four main types of requests. 

These four types make up the amazingly-named **CRUD** (Create, Read, Update, Delete) acronym of the **REST** (Representational State Transfer) **API** (search that on your own) standard. To help you understand, let's dine out tonight! The server will be our... server. Here they come now! Time to *request* an order.

Get (Read): "I'd like a sandwich!"<br/>
Post (Create): "Hey, can I suggest a new item for the menu?"<br/>
Patch (Update): "I think you should add more salt to this dish."<br/>
Delete (Delete): "Take this dish off the menu!"<br/>

Your food arrives, and it's delicious! Don't forget to tip! (0.001%) That sandwich is like the response from the server - but we'll go more in depth on responses a little later.

*Ahem*, back to our mini app.

Everything in the code is explained through comments, so head to [../examples/logic]('../examples/logic') to try it for yourself.

In the logic directory, run: ```pip install -r requirements.txt``` to install the app's dependencies.

You will also need a .env file in your root directory with an OpenAI API key to actually use the OpenAI API. Once that .env file is create put this line in it: ```OPENAI_KEY=<place_your_actual_api_key_here_and_dont_just_copy_and_paste_this_it_wont_work_just_put_the_api_key_after_the_equals_sign_and_without_the_greater_and_less_than_signs_please>```

You can get a temporarily free API key by creating an OpenAI account. If you already had an account, create a new one. Those keys expire a month after you create an account. [This documentation should help you create your key.](https://platform.openai.com/docs/quickstart)

To actually interact with the server (once it's running) you need to be able to make HTTP requests.

You have three options I recommend:<br/>
1. Get Postman.
2. Seriously just get Postman.
3. You don't have Postman yet?

If you are stubborn and hate yourself for whatever reason, you can also use [curl](https://curl.se/). Alternatively, if you're a hotshot dev with money where your Tesla is, you can use python (running alongside the server) to make a request to the server. But I won't help you with that. Look it up.

*Fine.*

```
import requests
import json

url = "http://localhost:2002"

payload = json.dumps({
  "prompt": "Why did you make me do this?"
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

I *won't* be doing error handling for you though!

Now get outta here!