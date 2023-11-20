from reactpy import component, html

from src.components.item import item


@component
def list_item(items: list = [], interferences: int = 0, case_b: int = 0):
    body_list = list(map(lambda x: item(x[0], x[1]), items))

    return html.div(
        html.div(
            {"class_name": "overflow-y-auto", "style": {"max-height": "36rem"}},
            html.table(
                {"class_name": "w-full text-center"},
                html.thead(
                    {"class_name": "sticky top-0 z-10 bg-white"},
                    html.tr(
                        html.th("Cojinete"),
                        html.th("Flecha"),
                        html.th("Resultado"),
                    ),
                ),
                html.tbody(body_list),
            ),
        ),
        html.div(
            {"class_name": "overflow-y-auto", "style": {"max-height": "36rem"}},
            html.p(f"Total de interferencias: {interferences}"),
            html.p(f"Total de interferencias caso b: {case_b}"),
        ),
    )
