from reactpy import component
from reactpy_router import route, simple

from src.screens.home import home
from src.screens.simulation import simulation
from src.screens.calculate_sample import calculate_sample


@component
def router():
    return simple.router(
        route("/", home()),
        route("/simulation", simulation()),
        route("/calculate_sample", calculate_sample()),
    )
