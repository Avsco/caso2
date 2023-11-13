from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure

import scipy.stats as stats
import random

app = FastAPI()

AVERAGE_A = 1.5
VARIANCE_A = 0.0016
STANDARD_DEVIATION_A = VARIANCE_A ** 0.5

AVERAGE_F = 1.48
VARIANCE_F = 0.0009
STANDARD_DEVIATION_F = VARIANCE_F ** 0.5


def formula(case, r):
    if(case == 1): 
        return  AVERAGE_A + ( STANDARD_DEVIATION_A * stats.norm.ppf(r) )
    else:
        return  AVERAGE_F + ( STANDARD_DEVIATION_F * stats.norm.ppf(r) )
    
tailwind = html.link(
    {
        "rel": "stylesheet",
        "href": "https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.7/tailwind.min.css",
    }
)

@component
def item():
    r1 = random.random()
    f1 = formula(1, r1)

    r2 = random.random()
    f2 = formula(2, r2)

    r =  "Hay interferencia" if (f1 > f2) else "No hay interferencia"

    return html.tr({"key": r1 + r2}, 
        html.td(f1),
        html.td(f2),
        html.td(r),
    )

@component
def listItem():
    lis = [item() for i in range(0, 20)]
    
    return html.div(
        html.table(
            { 
                "class_name": "w-full text-center border-collapse border-2 border-gray-500"
            },
            html.thead(
                html.tr(
                    html.th("Almuadilla"),
                    html.th("Flecha"),
                    html.th("Resultado"),
                )
            ),
            html.tbody(lis)
        ),
        html.p(f"Total de interferencias: {lis.count('Hay interferencia')}")
    )

@component
def variables():
    return  html.section(
        html.div(
            html.p({ "class_name": "text-2xl font-bold" },"Variables parametrizables")
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
            { "class_name": "flex items-center justify-between" },
            html.div(
                {
                    "class_name": "flex items-center gap-4 my-6"
                },
                html.label(
                    {"class_name": "flex flex-col"},
                    "Media de almuadilla",
                    html.input(
                        {
                            "type": "number",
                            "label": "Hola",
                            "value": AVERAGE_A,
                            "step": 0.01
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
                            "step": 0.0001
                        }
                    ),
                ),
            ),
            html.div(
                {
                    "class_name": "flex items-center gap-4 my-6"
                },
                html.label(
                    {"class_name": "flex flex-col"},
                    "Media de flecha",
                    html.input(
                        {
                            "type": "number",
                            "label": "Hola",
                            "value": AVERAGE_F,
                            "step": 0.01
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
                            "step": 0.0001
                        }
                    ),
                ),
            )
        )
    )

@component
def distributionElement():
    return 

@component
def App():
    return html.main(
        {
            "class_name": "flex flex-col gap-8 container min-h-screen p-4 min-w-full"
        },
        tailwind, 
        html.h1({ "class_name": "text-4xl font-extrabold" }, "Caso 2"),
        html.div(listItem()),
        html.div(variables()),
        html.div(distributionElement())
    )

configure(app, App)