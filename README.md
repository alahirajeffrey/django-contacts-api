# django-contacts-api
Contact api with django and django rest framework

### Features
* Create contacts
* Read contacts
* Update contacts
* Delete contacts

### Requirements
- [Python](https://www.python.org/) is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected.
- [Django](https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
- [Django Rest Framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.
- [Postman](https://www.postman.com/downloads/) is an API client that makes it easy for developers to create, share, test and document APIs. This is done by allowing users to create and save simple and complex HTTP/s requests, as well as read their responses. The result - more efficient and less tedious work.

### Installation Guide
* Clone this repository using `git clone https://github.com/alahirajeffrey/django-contacts-api.git`
* Ensure you have python, django and django rest framework installed locally
* Navigate to the project folder and then find the folder contaaining the manage.py and run `python manage.py runserver` to start up your local server

### API Endpoints
| HTTP Verbs | Endpoints | Action | Required |
| --- | --- | --- | --- |
| POST | /contacts/ | Create a new contact | request.data.first_name, request.data.last_name, request.data.nickname, request.data.email, request.data.phone_number |
| GET | /contacts/list | Get all contacts |  |
| PUT | /contacts/pk | Update a contact | request.data.first_name, request.data.last_name, request.data.nickname, request.data.email, request.data.phone_number, req.params.pks |
| DELETE | /contacts/pk | Delete a contact | request.params.pk |
| GET | /contacts/pk | Get a single contact | request.params.pk |

### Author(s)
* [Alahira Jeffrey](https://github.com/alahirajeffrey)

### License
This project is available for use under the MIT License.
