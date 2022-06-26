const TheList = [];
const TheOutlier = [];

function InputList(value) {
    TheList.push(parseInt(value));
    TheList.sort((function(a, b){return a - b}));
    document.getElementById("ShowData").innerHTML = "Data : "+TheList;
    document.getElementById("NumberData").innerHTML = "Number : "+TheList.length;
}

function OurputList(value) {
    TheList.splice(parseInt(value-1), 1);
    TheList.sort((function(a, b){return a - b}));
    document.getElementById("ShowData").innerHTML = "Data : "+TheList;
    document.getElementById("NumberData").innerHTML = "Number : "+TheList.length;
}

function Quartile(){
    INTList =  TheList.length
    Q01 = (INTList+1)/4
    Q02 = (INTList+1)*(2/4)
    Q03 = (INTList+1)*(3/4)
    Q1 = parseInt(TheList[Q01-1])
    Q2 = parseInt(TheList[Q02-1])
    Q3 = parseInt(TheList[Q03-1])
    document.getElementById("ShowQuartile1").innerHTML = "Q1 = "+Q1;
    document.getElementById("ShowQuartile2").innerHTML = "Q2 = "+Q2;
    document.getElementById("ShowQuartile3").innerHTML = "Q3 = "+Q3;
    Check1 = Q1-1.5*(Q3-Q1)
    Check2 = Q3+1.5*(Q3-Q1)
    for(var j = 0;j < INTList ; j++){
        if(TheList[j]<Check1){TheOutlier.push(TheList[j])}
        if(TheList[j]>Check2){TheOutlier.push(TheList[j])}
    }
    TheOutlier.sort();
    document.getElementById("ShowOutlier").innerHTML = "Outlier : "+TheOutlier;
    Average()
}

function Average() {
    Sum = 0
    for(var z1 = 0;z1 < INTList ; z1++){
        Sum += parseInt(TheList[z1])
    }
    Av1 = Sum/INTList
    Total = Sum
    INTOutlier = TheOutlier.length
    for(var z2 = 0;z2 < INTOutlier ; z2++){
        Total -= parseInt(TheOutlier[z2])
    Av2 = Total/(INTList-INTOutlier)
    }
    document.getElementById("ShowAverage1").innerHTML = "Average = "+Av1.toFixed(2);
    document.getElementById("ShowAverage2").innerHTML = "Average(Delete Outlier) = "+Av2.toFixed(2);
    console.log(TheList.median())
}