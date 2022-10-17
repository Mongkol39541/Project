function myFunction_2() {
    const ctx_2 = document.getElementById("myChart_2");
    let positive =
        document.getElementById("positive_resultcar").value;
    let negative =
        document.getElementById("negative_resultcar").value;
    const myChart_2 = new Chart(ctx_2, {
        type: "doughnut",
        data: {
            labels: ["ผลบวก", "ผลลบ"],
            datasets: [
                {
                    label: "# of Votes",
                    data: [positive, negative],
                    backgroundColor: [
                        "rgb(255, 99, 132)",
                        "rgb(54, 162, 235)",
                    ],
                    hoverOffset: 4,
                },
            ],
        },
    });
}