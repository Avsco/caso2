from reactpy import html


def input_number(
    label: str = "",
    value: float = 0,
    step: float = 0.01,
    name: str = "",
    on_change=lambda x: x,
    minified: bool = False,
):
    normal_style = "border border-gray-300 p-1 rounded-md"
    minified_style = "border border-gray-300 rounded-md w-16 h-6"

    label_style_normal = "flex w-full gap-2 block-inline align-middle"
    label_style_minified = "flex gap-2 block-inline align-middle"

    return (
        html.label(
            {"class_name": label_style_minified if minified else label_style_normal},
            f"{label}",
            html.input(
                {
                    "class_name": minified_style if minified else normal_style,
                    "type": "number",
                    "value": value,
                    "step": step,
                    "name": name,
                    "on_change": lambda x: on_change(
                        name=name, value=float(x["target"]["value"])
                    ),
                }
            ),
        ),
    )
