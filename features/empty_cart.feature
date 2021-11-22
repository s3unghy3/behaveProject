Feature: Testing the Contact Us page

  Background:
    Given The Home page is open

  Scenario: Empty cart by removing Delete button in the summary
    Given The Women button is clicked
    And The Product name is clicked
    And The Add to Cart button is clicked
    And The Proceed to checkout button is clicked
#    And The Before button is clicked
    When The Delete icon is clicked
    Then The alert-warning is shown