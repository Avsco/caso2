from reactpy import component, html


@component
def item(f1: float = 0, f2: float = 0):
    r = "Hay interferencia" if (f1 > f2) else "No hay interferencia"

    return html.tr(
        {"key": f1 + f2},
        html.td(f1),
        html.td(f2),
        html.td(r),
    )
