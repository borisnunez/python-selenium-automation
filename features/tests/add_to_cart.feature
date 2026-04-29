# Created by borisnunez at 4/22/26
Feature: Test cases for "Add to Card" on Target

  Scenario: Add any product into the cart, and verify it’s there
    Given Open Target main page
    When Search for coffee
    When Click "Add to Cart" for selected coffee
    And Click "Add to Cart" on side window for coffee
    Then Verify product added to cart