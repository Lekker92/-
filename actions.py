from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSubmitBookingForm(Action):
    def name(self) -> Text:
        return "action_submit_booking_form"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        destination = tracker.get_slot('destination')
        departure_date = tracker.get_slot('departure_date')
        
        if destination and departure_date:
            dispatcher.utter_message(text=f"Booking a ticket to {destination} on {departure_date}.")
        else:
            dispatcher.utter_message(text="I'm missing some information.")
        
        return []
