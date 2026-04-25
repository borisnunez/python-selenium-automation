# Created by borisnunez at 4/21/26
Feature: Cart test cases

  Scenario:"Your cart is empty" is shown on empty cart
    Given Open Target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown