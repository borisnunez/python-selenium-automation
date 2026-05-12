# Created by borisnunez at 4/17/26
Feature: Test cases for Product Search on Target

  Scenario: User can search for a product "coffee" on Target
    Given Open Target main page
    When Search for coffee
    Then Verify search results for coffee shown

  Scenario: User can search for a product "dress shoes" on Target
    Given Open Target main page
    When Search for dress shoes
    Then Verify search results for dress shoes shown

  Scenario Outline: User can search for products
    Given Open Target main page

    When Search for <search_query>
    Then Verify search results for <product> shown
    Examples:
    |search_query   |product      |
    |shoes          |shoes        |
    |scotch tape    |scotch tape  |
    |chairs         |chairs       |

  Scenario: Verify that user can see product names and images
    Given Open Target main page
    When Search for Playstation 5
    Then Verify that every product has a name and an image

  #Scenario: User can see favorites tooltip for search results
    #Given Open Target main page
    #And Hover favorites icon
    #Then Favorites tooltip is shown
