var chart = am4core.create(
    "chartdiv",
    am4plugins_forceDirected.ForceDirectedTree
);

// Create series
var series = chart.series.push(
    new am4plugins_forceDirected.ForceDirectedSeries()
);

// Set data
series.data = [
    {
        name: "คู่เลขมงคล",
        children: [
            {
                name: "การเงิน",
                children: [
                    {
                        name: "78",
                        value: 687,
                    },
                    {
                        name: "87",
                        value: 148,
                    },
                    {
                        name: "26",
                        value: 687,
                    },
                    {
                        name: "62",
                        value: 148,
                    },
                    {
                        name: "28",
                        value: 687,
                    },
                    {
                        name: "82",
                        value: 148,
                    },
                    {
                        name: "39",
                        value: 687,
                    },
                    {
                        name: "93",
                        value: 148,
                    },
                ],
            },
            {
                name: "เสน่ห์",
                children: [
                    {
                        name: "26",
                        value: 148,
                    },
                    {
                        name: "42",
                        value: 687,
                    },
                    {
                        name: "36",
                        value: 148,
                    },
                    {
                        name: "24",
                        value: 687,
                    },
                    {
                        name: "22",
                        value: 148,
                    },
                    {
                        name: "66",
                        value: 687,
                    },
                ],
            },
            {
                name: "การงาน",
                children: [
                    {
                        name: "65",
                        value: 687,
                    },
                    {
                        name: "94",
                        value: 148,
                    },
                    {
                        name: "79",
                        value: 687,
                    },
                    {
                        name: "97",
                        value: 148,
                    },
                    {
                        name: "14",
                        value: 148,
                    },
                    {
                        name: "41",
                        value: 687,
                    },
                    {
                        name: "16",
                        value: 148,
                    },
                    {
                        name: "61",
                        value: 687,
                    },
                    {
                        name: "19",
                        value: 148,
                    },
                    {
                        name: "91",
                        value: 687,
                    },
                ],
            },
            {
                name: "สติปัญญา",
                children: [
                    {
                        name: "15",
                        value: 148,
                    },
                    {
                        name: "51",
                        value: 687,
                    },
                    {
                        name: "45",
                        value: 148,
                    },
                    {
                        name: "54",
                        value: 687,
                    },
                    {
                        name: "55",
                        value: 148,
                    },
                    {
                        name: "59",
                        value: 687,
                    },
                    {
                        name: "95",
                        value: 148,
                    },
                ],
            },
            {
                name: "ความรัก",
                children: [
                    {
                        name: "69",
                        value: 687,
                    },
                    {
                        name: "96",
                        value: 148,
                    },
                    {
                        name: "56",
                        value: 687,
                    },
                    {
                        name: "65",
                        value: 148,
                    },
                    {
                        name: "64",
                        value: 687,
                    },
                    {
                        name: "36",
                        value: 148,
                    },
                    {
                        name: "63",
                        value: 687,
                    },
                    {
                        name: "26",
                        value: 148,
                    },
                    {
                        name: "62",
                        value: 687,
                    },
                    {
                        name: "16",
                        value: 148,
                    },
                    {
                        name: "61",
                        value: 148,
                    },
                ],
            },
        ],
    },
];

// Set up data fields
series.dataFields.value = "value";
series.dataFields.name = "name";
series.dataFields.children = "children";

// Add labels
series.nodes.template.label.text = "{name}";
series.fontSize = 18;
series.minRadius = 30;
series.maxRadius = 100;

series.centerStrength = 0.5;
series.links.template.distance = 1.5;