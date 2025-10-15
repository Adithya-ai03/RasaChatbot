from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBookFlight(Action):
    def name(self) -> str:
        return "action_book_flight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        
        destination = tracker.get_slot("destination")
        departure = tracker.get_slot("departure")
        date = tracker.get_slot("date")
        return_date = tracker.get_slot("return_date")
        passengers = tracker.get_slot("passengers")

        if destination and departure and date:
            if return_date:
                msg = f"Booking your return flight from {departure} to {destination} on {date}, returning on {return_date}."
            else:
                msg = f"Booking your one-way flight from {departure} to {destination} on {date}."
        elif destination:
            msg = f"Sure! I can help you book a flight to {destination}."
        else:
            msg = "Please provide the destination so I can book your flight."

        dispatcher.utter_message(text=msg)
        return []
