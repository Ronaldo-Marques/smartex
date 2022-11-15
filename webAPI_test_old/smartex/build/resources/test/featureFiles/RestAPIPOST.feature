Feature: Verify we get POST in the API

  Scenario Outline: GET all posts from the API
    Given Get call to "<url>"
    Then Response is "<statusCode>"

    Examples:
    | url | statusCode|
    | /posts | 200 |