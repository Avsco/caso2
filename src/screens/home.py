from reactpy import component, html


@component
def home():
    return html.main(
        {"class_name": "flex flex-col gap-8 h-full"},
        html.div(
            {"class_name": "flex gap-4 w-full h-full"},
            html.div(
                {
                    "class_name": "grow w-full flex flex-col gap-12 items-center justify-center h-full"
                },
                html.div(
                    {"class_name": "flex justify-center"},
                    html.iframe(
                        {
                            "width": 560,
                            "height": 315,
                            "src": "https://www.youtube.com/embed/uIeHQIe_LEE?si=fKt7bDBo7PmdnvA_",
                            "title": "YouTube video player",
                            "frameborder": 0,
                            "allow": "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share",
                            "allowfullscreen": True,
                        },
                    ),
                ),
                html.a(
                    {"href": "/simulation"},
                    html.button(
                        {
                            "class_name": "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded",
                            "style": {"background-color": "#122A4C"},
                        },
                        "Iniciar simulacion",
                    ),
                ),
            ),
            html.div(
                {
                    "class_name": "grow w-full flex flex-col gap-4 items-center justify-center"
                },
                html.div(
                    html.h3(
                        {"class_name": "text-xl"},
                        "¿Qué es el simulador de interferencia?",
                    ),
                    html.p(
                        {"class_name": ""},
                        "El simulador de interferencia es una herramienta que permite a los usuarios simular la interferencia entre dos dos variables, en este caso, en el ensabmblaje de una flecha y un cojinete.",
                    ),
                ),
                html.div(
                    html.h3(
                        {"class_name": "text-xl"},
                        "¿Cómo funciona el simulador de interferencia?",
                    ),
                    html.p(
                        {"class_name": ""},
                        "El simulador de interferencia genera datos aleatorios de acuerdo con las distribuciones y parametros dados. A continuación, determina si hay interferencia entre las dos variables.",
                    ),
                ),
                html.div(
                    {"class_name": "w-full"},
                    html.h3(
                        {"class_name": "text-xl"},
                        "Instrucciones paso a paso",
                    ),
                    html.div(
                        {"class_name": "w-full"},
                        html.p("Para iniciar una simulación, siga estos pasos:"),
                        html.ol(
                            {"class_name": "list-decimal list-inside"},
                            html.li(
                                "En la página principal del simulador, haga clic en el botón 'Iniciar simulación'."
                            ),
                            html.li(
                                "En la página de inicio de la simulación, ingrese los parámetros de la simulación. "
                            ),
                            html.li("Haga clic en el botón 'Simular'."),
                        ),
                    ),
                ),
            ),
        ),
    )
