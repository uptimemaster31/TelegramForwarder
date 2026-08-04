from core.footer import add_footer



class Sender:


    def __init__(
        self,
        client,
        footer
    ):

        self.client = client
        self.footer = footer



    async def send(
        self,
        message,
        destination
    ):

        """
        Send converted message
        to destination channel
        """

        try:

            caption = add_footer(
                message.text,
                self.footer
            )


            # If media exists
            if message.media:


                await self.client.send_file(

                    destination,

                    file=message.media,

                    caption=caption,

                    parse_mode="html"

                )


            # If only text

            elif message.text:


                await self.client.send_message(

                    destination,

                    caption,

                    parse_mode="html"

                )


            else:

                print(
                    "Nothing to send:",
                    message.id
                )

                return False



            print(
                "Posted:",
                message.id
            )


            return True



        except Exception as e:


            print(
                "Send error:",
                e
            )


            return False
