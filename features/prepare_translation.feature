Feature: Test Scenarios for turbotlumaczenia site functionality

  Scenario: User can prepare translation for estimated cost and time
    Given Open main page
    When Click Wycena page
    And Click tłumaczenia pisemne
    And Choose translation from Polish into German
    And Choose proofreading option
    And Enter a text between 250 and 400 sings into textarea
    And Email fields should be ampty
    Then Check if expected price is calculated
    And Check if expected time is calculated