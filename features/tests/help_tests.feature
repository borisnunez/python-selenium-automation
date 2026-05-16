# Created by borisnunez at 5/14/26
Feature: Tests for Help pages

  Scenario: User can select Help topic Promotions
    Given Open Help page for Returns
    Then Verify Help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify Help Current promotions page opened

  Scenario: User can select Help topic Target Circle
    Given Open Help page for Returns
    Then Verify Help Returns page opened
    When Select Help topic Target Circle™
    Then Verify Help About Target Circle page opened

  Scenario: User can select Help topic Target Account
    Given Open Help page for Returns
    Then Verify Help Returns page opened
    When Select Help topic Target Account
    Then Verify Help Create account page opened
