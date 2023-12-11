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
                    html.img(
                        {
                            "src": "https://lh3.googleusercontent.com/fife/AK0iWDxoNGe8kdVvh7Fkw8lFT9UFYSWGiyqfEJqXRZkgaGxNCvAZZT34JHndvi3MY3H9d5RGIOv4634w4I0Bb-FsvSF2ndae6D6nEUUW7E2WYNFo1TuiIYQFtKH4H_ZUsCxLzonO1jzhkO_TMKqhcZTBtC9A_XhLyGSVEdtkEdgORMZzfDkXort3oflLLaefhOYhpkPCsPcUtaXx5yT5U7DOBdsA8B8bC5GNtemOeKvj4g8apUYm_kfsXE8m22_GnKvy-eoJzfpxGnyIn7lKI4im7RYDipmyWYuAX2ugJz08IMuXnYcbVq7Iy458QDtdrGFKxxMAuaz8ZNz8JdwUBlCNXsKuozf_VSnf4tHnddCaW3nlpLeRsRTnmON1R6JSLspEBaFhgq-0kPYwaPzE86BJCvVwJKOtQXlW7dcZ3e6QH1okYOQexiiX4V27rZFgsWiB_UH6-HlpZdu0ja1NGQZfDFozydLDyntV7dcFXF1NH-48IIZDhetzRZict_3uOGj-yijcgpJPrgThZM3E4lN9Ljfsp5areDp1wyl3N4UnrADU2YAnpwGTuljh5wYSx1xwC0u3U7WfC_2eBW7d4oWK2GEx3aH8OYZr9eKqGqBK3uQ5ci03c_PPP1MqqqwsKh5Sv4U_V2UN6pRVIhkXgYroO0Dgalz1WWdsNZM30WVrY_XNSAbR_7qj3R15GLNXkOqgKOvf6SQYDEvUhSo7rH_JEbIz-0JOkiG6XHavjNPEPJm9DGbqO-NC69Lqb3yuTe3kzGsAvtKJS6rrn9ynwCt-JfBu_RdTVGZxAjHCkGl5iFdHlYrUGNlubIO_U1dBHxaDvrKgVmoGaCRJzOngs9DlotO78BKLy-tJ8aP0YHB4I0n3px0h1Ql3X-bbfSszvyRyhnrEPeYKoiyoOwD3ajUhEW8YXjO7nnqGCFHObpaqTfW4MizS6UlrRgRv_iR7jTa7pUqFbMcsDX-J5hE6F2HTnO0N7o4jtXrrvoUNzGNxnSNZMi5ya96LubCMvxxrBEitMBjUYYh2ljPAP83CMOOFzo1JW_yppL1pXgw5eWwyxqjcTZr4uABfV8RikpZ7_Myj68Tp7GVe_f_OsgbzXq4nk6Vf5XSB7B1_hb2eAut-0jWGB-8XPN9UY3cLwQBJ5R_qlVV9I7EmEh34MNPUbs8h7XsG25plH_FyBPI-HDI8IJtZ9PBOeumOW75khySeB5BT0mYTE9DoQdnsKuuaKTkjfncbaesGH1PAO93IobhY4FTgH1EPCr9MzSsEFjyi7q-tko-QLaj49BFB0Eb3iTwQODnCf1oUMmZLjD_9RvYbarv2COzVRenSn2cseQd8cHuTZV7ZBYn3eEpmJvuzdl2OB_e0iIIm8OdPAZBnO9CqbZLCp6Zo3bPEInSFZAwutmLcDNvzIzW9OJNxoB8U5yiONdeD7zHwG7rB0cfZpx9joFZU9DcLa65zut5z6qHVXKO-Pnyxf_xmPw0Rg0W7NCXMmfSBL5VZ0LhMdVeZkcryHfUXSmkJ8uj67T7FFDhzU6bW5o4=w1920-h1013",
                            "alt": "logo",
                            "width": "80%",
                        }
                    ),
                ),
                html.a(
                    {"href": "/simulation"},
                    html.button(
                        {
                            "class_name": "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded",
                            "style": {"background-color": "#122A4C"},
                        },
                        "Cualcular",
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
                            html.li("Haga clic en el botón 'Calcular'."),
                        ),
                    ),
                ),
            ),
        ),
    )
