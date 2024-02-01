import json

import requests
from behave import given, when, then

API_BASE_URL = "http://127.0.0.1:5000"

@given('the API endpoint for adding a record is "{endpoint}"')
def step_given_add_record_endpoint(context, endpoint):
    context.add_record_endpoint = f"{API_BASE_URL}{endpoint}"
    
@when('POST request is made with payload')
def step_when_post_request(context):
    data = json.loads(context.text)
    context.response = requests.post(context.add_record_endpoint, json=data)

@then('the response status code should be {status_code}')
def step_then_check_status_code(context, status_code):
    assert context.response.status_code == int(status_code)

@then('the response message should be "{message}"')
def step_then_check_response_message(context, message):
    assert context.response.json().get('message') == message
