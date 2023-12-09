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

# inside => reactpy.backend._common.CommonOptions
# html.script(
#     {
#         "type": "module",
#          "src": "https://cdn.jsdelivr.net/npm/chart.js@4.3.0/dist/chart.umd.min.js",
#         "crossorigin": "anonymous",
#         "referrerpolicy": "no-referrer",
#     }
# ),
# html.script(
#     """
#         let myChart
#         let interferences
#         let total

#         setTimeout(() => {
#             let canvas = document.querySelector('#myDoughnutChart');
#             const vars = document.querySelector('#vars');

#             var observer = new MutationObserver(function(mutations) {
#                 mutations.forEach(function(mutation) {
#                     if (mutation.type === "attributes") {

#                         interferences = Number(vars.dataset.interferences);
#                         total = Number(vars.dataset.total) - interferences;

#                         const ctx = canvas.getContext('2d');

#                         if (myChart) {
#                             myChart.destroy();
#                         }

#                         myChart = new Chart(ctx, {
#                             type: 'doughnut',
#                             data: {
#                                 labels: ['Interferencias', 'No interferencias'],
#                                 datasets: [{
#                                     data: [interferences, total],
#                                     backgroundColor: ['#122A4C', '#B9B9B9'],
#                                 }]
#                             },
#                             options: { }
#                         });
#                     }
#                 });
#             });

#             observer.observe(vars, { attributes: true });
#         }, 1000);
#     """
# )

main_css = html.style(
    """
    .table_x {
        max-height: 24rem;
    }

    .column-temp {
        flex-direction: row;
    }

    .show-print {
        overflow: hidden;
    }

    @media print {
        .hidden-print {
            display: none !important;
        }

        .show-print {
            overflow: visible;
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
        html.head(
            tailwind,
            google_apis,
            g_static,
            font,
            generate_report,
            main_css,
        ),
        app_element(),
    )


configure(app, root)
