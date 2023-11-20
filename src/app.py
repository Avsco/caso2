from reactpy import component, html, hooks

import random

from src.components.list_item import list_item
from src.components.variables import variables


@component
def app_element():
    list, set_list = hooks.use_state([])

    hooks.use_effect(
        lambda: set_list([[0.1, 0.2]]),
        dependencies=[],
    )

    return html.main(
        {"class_name": "flex flex-col gap-8 container min-h-screen p-4 min-w-full"},
        html.h1({"class_name": "text-4xl font-extrabold"}, "Caso 2"),
        html.div(list_item(items=list)),
        html.div(variables()),
    )
