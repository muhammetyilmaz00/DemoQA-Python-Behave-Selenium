@regression @api
Feature: BookStore API Tests

#  @createUser
#  Scenario: Create a User Account
#    When I send a POST request to create a user with valid credentials
#    Then the response should have a status code of "201"
#    And I store the userId
#
#  @createUser
#  Scenario: Verify Error Handling for User Account Creation with Invalid Credentials
#    When I send a POST request to retrieve the error response for creating a user with invalid credentials
#    Then the response should have a status code of "400"

#  @generateToken
#  Scenario: Generate token
#    When I send a POST request to generate a token with valid credentials
#    Then the response should have a status code of "200"
#    And I store the token
#
#  @getListOfBooks
#  Scenario: Get List of Books
#    When I send a GET request to retrieve all books
#    Then the response should have a status code of "200"
#    And I store the books
#
  @postBooksToUser
  Scenario: Add a list of books for the created user
    When I send a POST request to create a user with valid credentials
    And I store the userId
    And I send a POST request to generate a token with valid credentials
    And I store the token
    And I send a GET request to retrieve all books
    And I store the books
    And I send a POST request to post the books to the user
    Then the response should have a status code of "201"
#
#  @postBooksToUser
#  Scenario: Verify Error Handling for Add Book to User
#    When I send a POST request to post the books with the invalid user details
#    Then the response should have a status code of 401
#
#  @deleteBook
#  Scenario: Remove one of the added books
#    When I send a POST request to create a user with valid credentials
#    And I store the userId
#    And I send a POST request to generate a token with valid credentials
#    And I store the token
#    And I send a GET request to retrieve all books
#    And I store the books
#    And I send a POST request to post the books to the user
#    And I send a DELETE request to delete a book from the user
#    Then the response should have a status code of 204
#
#  @deleteBook
#  Scenario: Verify Error Handling for Delete Book from User
#    When I send a DELETE request to delete a book from the invalid user details
#    Then the response should have a status code of 401