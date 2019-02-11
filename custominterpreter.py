import json

import requests
from wit import Wit


def jdeserilized():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(response.text)
    for t in todos:
        print(t['userId'])


def wit_resp():
    client = Wit('OA5N7TDP2JWMT3EYEPEM5L53YLE5T2N6')
    resp = client.message('hi')
    print(resp)


class CustomInterpreter():
    def parse(text):
        if text == 'hi':
            return {
                'text': text,
                'intent': {
                    'name': 'greet',
                    'confidence': 1.0,
                },
                'intent_ranking': [{
                    'name': 'greet',
                    'confidence': 1.0,
                }],
                'entities': [],
            }
        elif text == 'bye':
            return {
                'text': text,
                'intent': {
                    'name': 'goodbye',
                    'confidence': 1.0,
                },
                'intent_ranking': [{
                    'name': 'goodbye',
                    'confidence': 1.0,
                }],
                'entities': [],
            }
        elif text == 'sad':
            return {
                'text': text,
                'intent': {
                    'name': 'mood_unhappy',
                    'confidence': 1.0,
                },
                'intent_ranking': [{
                    'name': 'mood_unhappy',
                    'confidence': 1.0,
                }],
                'entities': [

                ]
            }
        elif text == 'no':
            return {
                'text': text,
                'intent': {
                    'name': 'mood_deny',
                    'confidence': 1.0,
                },
                'intent_ranking': [{
                    'name': 'mood_deny',
                    'confidence': 1.0,
                }],
                'entities': [

                ]
            }
        else:
            return {
                'text': text,
                'intent': {
                    'name': 'inform',
                    'confidence': 1.0,
                },
                'intent_ranking': [{
                    'name': 'inform',
                    'confidence': 1.0,
                }],
                'entities': [
                    {
                        "start": 2,
                        "end": 5,
                        "value": "cats",
                        "entity": "group"
                    }
                ],
            }
