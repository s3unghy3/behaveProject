Feature: Testing the Contact Us page

  Background:
    Given The Home page is open
    And The Contact Us link is clicked

  Scenario Outline: Succeeded to contact to the customer service
    Given Subject is "<subject>"
    And The email is "<email>"
    And The order reference is "<ref>"
    And The <message> is written in the Message
    When The send button is clicked
    Then the "<succeeded>" message is shown
    Examples:
      | subject          | email                      | ref    | message   | succeeded                                           |
      | Customer service | seunghye@mailbox.unideb.hu | d12345 |Hello      |Your message has been successfully sent to our team. |
      | Customer service | seunghye@mailbox.unideb.hu |        |Buna       |Your message has been successfully sent to our team. |
      | Webmaster        | seunghye@mailbox.unideb.hu | b12345 |Hola       |Your message has been successfully sent to our team. |
      | Webmaster        | seunghye@mailbox.unideb.hu |        |Szia       |Your message has been successfully sent to our team. |



  Scenario Outline: Failed to contact to the customer service
    Given Subject is "<subject>"
    And The email is "<email>"
    And The order reference is "<ref>"
    And The <message> is written in the Message
    When The send button is clicked
    Then the "<failed>" alert is shown
    Examples:
      | subject          | email                      | ref    | message   | failed                                               |
      | Customer service |                            | d12345 |  Hello    | Invalid email address.                               |
      |                  | seunghye@mailbox.unideb.hu |        |  Hello    | Please select a subject from the list provided.      |
      | Webmaster        | seunghye@mailbox.unideb.hu | b12345 |           | The message cannot be blank.                         |
      | Customer service | seunghye2mailbox.unideb.hu |        |           | Invalid email address.                               |