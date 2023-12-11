from reactpy import component, html, hooks

from src.components.input_number import input_number
from src.components.button import button
from src.components.list_item import list_item
from src.components.variables import variables
from src.utils.generate_list import generate_list_b

from src.constants.variables import (
    AVERAGE_A,
    AVERAGE_F,
    VARIANCE_A,
    VARIANCE_F,
)


@component
def calculate_sample():
    data, set_data = hooks.use_state(
        {
            "list_random": [],
            "interferences": 0,
            "case_b": 0,
            "security_level": 0.1,
            "interference_probability": 0.95,
            "is_break": False,
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
                "is_break": data["is_break"],
                "security_level": data["security_level"],
                "interference_probability": data["interference_probability"],
            }
        )

    def change_interference_probability(value):
        set_data(
            {
                "interference_probability": value,
                "list_random": data["list_random"],
                "interferences": data["interferences"],
                "case_b": data["case_b"],
                "is_break": data["is_break"],
                "options": data["options"],
                "security_level": data["security_level"],
            }
        )

    def change_security_level(value):
        set_data(
            {
                "security_level": value,
                "list_random": data["list_random"],
                "interferences": data["interferences"],
                "case_b": data["case_b"],
                "is_break": data["is_break"],
                "options": data["options"],
                "interference_probability": data["interference_probability"],
            }
        )

    def set_default():
        set_data(
            {
                "list_random": [],
                "interferences": 0,
                "case_b": 0,
                "is_break": False,
                "security_level": 0.1,
                "interference_probability": 0.95,
                "options": {
                    "distribution": "normal",
                    "average_a": AVERAGE_A,
                    "average_f": AVERAGE_F,
                    "variance_a": VARIANCE_A,
                    "variance_f": VARIANCE_F,
                },
            }
        )

    def empty_action():
        print("Printing...")

    def calculate_list():
        temp_data = generate_list_b(
            options=data["options"],
            security_level=data["security_level"],
            interference_probability=data["interference_probability"],
        )
        set_data(
            {
                "list_random": temp_data["list_random"],
                "interferences": temp_data["interferences"],
                "case_b": temp_data["case_b"],
                "is_break": temp_data["is_break"],
                "options": data["options"],
                "security_level": data["security_level"],
                "interference_probability": data["interference_probability"],
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
                case_b=data["case_b"],
                alternative=True,
            ),
            html.div(
                {"class_name": "flex justify-center gap-8 w-full"},
                button(text="Volver a simular", on_click=set_default, name="simulate"),
                button(text="Generar reporte", on_click=empty_action, name="report"),
            ),
        ),
        html.div(
            {"class_name": "flex grow flex-col gap-4 p-24 px-4 w-full"},
            html.div(variables(change_options=change_options, options=data["options"])),
            html.div(
                {"class_name": "flex w-full"},
                input_number(
                    value=data["interference_probability"],
                    step=1,
                    label="Probabilidad de interferencia estimada",
                    name="interference_probability",
                    on_change=lambda name, value: change_interference_probability(
                        value
                    ),
                    minified=True,
                ),
            ),
            html.div(
                {"class_name": "flex w-full"},
                input_number(
                    value=data["security_level"],
                    step=1,
                    label="Nivel de seguridad",
                    name="security_level",
                    on_change=lambda name, value: change_security_level(value),
                    minified=True,
                ),
            ),
            html.p(
                {
                    "class_name": "text-red-600",
                    "style": {"display": "block" if (data["is_break"]) else "none"},
                },
                "Número máximo de simulaciones alcanzado",
            ),
            html.div(
                {"class_name": "m-auto"},
                button(text="Calcular", on_click=calculate_list, name="simulate2"),
            ),
        ),
    )
