@positions @regression

Feature: Testing satellite position endpoints
    @satellitePosition
    Scenario: Listing all satellite positions with valid timestamps
    Given I retrieve all satellites positions with valid timestamps
    Then I should see the status code "200"
    And the information should be valid and same as expected


    @satellitePositionWrongId
    Scenario: Listing all satellite positions with invalid id
    Given I retrieve all satellites positions with invalid id
    Then I should a status code "404" and an error message


    @satellitePositionSameInformationQuantity
    Scenario: Checking the amount of information
    Given I retrieve all satellites positions with valid id and timestamp
    Then I should see the same quantity of information


    @satelliteUnit
    Scenario: Checking different types of units
    Given I retrieve all satellites positions with valid id and wrong units
    Then I the endpoint should work fine and don't display error