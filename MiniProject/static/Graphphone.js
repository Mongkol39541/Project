function myFunction() {
    const ctx_1 = document.getElementById("myChart_1");
    let positive = document.getElementById(
        "positive_resultphone"
    ).value;
    let negative = document.getElementById(
        "negative_resultphone"
    ).value;
    const myChart_1 = new Chart(ctx_1, {
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