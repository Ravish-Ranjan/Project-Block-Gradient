function hexToHSL(hex) {
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    r = parseInt(result[1], 16);
    g = parseInt(result[2], 16);
    b = parseInt(result[3], 16);
    r /= 255, g /= 255, b /= 255;
    var max = Math.max(r, g, b), min = Math.min(r, g, b);
    var h, s, l = (max + min) / 2;
    if(max == min){
        h = s = 0; 
    }
    else{
        var d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        switch(max){
            case r: h = (g - b) / d + (g < b ? 6 : 0); break;
            case g: h = (b - r) / d + 2; break;
            case b: h = (r - g) / d + 4; break;
        }
        h /= 6;
    }
    var HSL = new Object();
    HSL['h']=Math.round(h*360);
    HSL['s']=s.toFixed(2);
    HSL['l']=l.toFixed(2);
    return HSL;
}

let from_ = document.getElementById('from');
let to = document.getElementById('to');

const HEXer = (color) => {
    const hexadecimal = color.toString(16);
    return hexadecimal.length == 1 ? "0" + hexadecimal : hexadecimal;
}

const RGBtoHex = (red, green, blue) => {return "#"+HEXer(red)+HEXer(green)+HEXer(blue);}

function gradientSet(fromcolor,tocolor) {
    divi = document.getElementsByClassName('color-range')[0];
    divi.style.backgroundImage = `linear-gradient(to bottom,${fromcolor},${tocolor})`;
}

function randnum(){ return Math.floor(Math.random() * 255);}

function randgen() {
    fromcol = RGBtoHex(randnum(),randnum(),randnum());
    tocol = RGBtoHex(randnum(),randnum(),randnum());
    gradientSet(`${fromcol}`,`${tocol}`);
    from_.value = fromcol;
    to.value = tocol;
}
function rangeSet() {
    document.getElementById('custsize').value = document.getElementById('size').value;
}

async function getInputs() {
    from_color = hexToHSL(from_.value);
    to_color = hexToHSL(to.value);
    rangeInp = document.getElementById('size').value;
    numInp = document.getElementById('custsize').value;
    blockNo = parseInt(numInp == "" ? rangeInp : numInp);
    resp = { from_color, to_color, blockNo }
    const loc = window.location.href;
    let response = await fetch(loc + "blocks?" + (new URLSearchParams({data:JSON.stringify(resp)})),{ method: "GET", mode: "cors" } )
    response = await response.json()
    response = JSON.parse(response.blocks[0].replaceAll(/'+/g, "\""))
    console.log(response)
    const output = document.getElementById("output");
    response.forEach(img => {
        temp = document.createElement("img")
        temp.setAttribute("src", img)
        temp.setAttribute("alt", "loading image")
        output.appendChild(temp)
    });
    console.log(response);
}
randgen();
