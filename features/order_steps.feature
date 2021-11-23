Feature: Testing the order process

  Scenario: Going through the steps to place an order
    Given The Home page is open
    And The Women button is clicked
    And The Product name is clicked
    And The Add to Cart button is clicked
    And The Proceed to checkout button is clicked
    And Another Checkout button is clicked
    And Enter email "s2@gmail.com" and password "12345"
    And Sign in button is clicked
    And Checkout in Address is clicked
    And Terms of service is checked
    And Checkout in Shipping is clicked
    And The Payment button is clicked
    When The Confirm order button is clicked
    Then Order confirmation is shown
