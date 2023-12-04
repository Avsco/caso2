from reactpy import component, html

cell_styles = {
    "class_name": "border border-slate-600",
    "style": {"min-width": "220px"},
}


@component
def item(f1: float = 0, f2: float = 0):
    r = "Si hay interferencia" if (f1 > f2) else "No hay interferencia"

    return html.tr(
        {"key": f1 + f2},
        html.td(cell_styles, f1),
        html.td(cell_styles, f2),
        html.td(
            {
                "class_name": "border border-slate-600 text-xs",
                "style": {"min-width": "220px"},
            },
            r,
        ),
    )
