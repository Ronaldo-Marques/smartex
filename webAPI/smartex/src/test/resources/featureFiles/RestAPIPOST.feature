Feature: Verify we get POST in the API

  Scenario Outline: GET all posts from the API
    Given Get call to "<url>"
    Then Response is "<statusCode>"

    Examples:
    | url | statusCode|
    | /posts | 200 |

  Scenario Outline:  Verify Code
    Given Get Call to "<url>"
    Then Response  is array total "<total>"

    Examples:
      | url      | total |
      | /student | 18    |