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
def listItem():
    lis = [item() for i in range(0, 20)]
    return html.table(
        { 
            "style": {
                "border": "1px solid black",
                "border-collapse": "collapse",
                "text-align": "center",
                "width": "100%",
            },
            "class_name": "mx-2"
        
        },
        html.thead(
            html.tr(
                html.th("Almuadilla"),
                html.th("Flecha"),
                html.th("Resultado"),
            )
        ),
        html.tbody(
            lis
        )
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
def App():
    return html.main(
        tailwind, 
        html.h1("Caso 2"),
        html.div(listItem()),
        html.div(
            html.input(
                {
                    "type": "number",
                    "placeholder": "Almuadilla",
                    "class_name": "mx-2",
                    "label": "Hola"
                }
            )
        )
    )

configure(app, App)