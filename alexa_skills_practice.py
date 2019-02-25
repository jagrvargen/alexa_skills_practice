import random


"""
   ** Lambda Handler **
"""

def lambda_handler(event, session):
    """ Handles incoming Alexa requests """
    if event["request"]["type"] == "LaunchRequest":
        return handle_launch()
    elif event["request"]["type"] == "IntentRequest":
        return handle_intent(event["request"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return handle_session_end()

"""
   ** Request Handlers **
"""

def handle_launch():
    """ Greets user upon launching Alexa skill """
    text = "Welcome to complement, you're looking handsome today!"
    title = "Welcome"
    reprompt_text = "Is there something I can do for you today?"

    return alexa_response(speechlet_builder(text, title, reprompt_text, end_session=False))

def handle_intent(intent_request):
    """ Parses the intent request and responds accordingly """
    if intent_request["intent"]["name"] == "request_complement":
        text = random_complement()
        title = random_complement_title()
        reprompt_text = random_reprompt()

        return alexa_response(speechlet_builder(text, title, reprompt_text, end_session=False))

def handle_session_end():
    """ Says goodbye to user and ends session """
    text = "Goodbye friend!"
    title = "See ya!"
    reprompt_text = ""

    return alexa_response(speechlet_builder(text, title, reprompt_text))


"""
   ** Response Builders **
"""

def alexa_response(speechlet, session_attributes={}):
    """ Builds and returns Alexa response """
    response = {}
    response["version"] = "1.0"
    response["sessionAttributes"] = session_attributes
    response["response"] = speechlet

    return response

def output_speech_builder(text, text_type):
    """ Builds JSON object for output speech """
    output_speech = {}
    output_speech["type"] = text_type
    output_speech["text"] = text

    return output_speech

def card_builder(text, title, card_type):
    """ Builds JSON object for Alexa card """
    card = {}
    card["type"] = card_type
    card["title"] = title
    card["content"] = text

    return card

def reprompt_builder(text, text_type):
    """ Builds JSON object for reprompt message """
    reprompt = {"outputSpeech": {}}
    reprompt["outputSpeech"]["text"] = text
    reprompt["outputSpeech"]["type"] = text_type

    return reprompt

def speechlet_builder(text, title, reprompt_text, text_type="PlainText", card_type="Simple", end_session=True):
    """ Builds speechlet to pass to alexa_response """
    speechlet = {}
    speechlet["outputSpeech"] = output_speech_builder(text, text_type)
    speechlet["card"] = card_builder(text, title, card_type)
    speechlet["reprompt"] = reprompt_builder(reprompt_text, text_type)
    speechlet["shouldEndSession"] = end_session

    return speechlet


"""
   ** Functionality **
"""

def random_complement_title():
    """ Generates title for card with complement """
    complement_titles = ["Here's a complement!", "One complement coming up!", "You deserve a complement"]

    return complement_titles[random.randint(0, len(complement_titles) - 1)]

def random_complement():
    """ Generates a complement for output speech """
    complements = ["You look beautiful", "You're the most handsomest person alive", "Me yow"]

    return complements[random.randint(0, len(complements) - 1)]

def random_reprompt():
    """ Generates kind reprompt for user """
    reprompts = ["How you doing friend?", "You in the market for a complement?", "Who needs a complement? You do!"]

    return reprompts[random.randint(0, len(reprompts) - 1)]
