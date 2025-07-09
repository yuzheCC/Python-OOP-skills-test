from notification_service import (
    EmailChannel,
    SlackChannel,
    Template,
    RealTimeEventSource,
    ScheduledQueryEventSource,
    Notification,
    NotificationRegistry,
)


def mock_daily_stats_query():
    """Simulate a SQL query returning daily statistics."""
    return [
        {"id": 1, "active_users": 523, "new_signups": 32},
    ]


def main() -> None:
    registry = NotificationRegistry()

    # ----- User Signup Notifications -----
    user_signup_events = RealTimeEventSource(
        [
            {"id": "u1", "name": "Alice", "email": "alice@example.com"},
            {"id": "u2", "name": "Bob", "email": "bob@example.com"},
            {"id": "u1", "name": "Alice", "email": "alice@example.com"},  # duplicate
        ]
    )

    welcome_email_template = Template(
        name="welcome_email",
        text="Hello {{ name }}, welcome to our service!",
    )

    slack_new_user_template = Template(
        name="slack_new_user",
        text="New user signed up: {{ name }}",
    )

    email_channel = EmailChannel()
    slack_channel = SlackChannel()

    registry.register(
        Notification(
            name="User Signup Email",
            channel=email_channel,
            template=welcome_email_template,
            event_source=user_signup_events,
        )
    )

    registry.register(
        Notification(
            name="User Signup Slack",
            channel=slack_channel,
            template=slack_new_user_template,
            event_source=user_signup_events,
        )
    )

    # ----- Daily Stats Report -----
    daily_stats_template = Template(
        name="daily_stats_email",
        text=(
            "Daily report:\n"
            "- Active users: {{ active_users }}\n"
            "- New signups: {{ new_signups }}"
        ),
    )
    daily_stats_source = ScheduledQueryEventSource(mock_daily_stats_query)

    registry.register(
        Notification(
            name="Daily Stats Email",
            channel=email_channel,
            template=daily_stats_template,
            event_source=daily_stats_source,
        )
    )

    # ----- Execute all -----
    print(registry)
    registry.process_all()


if __name__ == "__main__":
    main() 