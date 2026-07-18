from sample_api import DATA

from request import Request


class ApiClient:

    def send(

        self,

        endpoint

    ):

        request = Request(

            endpoint

        )

        return DATA.get(

            request.endpoint.path

        )
