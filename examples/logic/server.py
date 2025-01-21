from flask import Flask, request
from llm import get_model_response

# create an app instance
app = Flask(__name__)

# use openai key
# call model with key
# use function here

# '/' is the "home" route (like home page). only accepts POST requests (with the payload being {"prompt": "<prompt_text>"})
@app.route("/", methods=['POST'])
def model():

    # get prompt text from user's post request
    data = request.get_json()
    prompt =  data.get("prompt")

    # give that prompt to model
    response = get_model_response(prompt)
    return response or "Model failed."

# look into if flask has a better method for child endpoints
# @app.route("/cheese/gouda", methods=['POST'])
# def model():
#     data = request.get_json()
#     prompt =  data.get("prompt")
#     response = get_model_response(prompt)
#     return response or "Model failed."

# look into if flask has a better method for catchall
# @app.route('/whatever')
# def all():
#     return "Go to cheese."

if __name__ == "__main__":
    # start the server
    app.run(host='0.0.0.0', port=2002)