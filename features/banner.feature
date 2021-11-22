Feature: Testing the banner presence

 Background:
   Given The Home page is open

  Scenario: Banner does exist on the landing page
    Then Check if the Banner exists

  Scenario Outline: Banner does exist on every pages
    Then Navigate to the "<page>" page
    And Check if the Banner exists
    Examples:
      | page       |
      | contact-us |
      | sign-in    |
      | cart       |
      | our stores |

