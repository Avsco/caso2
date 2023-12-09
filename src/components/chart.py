from reactpy import component, html


@component
def chart(interferences: int = 0, total: int = 0):
    return html.div(
        {
            "class_name": "show-print h-52",
        },
        html.div(
            {
                "class_name": "display-none",
                "id": "vars",
                "data-interferences": interferences,
                "data-total": total,
            },
        ),
        html.canvas(
            {
                "class_name": "m-auto",
                "id": "myDoughnutChart",
                "height": "100",
                "max-height": "100",
            },
        ),
    )
