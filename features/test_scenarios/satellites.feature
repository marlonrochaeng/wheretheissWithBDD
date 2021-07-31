@satellites @regression

Feature: Testing satellite coordination endpoints
    @listAllSatellite
    Scenario: Listing all satellites
    Given I retrieve all satellites list information
    Then I should see only one satellite
    And its name and id are "iss" and "100"

    @getByCorrectId
    Scenario: Get Satellite by id
    Given I retrieve the satellite info by id "25544"
    Then I should verify that its name is "iss"
    And all other information is valid

    @getByIncorrectId
    Scenario: Get Satellite by id
    Given I retrieve the satellite info by id "10"
    Then I should see status code "404" and an error message