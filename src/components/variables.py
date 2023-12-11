from reactpy import component, html

from src.components.input_number import input_number


@component
def variables(options: dict = {}, change_options=lambda x: x):
    def change_data(name: str, value: float):
        temp_options = options.copy()

        temp_options[name] = value
        change_options(options=temp_options)

    return html.section(
        {"style": "color: #122A4C"},
        html.div(
            html.p(
                {"class_name": "text-md text-center mb-8"},
                "Variables parametrizables",
            )
        ),
        html.div(
            html.label(
                {"class_name": "flex flex-col mb-4"},
                "Distribucion",
                html.select(
                    {
                        "class_name": "border border-gray-300 p-2 rounded-md",
                        "value": "normal",
                        "name": "distribution",
                        "on_change": lambda x: change_data(
                            name="distribution", value=x["target"]["value"]
                        ),
                    },
                    html.option({"value": "normal"}, "Normal"),
                    html.option({"value": "uniform"}, "Uniforme"),
                    html.option({"value": "exponential"}, "Exponencial"),
                ),
            ),
        ),
        html.div(
            {"class_name": "flex items-center gap-8 column-temp"},
            html.div(
                {"class_name": "flex flex-col items-center gap-4"},
                html.span({"class_name": "w-full"}, "Cojinete"),
                input_number(
                    label="Media",
                    value=options["average_a"],
                    step=0.01,
                    name="average_a",
                    on_change=lambda name, value: change_data(name=name, value=value),
                ),
                input_number(
                    label="Varianza",
                    value=options["variance_a"],
                    step=0.0001,
                    name="variance_a",
                    on_change=lambda name, value: change_data(name=name, value=value),
                ),
            ),
            html.div(
                {"class_name": "flex flex-col items-center gap-4 w-full"},
                html.span({"class_name": "w-full"}, "Flecha"),
                input_number(
                    label="Media",
                    value=options["average_f"],
                    step=0.01,
                    name="average_f",
                    on_change=lambda name, value: change_data(name=name, value=value),
                ),
                input_number(
                    label="Varianza",
                    value=options["variance_f"],
                    step=0.0001,
                    name="variance_f",
                    on_change=lambda name, value: change_data(name=name, value=value),
                ),
            ),
        ),
    )
