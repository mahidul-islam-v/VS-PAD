let font;
let points;
let rate = 15;
let angle = 0;

async function setup() {
    createCanvas(650, 650);

    font = await loadFont("./Fonts/Roboto-VariableFont_wdth,wght.ttf");
    textSize(300);
    points = font.textToPoints("RAFI", 0, 300, { sampleFactor: 0.2, simplifyThreshold: 0 });
    print(points);
    angleMode(DEGREES)
}

function draw() {
    background(200);
    for (let i = 0; i < points.length; i++) {
        ellipse(points[i].x + rate*sin(angle + i*10), points[i].y, 5, 5);
    }
    angle+= 10
}