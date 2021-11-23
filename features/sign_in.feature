Feature: Testing sign in page

  Background:
    Given The Home page is open
    And The Sign In link is clicked

  Scenario: Successful Log-in
    Given Enter email "s2@gmail.com" and password "12345"
    When Sign in button is clicked
    Then User logged in successfully


  Scenario Outline: Failed Log-in
    Given Enter email "<email>" and password "<password>"
    When Sign In button is clicked
    Then The "<msg>" error message is shown
    Examples:
      | email                          | password | msg                        |
      |                                | debrecen | An email address required. |
      | seunghye2mailbox.unideb.hu     | debrecen | Invalid email address.     |
      | valid@email.com                |          | Password is required.      |
      |                                |          | An email address required. |