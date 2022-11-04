Feature:PharmEasy login

  Scenario Outline:Login the PharmEasy and logout the PharmEasy page
    Given Lunch the opera browser
    When Open PharmEasy click on login
    When user enter the valid phone number"<phone_number>"
    When User is able to click on the send OTP button
    When User is able to click on continue
    Then user is able to click on user icon
    When user is able to click on logout button

    Examples:
              |phone_number|
              |7981954564  |
              |798199955510  |
              |75$#@^&62   |


