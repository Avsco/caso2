from reactpy import component, html

from src.components.item import item
from src.components.chart import chart


cell_styles = {
    "class_name": "border border-slate-600",
    "style": {"min-width": "33%"},
}


@component
def list_item(
    items: list = [], interferences: int = 0, case_b: int = 0, alternative: bool = False
):
    body_list = (
        list(map(lambda x: item(x[0], x[1]), items))
        if len(items) > 0
        else [
            html.tr(
                html.td({"colspan": 3, "class_name": "center-text h-12"}, "Sin datos")
            )
        ]
    )

    return html.div(
        {"class_name": "w-full"},
        chart(interferences=interferences, total=len(items)),
        html.div(
            {
                "class_name": "table_x overflow-y-auto overflow-x-auto",
            },
            html.table(
                {
                    "class_name": "w-full text-center border-collapse border border-slate-500"
                },
                html.thead(
                    {
                        "class_name": "sticky top-0 z-10",
                        "style": {"background": "#B9B9B9", "height": "46px"},
                    },
                    html.tr(
                        html.th(
                            cell_styles,
                            "Cojinete",
                        ),
                        html.th(
                            cell_styles,
                            "Flecha",
                        ),
                        html.th(
                            cell_styles,
                            "Resultado",
                        ),
                    ),
                ),
                html.tbody(body_list),
            ),
        ),
        html.div(
            {
                "class_name": "overflow-y-auto flex flex-col gap-2",
                "style": {
                    "max-height": "36rem",
                    "color": "#122A4C",
                    "font-size": "1.2rem",
                },
            },
            html.p(
                f"Total de interferencias: {interferences}",
            ),
            html.div(
                {"class_name": "flex flex-col items-center justify-center"},
                html.span(
                    case_b
                    if alternative
                    else "0%"
                    if (len(items) == 0)
                    else f"{(interferences / len(items)) * 100}%"
                ),
                html.span("Numero de muestra" if alternative else "Interferencia"),
            ),
        ),
    )
