## greet
* greet
    - utter_greet


## goodbye
* goodbye
    - utter_goodbye


## meetup
* meetup
    - action_meetup


## thanks+goodbye
* thanks+goodbye
    - utter_goodbye


## find_meetup_01
* greet
    - utter_greeting
* mood_great
    - utter_happy
* meetup{"location":"Berlin", "type":"sports"}
    - action_meetup
* affirm
    - action_join_meetup
* affirm
	- action_join_event
* ask_transport{"origin":"Rasa Technologies GmbH"}
	- action_suggest_route
* thanks
	- utter_thanks
	- utter_goodbye
	- action_slot_reset


## find_meetup_02
* greet
    - utter_greeting
* mood_great
    - utter_happy
* meetup{"location":"Berlin", "type":"sports"}
    - action_meetup
* affirm
    - action_join_meetup
* affirm
	- action_join_event
* ask_transport{"origin":"Alexanderplatz"}
	- action_suggest_route
* thanks
	- utter_thanks
	- utter_goodbye
	- action_slot_reset


## find_meetup_03
* greet
  - utter_greeting
* mood_great
  - utter_happy
* meetup{"location":"London", "type":"tech"}
	- action_meetup
* affirm
    - action_join_meetup
* affirm
	- action_join_event
* ask_transport{"origin":"Marylebone"}
	- action_suggest_route
* thanks
	- utter_thanks
	- utter_goodbye
	- action_slot_reset


## find_meetup_04
* greet
  - utter_greeting
* mood_great
  - utter_happy
* meetup{"location":"London", "type":"tech"}
	- action_meetup
* affirm
    - action_join_meetup
* thanks
	- utter_thanks
	- utter_goodbye
	- action_slot_reset


## find_meetup_06
* greet
  - utter_greeting
* mood_great
  - utter_happy
* meetup{"location":"Berlin", "type":"sports"}
    - action_meetup
* affirm
    - action_join_meetup
* affirm+ask_transport{"origin":"Alexanderplatz"}
	- action_join_event
	- action_suggest_route
* thanks+goodbye
	- utter_thanks
	- utter_goodbye
	- action_slot_reset


## find_meetup_07
* greet
  - utter_greeting
* mood_great
  - utter_happy
* meetup{"location":"Berlin", "type":"sports"}
    - action_meetup
* affirm
    - action_join_meetup
* affirm+ask_transport{"origin":"Rasa Technologies GmbH"}
	- action_join_event
	- action_suggest_route
* thanks+goodbye
	- utter_goodbye
	- action_slot_reset


## story_09
* greet
  - utter_greeting
* mood_great
  - utter_happy
* meetup{"location":"London", "type":"fitness"}
	- action_meetup
* affirm
	- action_join_meetup
* affirm+ask_transport{"origin":"Baker Street"}
	- action_join_event
	- action_suggest_route
* thanks+goodbye
	- utter_thanks
	- utter_goodbye
	- action_slot_reset


## story_10
* greet
  - utter_greeting
* mood_great
  - utter_happy
* meetup{"location":"London", "type":"fitness"}
	- action_meetup
* affirm
	- action_join_meetup
* affirm+ask_transport{"origin":"Baker Street"}
	- action_join_event
	- action_suggest_route
* thanks+goodbye
	- utter_goodbye
	- action_slot_reset

## find_meetup_11
* greet
  - utter_greeting
* mood_great
  - utter_happy
* meetup{"location":"Berlin", "type":"sports"}
    - action_meetup
* deny
	- utter_goodbye
	- action_slot_reset


## find_meetup_12
* greet
  - utter_greeting
* mood_great
  - utter_happy
* meetup{"location":"Berlin", "type":"sports"}
    - action_meetup
* affirm
	- action_join_meetup
* goodbye
	- utter_goodbye
	- action_slot_reset


## find_meetup_13
* greet
  - utter_greeting
* mood_great
  - utter_happy
* meetup{"location":"London", "type":"tech"}
	- action_meetup
* affirm
    - action_join_meetup
* affirm
	- action_join_event
* thanks
	- utter_thanks
	- utter_goodbye
	- action_slot_reset

## sad path 1
* greet
  - utter_greeting
* mood_unhappy
  - utter_ask_entertainment
* inform_type{"type":"dance"}
	- action_meetup
* affirm
    - action_join_meetup
* affirm
	- action_join_event
* thanks
	- utter_thanks
	- utter_goodbye
	- action_slot_reset

## sad path 2
* greet
  - utter_greeting
* mood_unhappy
  - utter_ask_entertainment
* inform_type{"type":"music"}
    - action_meetup
* affirm
	- action_join_meetup
* goodbye
	- utter_goodbye
	- action_slot_reset


## sad path 3
* greet
  - utter_greeting
* mood_unhappy
  - utter_ask_entertainment
* deny
	- utter_goodbye
	- action_slot_reset

## find_meetup_04
* greet
  - utter_greeting
* mood_unhappy
  - utter_ask_entertainment
* inform_type{"type":"poetry"}
	- action_meetup
* affirm
    - action_join_meetup
* thanks
	- utter_goodbye
	- action_slot_reset


## happy path 1
* greet
  - utter_greeting
* mood_great
  - utter_happy
* mood_affirm
  - utter_happy
* mood_affirm
  - utter_goodbye

## happy path 2
* greet
  - utter_greeting
* mood_great
  - utter_happy
* mood_deny
  - utter_goodbye

## strange user
* mood_affirm
  - utter_happy
* mood_affirm
  - utter_unclear


