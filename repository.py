from endpoint import Endpoint


class Repository:

    def users(self):

        return Endpoint(

            "/users",

            "GET"

        )

    def posts(self):

        return Endpoint(

            "/posts",

            "GET"

        )
