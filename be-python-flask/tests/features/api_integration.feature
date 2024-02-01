Feature: Encounter API Integration

    Scenario: It is possible to add new encounter record
        Given the API endpoint for adding a record is "/records"
        When POST request is made with payload
        """
        {
            "person": "Rambo",
            "date_of_meeting": "2024-01-26",
            "what_we_did": "Some activity"
        }
        """
        Then the response status code should be 200
        And the response message should be "Record added successfully"
