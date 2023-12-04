from reactpy import component, html

from src.layout.main_layout import main_layout
from src.router.router import router


@component
def app_element():
    return html.div({"class_name": "h-full"}, main_layout(router()))
