from reactpy import html


def button(text: str = "", on_click=lambda x: x, name: str = ""):
    return (
        html.button(
            {
                "name": name,
                "class_name": "text-white py-2 px-4 rounded hidden-print",
                "style": {"background": "#122A4C"},
                "onClick": lambda x: on_click(),
            },
            text,
        ),
    )
