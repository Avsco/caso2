from reactpy import component, html
from reactpy_router import link


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
                            "src": "https://lh3.googleusercontent.com/fife/AK0iWDwRivoMS_fvpF997Xt6gTtoXwvhpYADtMcl8XmyGHSiYOr_ztFgz8itKSkjhm31yl4_Y3EXV9-h45wVDnwDzNMrRKaQKK52Oz9y2EzO6E-1hs9j8c5qpt4Cj3bKxCM41ymHRH8S45YDVAiitSEUoXKW6Ok_hcUITDcufPAQVt84G77LP2ZFXphCSXmFsh4SyaMR5wESdBvstMePruM1qqGkmAHttc2jPB7L415uodOerGW6tDw30VBtPbncTV7GUNZ3C2nnkjGwZTzODoBAZ65jnGyUD_BoH8zUB2g6J4xWruSA_8ne7dcI2tMuqHuxhiEOjI9AseaUqW2yRrui9oiUHdGShKf8GLqXbdH2D0zbS8vgQyLlo893xC9pL4U6xJutix9TE65TNisRxAlx00BrTn7jPvF0wBHp1e3seHYg8gywlAYgLQ7UT596tZ0rdU-q-e2f0u6HjHk95XeeNzcMnT4yc_l-m9IVBdmlb4T67PHZu3EFDGWHh7Y-Ar3MTme2uWMJ7R1LEwCDgHyvbirCV_9RXB1St0ov3LWJ9tVMwYr8MNmhKjY0KN-OmrXCVvtVoLLRMkbi6qt9IkJ7o75pRr6arVyP1_IY1aLMFosDduR_rMQ-F1F23wD1_4-PxjmjyOe1rY814ejK6GWNn_WYC8nz0Be3o2pZh0kNs3TCgZiKztTLM0wNkvI8oaiUwmwGuRImoJpNFyIOkd__LVqxI_V1Km_Dp97135MM1VotyFOd2r1sXqYWEEsCLee_8ZA9y5guRZF4ElPzTfkl3wkQHdJ08WIMpaD_Wgud74pkz6i5lA5Ms-lk5vI2nkaqFV-17i6h8D4EsnY8mQx1MoB_EDIJmwVFB64A2PkbAHdzvKMa64qFRLN49WNOtIgw6zhoGIEFXSixAG6bxkEYyKZIjYPRmU_WrIgJTublB2oInYffbHg2OWZzfyh1MK_8BIpjSwIwId7KYP2vd11-6xYGRKMWOwcjvxfZ8RY_-2D72ow2IfUNs6TEjbX_PbDwJ_QQeYhccuV7sNur02PSS5TyB4fdvXfhJsYTV9ZqEoQy6L2Zd-5ck2w5JR4C15QOYNC2K7M4ggkqH4IAhYNs_AuWbqQFFUkVNmvHDaVaZ_OdsJX444Jpv5zWGc4bF9TBVpP2-MsLJjGYdVSpjK-YES0cwBfsncdP-5HNVG69JJSr_Az_UhUlKtarf04R0iI8y2k4sYMVYln2VjxMWa7sqJx2P42Y5iVhMDd6KNi8sG_L7KuGGPkNb_ooXdVAbEs-xj-UUvaTzI3FnOEsehFmlTjkLjNAQ4FGAjSCZWETSkh3Rh1ecfDGobrbqwrvist075Yck41P1fyrw-Kavu2sFKs97LncEzZAnh7MTw5LbkFmz6dF5D5wieuNBB5Di3CQjZgBExzh5YkviS-WiIsg9F2uBqy-KGZy5u0VPwoca2qsoZh_VIkAajV7qKnIyagezc0kkGBNhiyiZor0g2cMwvMCyuLsWXFsrwmll9wkbhYWMpTQmobXnwZwfQ=w958-h987",
                            "alt": "logo",
                            "width": "80%",
                        }
                    ),
                ),
                html.button(
                    {
                        "class_name": "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded",
                        "onclick": "window.location.href='/calculate_sample'",
                        "style": {"background-color": "#122A4C"},
                    },
                    link(
                        "Iniciar simulación",
                        to="/simulation",
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
