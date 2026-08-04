from html import escape


def add_footer(
    caption,
    footer
):

    if not caption:

        caption = ""


    # Prevent duplicate footer

    if "𝑨𝑳𝑳 CHANNEL" in caption:

        return caption



    return (
        caption
        +
        "\n\n"
        +
        footer
    )
