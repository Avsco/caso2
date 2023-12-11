from reactpy import component, html, hooks

from src.components.input_number import input_number
from src.components.button import button
from src.components.list_item import list_item
from src.components.variables import variables
from src.utils.generate_list import generate_list
from src.screens.history import set_json_data, get_json_data

from src.constants.variables import (
    AVERAGE_A,
    AVERAGE_F,
    VARIANCE_A,
    VARIANCE_F,
)


@component
def simulation():
    data, set_data = hooks.use_state(
        {
            "list_random": [],
            "interferences": 0,
            "number_of_simulations": 10,
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
                "number_of_simulations": data["number_of_simulations"],
            }
        )

    def change_number_of_simulations(value):
        set_data(
            {
                "number_of_simulations": value,
                "list_random": data["list_random"],
                "interferences": data["interferences"],
                "options": data["options"],
            }
        )

    def printing_action():
        print("printing...")

    def calculate_list():
        temp_data = generate_list(
            options=data["options"], limit=data["number_of_simulations"]
        )
        set_data(
            {
                "number_of_simulations": data["number_of_simulations"],
                "list_random": temp_data["list_random"],
                "interferences": temp_data["interferences"],
                "options": data["options"],
            }
        )

        list_data = get_json_data()
        list_data.append(
            {
                "distribution": data["options"]["distribution"],
                "total_interferences": temp_data["interferences"],
                "total_simulations": len(temp_data["list_random"]),
                "average_a": data["options"]["average_a"],
                "average_f": data["options"]["average_f"],
                "variance_a": data["options"]["variance_a"],
                "variance_f": data["options"]["variance_f"],
            }
        )

        set_json_data(list_data)

    def set_default():
        set_data(
            {
                "list_random": [],
                "interferences": 0,
                "number_of_simulations": 10,
                "options": {
                    "distribution": "normal",
                    "average_a": AVERAGE_A,
                    "average_f": AVERAGE_F,
                    "variance_a": VARIANCE_A,
                    "variance_f": VARIANCE_F,
                },
            }
        )

    return html.main(
        {"class_name": "flex grow gap-8 w-full"},
        html.div(
            {
                "class_name": "flex flex-col justify-between items-center w-full p-24 px-4 pb-0 gap-8",
            },
            list_item(
                items=data["list_random"],
                interferences=data["interferences"],
            ),
            html.div(
                {"class_name": "flex justify-center gap-8 w-full"},
                button(text="Volver a simular", on_click=set_default, name="simulate"),
                button(text="Generar reporte", on_click=printing_action, name="report"),
            ),
        ),
        html.div(
            {"class_name": "flex grow flex-col gap-4 p-24 px-4 w-full"},
            html.div(variables(change_options=change_options, options=data["options"])),
            html.div(
                {"class_name": "flex w-full"},
                html.p(
                    {"class_name": "grow", "style": {"color": "#122A4C"}},
                    "Para hacer el calculo de probabilidad de interferencia, inserte la cantidad de simulaciones que desee:",
                ),
                input_number(
                    value=data["number_of_simulations"],
                    step=1,
                    name="number_of_simulations",
                    on_change=lambda name, value: change_number_of_simulations(value),
                    minified=True,
                ),
            ),
            html.div(
                {"class_name": "m-auto"},
                button(text="Simular", on_click=calculate_list, name="simulate2"),
            ),
        ),
    )
