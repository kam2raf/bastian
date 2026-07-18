from repository import Repository

from client import ApiClient

from parser import Parser

print()

print("Connecting...")

print()

endpoint = Repository().users()

print(

    endpoint.method,

    endpoint.path

)

print()

response = ApiClient().send(

    endpoint

)

summary = Parser().summary(

    response

)

print(

    "Status :",

    summary["status"]

)

print()

print(

    "Items received :",

    summary["count"]

)

print()

print(

    "Operation completed."

)
