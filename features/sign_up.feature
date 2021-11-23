Feature: Testing Sign-up page

  Scenario Outline: Sign-up with correct information
    Given The Home page is open
    And The Sign In link is clicked
    And The user types his/her email "<email>"
    When The create an account button is clicked
    And The user types his/her First name "<firstname>"
    And The user types his/her Last name "<lastname>"
    And The user set his/her Password "<password>"
    And The user types his/her Address "<address>"
    And The user types his/her City "<city>"
    And The user clicks his/her State "<state>"
    And The user types his/her Zip Code "<zipcode>"
    And The user types his/her Mobile phone number "<mobile>"
    And The user clicks Register button
    Then The user created his/her account
    Examples:
      | email              | firstname | lastname | password   | address         | city | state      | zipcode | mobile |
      | incheon@gmail.com  | Seunghye  | Yang     | hungary123 | halaszle ut 123 | Baja | California | 12345   | 010333 |
      | ysh@naver.com      | Viktor    | Kim      | budapest12 | jogobella ut 13 | Buda | Florida    | 12343   | 010222 |
      | sofia@naver.com    | Fekete    | Lee      | budapest32 | viz ut 13       | Buda | Iowa       | 12341   | 010555 |
      | pest@naver.com     | Feher     | Lee      | budapest42 | viz ut 33       | Baja | Idaho      | 12347   | 010666 |

