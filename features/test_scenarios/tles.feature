@tles @regression

Feature: Testing satellite tles endpoints
    @testtles
    Scenario: Testing retrievied information using correct tles info
    Given I retrieve information using correct information for tles
    Then I should see status code "200" and a valid data for tles

    @testtlesText
    Scenario: Testing retrievied information using text parameter for tles
    Given I retrieve information using text parameter for tles
    Then I should see the text "ISS (ZARYA)" in the response

    @testtlesWrongId
    Scenario: Testing retrievied information using incorrect id for tles
    Given I retrieve information using incorrect tles info
    Then I should see status code "404" and the error message for tles
    