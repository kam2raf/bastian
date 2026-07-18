from response import Response

DATA = {

    "/users": Response(

        200,

        [

            {"id": 1, "name": "Alice"},

            {"id": 2, "name": "Bob"},

            {"id": 3, "name": "Emma"}

        ]

    ),

    "/posts": Response(

        200,

        [

            {"id": 101},

            {"id": 102}

        ]

    )

}
