class Parser:

    def summary(

        self,

        response

    ):

        return {

            "status": response.status,

            "count": len(

                response.payload

            )

        }
