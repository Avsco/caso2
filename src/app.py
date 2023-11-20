from reactpy import component, html, hooks

from src.components.list_item import list_item
from src.components.variables import variables
from src.utils.generate_list import generate_list

from src.constants.variables import (
    AVERAGE_A,
    AVERAGE_F,
    VARIANCE_A,
    VARIANCE_F,
)


@component
def app_element():
    data, set_data = hooks.use_state(
        {
            "list_random": [],
            "interferences": 0,
            "case_b": 0,
            "options": {
                "distribution": "normal",
                "average_a": AVERAGE_A,
                "average_f": AVERAGE_F,
                "variance_a": VARIANCE_A,
                "variance_f": VARIANCE_F,
            },
        }
    )

    def change_options(options):
        set_data(
            {
                "options": options,
                "list_random": data["list_random"],
                "interferences": data["interferences"],
                "case_b": data["case_b"],
            }
        )

    def calculate_list():
        temp_data = generate_list(options=data["options"])
        set_data(
            {
                "list_random": temp_data["list_random"],
                "interferences": temp_data["interferences"],
                "case_b": temp_data["case_b"],
                "options": data["options"],
            }
        )

    hooks.use_effect(
        calculate_list,
        dependencies=[data["options"]],
    )

    return html.main(
        {"class_name": "flex flex-col gap-8 container min-h-screen p-4 min-w-full"},
        html.div(
            {"class_name": "flex justify-between items-center"},
            html.h1({"class_name": "text-4xl font-extrabold"}, "Caso 2"),
            html.button(
                {
                    "class_name": "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded",
                    "onClick": lambda x: calculate_list(),
                },
                "Simular nuevamente",
            ),
        ),
        html.div(
            list_item(
                items=data["list_random"],
                interferences=data["interferences"],
                case_b=data["case_b"],
            )
        ),
        html.div(variables(change_options=change_options, options=data["options"])),
    )
