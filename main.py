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

google_apis = html.link(
    {
        "rel": "preconnect",
        "href": "https://fonts.googleapis.com",
    }
)

g_static = html.link(
    {
        "rel": "preconnect",
        "href": "https://fonts.gstatic.com",
        "crossorigin": "true",
    }
)

font = html.link(
    {
        "href": "https://fonts.googleapis.com/css2?family=Inter&family=Noto+Sans+Hebrew:wght@100&display=swap",
        "rel": "stylesheet",
    }
)

generate_report = html.script(
    """document.querySelector("[name=report]")
        .addEventListener("click", () => {
            window.print();
        })
    """
)

main_css = html.style(
    """
    .table_x {
        max-height: 24rem;
    }

    .column-temp {
        flex-direction: row;
    }

    @media print {
        .hidden-print {
            display: none !important;
        }

        .table_x {
            max-height: unset;
        }

        .column-temp {
            flex-direction: column !important;
        }
    }
    """
)


@component
def root():
    return html.div(
        {
            "class_name": "flex flex-col gap-8 min-h-screen p-0 min-w-full font-Inter",
        },
        tailwind,
        google_apis,
        g_static,
        font,
        generate_report,
        main_css,
        app_element(),
    )


configure(app, root)
