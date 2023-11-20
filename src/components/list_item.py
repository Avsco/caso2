from reactpy import component, html
from src.components.item import item


@component
def list_item(items: list = []):
    body_list = list(map(lambda x: item(x[0], x[1]), items))

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
            html.tbody(
                body_list,
            ),
        ),
        html.p(f"Total de interferencias: {items.count('Hay interferencia')}"),
    )
