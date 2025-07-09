# Notification Service Prototype

This mini–project demonstrates a pluggable notification framework written in modern Python.

## Features

* **Channels**  
  * Email – mocked by writing files to an `outbox/` directory  
  * Slack – mocked by printing to the console  

* **Templating** – powered by Jinja2

* **Event sources**  
  * Real-time (in-memory lists)  
  * Scheduled query (any callable, e.g. simulating SQL)

* **De-duplication** – pluggable policy, includes an in-memory example

* **Registry** – see every notification configuration in one place

## Running the example

```bash
pip install -r requirements.txt
python example.py
```

Watch the console for Slack messages and check the `outbox/` folder for generated email files.

## Adding a new notification

1. Create or choose an `EventSource` (e.g., `RealTimeEventSource`).
2. Write a `Template` string containing Jinja2 placeholders.
3. Select a `NotificationChannel` (or implement a new one by subclassing `NotificationChannel`).
4. Assemble them into a `Notification` instance and register it:

```python
registry.register(Notification(
    name="My Cool Notification",
    channel=my_channel,
    template=my_template,
    event_source=my_source,
))
```

## Extending the system

* **New channel** – subclass `NotificationChannel` and implement `send`.
* **New event source** – subclass `EventSource` and implement `get_events`.
* **New dedup policy** – subclass `DedupPolicy` and implement `is_duplicate`.

Because dependencies are injected via constructors, components are easy to unit-test in isolation. 