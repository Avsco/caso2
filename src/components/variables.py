from reactpy import component, html


@component
def variables(options: dict = {}, change_options=lambda x: x):
    def change_data(name: str, value: float):
        temp_options = options.copy()

        temp_options[name] = value
        change_options(options=temp_options)

    return html.section(
        html.div(
            html.p({"class_name": "text-2xl font-bold"}, "Variables parametrizables")
        ),
        html.div(
            html.label(
                {"class_name": "flex flex-col"},
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
            {"class_name": "flex items-center justify-between"},
            html.div(
                {"class_name": "flex items-center gap-4 my-6"},
                html.label(
                    {"class_name": "flex flex-col"},
                    "Media de cojinete",
                    html.input(
                        {
                            "type": "number",
                            "value": options["average_a"],
                            "step": 0.01,
                            "name": "average_a",
                            "on_change": lambda x: change_data(
                                name="average_a", value=float(x["target"]["value"])
                            ),
                        }
                    ),
                ),
                html.label(
                    {"class_name": "flex flex-col"},
                    "Varianza de cojinete",
                    html.input(
                        {
                            "type": "number",
                            "value": options["variance_a"],
                            "step": 0.0001,
                            "name": "variance_a",
                            "on_change": lambda x: change_data(
                                name="variance_a", value=float(x["target"]["value"])
                            ),
                        }
                    ),
                ),
            ),
            html.div(
                {"class_name": "flex items-center gap-4 my-6"},
                html.label(
                    {"class_name": "flex flex-col"},
                    "Media de flecha",
                    html.input(
                        {
                            "type": "number",
                            "value": options["average_f"],
                            "step": 0.01,
                            "name": "average_f",
                            "on_change": lambda x: change_data(
                                name="average_f", value=float(x["target"]["value"])
                            ),
                        }
                    ),
                ),
                html.label(
                    {"class_name": "flex flex-col"},
                    "Varianza de flecha",
                    html.input(
                        {
                            "type": "number",
                            "value": options["variance_f"],
                            "step": 0.0001,
                            "name": "variance_f",
                            "on_change": lambda x: change_data(
                                name="variance_f", value=float(x["target"]["value"])
                            ),
                        }
                    ),
                ),
            ),
        ),
    )
