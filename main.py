from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure

from src.app import app_element

app = FastAPI()

tailwind = html.link(
    {
        "rel": "stylesheet",
        "href": "https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.7/tailwind.min.css",
    }
)


@component
def root():
    return html.div(
        {"class_name": "flex flex-col gap-8 container min-h-screen p-4 min-w-full"},
        tailwind,
        app_element(),
    )


configure(app, root)
