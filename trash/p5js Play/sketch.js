let walker;

function setup() {
    createCanvas(900, 600);
    background(200);
    walker = new Walker();
    frameRate(144);
}


class Walker {
    constructor() {
        this.x = width / 2;
        this.y = height / 2;
    }

    show(r) {
        circle(this.x, this.y, r);
    }

    step(size) {
        let xStep = random(1) < 0.5 ? (mouseX > this.x ? 1 : -1) : floor(random(3) - 1) * size;
        let yStep = random(1) < 0.5 ? (mouseY > this.y ? 1 : -1) : floor(random(3) - 1) * size;

        this.x += xStep;
        this.y += yStep;
    }
}

function draw() {

    walker.show(1);
    walker.step(1);
 
}
