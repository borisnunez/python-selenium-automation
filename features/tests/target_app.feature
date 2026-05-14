# Created by borisnunez at 5/8/26
Feature: Tests for Target App page


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Sign in page
    And Store original window
    When Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current window
    And Return to original window
