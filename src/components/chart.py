from reactpy import component, html


@component
def chart(interferences: int = 0, total: int = 0):
    return html.div(
        {
            "class_name": "show-print h-52",
        },
        html.script(
            """
            let myChart
            let interferences
            let total

            setTimeout(() => {
                let canvas = document.querySelector('#myDoughnutChart');
                const vars = document.querySelector('#vars');

                var observer = new MutationObserver(function(mutations) {
                    mutations.forEach(function(mutation) {
                        if (mutation.type === "attributes") {
                        
                            interferences = Number(vars.dataset.interferences);
                            total = Number(vars.dataset.total) - interferences;
                            
                            const ctx = canvas.getContext('2d');

                            if (myChart) {
                                myChart.destroy();
                            }

                            myChart = new Chart(ctx, {
                                type: 'doughnut',
                                data: {
                                    labels: ['Interferencias', 'No interferencias'],
                                    datasets: [{
                                        data: [interferences, total],
                                        backgroundColor: ['#122A4C', '#B9B9B9'],
                                    }]
                                },
                                options: { }
                            });    
                        }
                    });
                });

                observer.observe(vars, { attributes: true });
            }, 1000);
            """
        ),
        html.div(
            {
                "class_name": "display-none",
                "id": "vars",
                "data-interferences": interferences,
                "data-total": total,
            },
        ),
        html.canvas(
            {
                "class_name": "m-auto",
                "id": "myDoughnutChart",
                "height": "100",
                "max-height": "100",
            },
        ),
    )
