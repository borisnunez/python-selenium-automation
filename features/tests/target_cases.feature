# Created by borisnunez at 4/17/26
Feature: Test Cases on Target

  Scenario: Verify that "Your cart is empty" message is shown
    Given Open Target main page
    When Click on cart icon
    Then Should see "Your cart is empty" message


  Scenario: Verify that a logged out user can navigate to "Sing in"
    Given Open Target main page
    When Click on Sing in
    Then Verify Sing in form opened
