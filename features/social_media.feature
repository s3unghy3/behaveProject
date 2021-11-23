Feature: Testing Social Media presence

  Scenario: 4 Social Media does exist in product page
    Given The Home page is open
    When The Product Blouse is clicked
    Then Twitter is shown
    Then Facebook is shown
    Then Googleplus is shown
    Then Pinterest in shown