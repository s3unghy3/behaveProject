Feature: Testing Searching Product

  Background:
    Given The Home page is open
    And The Search box is clicked

  Scenario: Searching products that doesn't exist
    Given Enter product "coat"
    When The Search button is clicked
    Then The alert-warning is shown


  Scenario Outline: Searching products that exist
    Given Enter product "<product>"
    When The Search button is clicked
    Then The "<result>" result is shown
    Examples:
      | product           | result                     |
      | dress             | 7 results have been found. |
      | chiffon           | 2 results have been found. |
      | short             | 4 results have been found. |
      | printed           | 5 results have been found. |