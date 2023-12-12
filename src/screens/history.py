from reactpy import component, html
import json

FILEPATH = "src/constants/data.json"


def get_json_data():
    with open(FILEPATH) as json_file:
        data = json.load(json_file)
    return data


def set_json_data(data):
    with open(FILEPATH, "w") as outfile:
        json.dump(data, outfile)


def item_history(item):
    return html.li(
        {"class_name": "list-group-item"},
        html.div(
            html.div(
                {"class_name": "badge badge-primary badge-pill font-black"},
                "Simulación",
            ),
            html.div(
                {"class_name": "badge badge-primary badge-pill"},
                f"Total simulaciones: {item['total_simulations']}",
            ),
            html.div(
                {"class_name": "badge badge-primary badge-pill"},
                f"Total interferencias: {item['total_interferences']}",
            ),
            html.div(
                {"class_name": "badge badge-primary badge-pill"},
                f"Flecha media: {item['average_a']}",
            ),
            html.div(
                {"class_name": "badge badge-primary badge-pill"},
                f"Cojinete media: {item['average_f']}",
            ),
            html.div(
                {"class_name": "badge badge-primary badge-pill"},
                f"Flecha varianza: {item['variance_a']}",
            ),
            html.div(
                {"class_name": "badge badge-primary badge-pill"},
                f"Cojinete varianza: {item['variance_f']}",
            ),
            html.div(
                {"style": {"color": "#122A4C"}},
                f"Conclusiónn: La simulación tiene una probabilidad mayor a 85% de interferencias, se recomienda reducir la varianza y/o medida de la flecha o incrementar la varianza y/o medida del cojinete"
                if (
                    item["total_interferences"] > 0
                    and item["total_simulations"] / item["total_interferences"] > 0.85
                )
                else f"Conclusiónn: La simulación tiene una probabilidad mayor a 40% y menor al 85% de interferencias, se recomienda reducir la varianza y/o medida de la flecha o incrementar la varianza y/o medida del cojinete"
                if (
                    item["total_interferences"] > 0
                    and item["total_simulations"] / item["total_interferences"] > 0.20
                )
                else f"Conclusiónn: La simulación tiene una probabilidad menor a 20% de interferencias, se tiene una buena media y varianza entre la flecha y el cojinete",
            ),
        ),
    )


@component
def history():
    list_history = get_json_data()

    items = [item_history(item) for item in list_history]

    return html.div(html.ol({"class_name": "list-group list-decimal p-4 pt-0"}, items))
