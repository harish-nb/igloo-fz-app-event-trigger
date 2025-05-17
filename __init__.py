import logging
import azure.functions as func

def main(event: func.EventGridEvent):
    logging.info('EventGrid trigger function processed an event.')
  
    # Log Event Grid event metadata
    logging.info(f"Event Subject: {event.subject}")
    logging.info(f"Event Type: {event.event_type}")
  
    # Log the actual event data
    try:
        data = event.get_json()
        logging.info(f"Event Data: {data}")

    except Exception as e:
        logging.error(f"Failed to parse event data: {e}")
