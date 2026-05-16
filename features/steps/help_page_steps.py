from behave import given, when, then


@given('Open Help page for Returns')
def click_cart(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {topic}')
def select_topic(context, topic):
    context.app.help_page.select_topic(topic)


@then('Verify Help {expected_text} page opened')
def verify_header_present(context, expected_text):
    context.app.help_page.verify_header_present(expected_text)

