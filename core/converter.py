import asyncio
from telethon import events


class Converter:

    def __init__(
        self,
        client,
        bot_username,
        timeout=120
    ):

        self.client = client
        self.bot = bot_username
        self.timeout = timeout



    async def convert(self, message):

        """
        Send message to converter bot
        and wait for converted result
        """

        try:

            # Forward original post
            await self.client.forward_messages(
                self.bot,
                message
            )


            # Wait for bot response

            response = await self.client.wait_for(
                events.NewMessage(
                    chats=self.bot
                ),
                timeout=self.timeout
            )


            converted = response.message


            # Check if bot returned something

            if not converted:

                print(
                    "Converter returned empty response"
                )

                return None



            # Check for error messages

            text = converted.text or ""


            error_words = [
                "error",
                "failed",
                "invalid",
                "try again"
            ]


            for word in error_words:

                if word.lower() in text.lower():

                    print(
                        "Converter error:",
                        text
                    )

                    return None



            return converted



        except asyncio.TimeoutError:

            print(
                "Converter timeout:",
                message.id
            )

            return None



        except Exception as e:

            print(
                "Converter exception:",
                e
            )

            return None
