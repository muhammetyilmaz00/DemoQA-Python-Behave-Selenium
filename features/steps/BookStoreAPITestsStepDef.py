from behave import step
from Services.ApiServices import apiServices
from random import randint

randomNumber = randint(0, 10000)


@step('I send a POST request to create a user with valid credentials')
def create_user(context):
    response = apiServices.create_user('testUser' + str(randomNumber), 'String123321*-')
    context.response = response
    # print('status code=' + str(response.status_code))


@step('the response should have a status code of "{code}"')
def check_status_code(context, code):
    assert context.response.status_code == int(code)


@step('I store the userId')
def store_user_id(context):
    # print('json=' + str(context.response.json()))
    # print('text=' + str(context.response.text))
    json_response = context.response.json()
    context.userId = json_response['userID']
    # print('userID=' + str(context.userId))


@step('I send a POST request to retrieve the error response for creating a user with invalid credentials')
def attempt_create_user_with_invalid_credentials(context):
    response = apiServices.create_user('invalid_username', 'invalid_password')
    context.response = response
    # print('status code=' + str(response.status_code))


@step('I send a POST request to generate a token with valid credentials')
def generate_token(context):
    response = apiServices.generate_token('testUser' + str(randomNumber), 'String123321*-')
    assert response.headers.get('Content-Type') == 'application/json; charset=utf-8'
    context.response = response
    # print('status code=' + str(response.status_code))


@step('I store the token')
def store_token(context):
    # print('json=' + str(context.response.json()))
    json_response = context.response.json()
    context.token = json_response['token']
    # print(str(context.token))


@step('I send a GET request to retrieve all books')
def get_all_books(context):
    response = apiServices.get_all_books()
    context.response = response


@step('I store the books')
def store_books(context):
    context.books = context.response.json()['books']
    # print(str(context.books))
    # for book in context.books:
    #     print(book)


@step('I send a POST request to post the books to the user')
def post_all_books_to_user(context):
    for book in context.books:
        # print('***************************************************')
        # print(str(book['isbn']))
        # print(context.userId)
        # print(context.token)
        # print('***************************************************')
        response = apiServices.post_book(context.userId, context.token, book['isbn'])
        # print(response)
        # print(response.status_code)
        assert response.headers.get('Content-Type') == 'application/json; charset=utf-8'
        context.response = response
        print('Book isbn ' + str(book['isbn']) + ' has been posted to the user ' + str(context.userId))
