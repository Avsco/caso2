from reactpy import component, html

from src.constants.variables import (
    AVERAGE_A,
    AVERAGE_F,
    VARIANCE_A,
    VARIANCE_F,
)


@component
def variables():
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
                    "Media de almuadilla",
                    html.input(
                        {
                            "type": "number",
                            "label": "Hola",
                            "value": AVERAGE_A,
                            "step": 0.01,
                        }
                    ),
                ),
                html.label(
                    {"class_name": "flex flex-col"},
                    "Varianza de almuadilla",
                    html.input(
                        {
                            "type": "number",
                            "label": "Hola",
                            "value": VARIANCE_A,
                            "step": 0.0001,
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
                            "label": "Hola",
                            "value": AVERAGE_F,
                            "step": 0.01,
                        }
                    ),
                ),
                html.label(
                    {"class_name": "flex flex-col"},
                    "Varianza de flecha",
                    html.input(
                        {
                            "type": "number",
                            "label": "Hola",
                            "value": VARIANCE_F,
                            "step": 0.0001,
                        }
                    ),
                ),
            ),
        ),
    )
