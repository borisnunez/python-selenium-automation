# Created by borisnunez at 4/17/26
Feature: Test cases for Product Search on Target

  Scenario: User can search for a product "tea" on Target
    Given Open Target main page
    When Search for soccer cleats
    Then Verify search results for soccer cleats shown

  Scenario: User can search for a product "coffee" on Target
    Given Open Target main page
    When Search for dress shoes
    Then Verify search results for dress shoes shown

  Scenario Outline: User can search for products
    Given Open Target main page
#    ..
    When Search for <search_query>
    Then Verify search results for <product> shown
    Examples:
    |search_query   |product      |
    |Coffee         |Coffee       |
    |coffee cup     |coffee cup   |
    |sugar          |sugar        |
#    |茶             |茶           |

