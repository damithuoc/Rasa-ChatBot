## greet
* greet
    - utter_greet
	

## goodbye
* goodbye
    - utter_goodbye

## sad path 2
* greet
- utter_greet
* mood_unhappy
- utter_ask_picture
* inform{"group":"cat"}
- action_retrieve_image
- utter_did_that_help
* mood_deny
- utter_goodbye