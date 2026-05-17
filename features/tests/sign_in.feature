# Created by borisnunez at 4/21/26
Feature: Sign in test cases

  Scenario: Verify that Sign in form opened
    Given Open Target main page
    When Click on Sing in from right side navigation menu
    Then Verify Sing in form opened

  Scenario: Verify ERROR message with incorrect password when Signing in
    Given Open Target main page
    When Click on Sing in from right side navigation menu
    When Enter correct email "boris.nunez@icloud.com" and click continue
    And Enter incorrect password "riuer5656iueri"
    Then Verify that en error message is shown

