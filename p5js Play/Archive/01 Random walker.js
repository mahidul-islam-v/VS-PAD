function setup() {
    createCanvas(600, 600)
    walker = new Walker()
    background(200)
}

function draw() {
    walker.show(50)
    walker.step(3)
}

class Walker {
    constructor() {
        this.x = width / 2
        this.y = height / 2
    }

    show(rads) {
        let rad = rads
        stroke(0)
        circle(this.x, this.y, rad)
    }

    step(incrs) {
        let choice = floor(random(4))
        let incr = incrs

        if (choice == 0) {
            this.y+= incr;
        } else if (choice == 1) {
            this.x += incr;
        } else if (choice == 2) {
            this.y -= incr;
        } else {
            this.x -= incr;
        }
    }
}