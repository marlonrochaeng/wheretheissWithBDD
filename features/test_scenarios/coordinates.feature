@coordinates @regression

Feature: Testing satellite endpoints
    @testCoordinates
    Scenario: Testing retrievied information using correct coordinates
    Given I retrieve information using correct coordinates
    Then I should see status code "200" and the correct coordinates data

    @testWrongCoordinates
    Scenario: Testing retrievied information using incorrect coordinates
    Given I retrieve information using incorrect coordinates
    Then I should see status code "500" and the error message
    