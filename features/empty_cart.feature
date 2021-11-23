Feature: Testing the Contact Us page

  Background:
    Given The Home page is open
    And The Women button is clicked
    And The Product name is clicked
    And The Add to Cart button is clicked
    And The Proceed to checkout button is clicked

  Scenario: Empty cart by removing Delete button in the summary
    When The Delete icon is clicked
    Then The alert-warning is shown


  Scenario: Empty cart by reducing Quantity in the summary
    When The Subtract icon is clicked
    Then The alert-warning is shown