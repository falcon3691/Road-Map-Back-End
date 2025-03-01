function loadForm(page) {
    document.getElementById('form-frame').src = page;
}

function convertLength() {
    let inputValue = parseFloat(document.getElementById("lengthValue").value);
    let fromUnit = document.getElementById("fromLength").value;
    let toUnit = document.getElementById("toLength").value;
    
    const lengthConversions = {
        millimeter: 0.001,
        centimeter: 0.01,
        meter: 1,
        kilometer: 1000,
        inch: 0.0254,
        foot: 0.3048,
        yard: 0.9144,
        mile: 1609.34
    };
    
    let result = (inputValue * lengthConversions[fromUnit]) / lengthConversions[toUnit];
    displayResult(result, toUnit);
}

function convertWeight() {
    let inputValue = parseFloat(document.getElementById("weightValue").value);
    let fromUnit = document.getElementById("fromWeight").value;
    let toUnit = document.getElementById("toWeight").value;
    
    const weightConversions = {
        milligram: 0.001,
        gram: 1,
        kilogram: 1000,
        ounce: 28.3495,
        pound: 453.592
    };
    
    let result = (inputValue * weightConversions[fromUnit]) / weightConversions[toUnit];
    displayResult(result, toUnit);
}

function convertTemperature() {
    let inputValue = parseFloat(document.getElementById("temperatureValue").value);
    let fromUnit = document.getElementById("fromTemperature").value;
    let toUnit = document.getElementById("toTemperature").value;
    let result;
    
    if (fromUnit === "celsius" && toUnit === "fahrenheit") {
        result = (inputValue * 9/5) + 32;
    } else if (fromUnit === "fahrenheit" && toUnit === "celsius") {
        result = (inputValue - 32) * 5/9;
    } else if (fromUnit === "celsius" && toUnit === "kelvin") {
        result = inputValue + 273.15;
    } else if (fromUnit === "kelvin" && toUnit === "celsius") {
        result = inputValue - 273.15;
    } else if (fromUnit === "fahrenheit" && toUnit === "kelvin") {
        result = (inputValue - 32) * 5/9 + 273.15;
    } else if (fromUnit === "kelvin" && toUnit === "fahrenheit") {
        result = (inputValue - 273.15) * 9/5 + 32;
    } else if (fromUnit == toUnit){
        result = inputValue;
    }
    
    displayResult(result, toUnit);
}

function displayResult(result, unit) {
    document.getElementById("result-text").innerText = `${result.toFixed(4)} ${unit}`;
    document.getElementById("result-container").style.display = "block";
}

function reset() {
    document.getElementById("result-container").style.display = "none";
}
