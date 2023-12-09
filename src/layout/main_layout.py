from reactpy import component, html


@component
def main_layout(children: list = {}):
    links = [
        {"name": "Inicio", "href": "/"},
        {"name": "Simulación", "href": "/simulation"},
        {"name": "Calcular muestra", "href": "/calculate_sample"},
        {"name": "Historial de simulaciones", "href": "/history"},
    ]
    item_links = list(
        map(
            lambda link: html.a(
                {"href": link["href"], "class_name": "grid items-center px-8"},
                link["name"],
            ),
            links,
        )
    )

    return html.div(
        {
            "class_name": "h-full",
            "style": {"font_family": "Inter, sans-serif"},
        },
        html.header(
            {"class_name": "hidden-print"},
            html.div(
                {"class_name": "p-4 h-18 flex items-center w-full pt-3"},
                html.h1(
                    {
                        "class_name": "text-4xl text-center font-thin w-full",
                        "style": {
                            "font_family": "Noto Sans Hebrew",
                        },
                    },
                    "CALCULO DE INTERFERENCIA",
                ),
            ),
            html.nav(
                {
                    "class_name": "h-20 w-full text-white",
                    "style": {
                        "background_color": "#122A4C",
                    },
                },
                html.ul(
                    {"class_name": "flex gap-4 h-full justify-center items-center"},
                    item_links,
                ),
            ),
        ),
        html.div(
            {"class_name": "p-4 h-full"},
            children,
        ),
    )
