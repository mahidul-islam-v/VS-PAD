function setup() {
  createCanvas(600, 600)
  frameRate(144);
  angleMode(DEGREES)
}

let x = 600
let y = 200
let ellipseX = 30
let ellipseY = 30
let xDir = 1
let yDir = 1
let xSpeed = 1
let ySpeed = 1
let rotor = 0;
function speedChange() {
    xSpeed = Math.ceil(Math.random() * 10);
    ySpeed = Math.ceil(Math.random() * 10);
}


function draw() {
  colorMode(RGB, 255);
  background(200, 75);
  console.log(frameCount);

  noStroke()
  
  fill(20, 20, 20);
  ellipse(x, y, ellipseX, ellipseY);

  
  
  // xDir = x + ellipseX > width ? -1 : 1;

  // yDir = y + ellipseY > height ? -1 : 1;

  if (x + ellipseX/2 > width) {
    xDir = -1;
    speedChange();
  } else if (x - ellipseY/2 < 0) {
    xDir = 1;
    speedChange();
  }
  
  if (y + ellipseY/2 > height) {
      yDir = -1;
    speedChange();
  } else if (y - ellipseY/2 < 0) {
      yDir = 1;
    speedChange();
  }

  x += 1*xDir*xSpeed
  y += 1*yDir*ySpeed

  stroke(255, 255, 255);
  strokeWeight(6);

  rectMode(CENTER);
  // noFill()
  noFill()
  rect(width / 2, height / 2, 100, 140);
  
  stroke(0);
  strokeWeight(1);
  rect(width / 2, height / 2, 100 - 6, 140 - 6);

  stroke(0);
  strokeWeight(1);
  rect(width / 2, height / 2, 100 + 6, 140 + 6);


  let mx = mouseX;
  let my = mouseY;
  let colorx = map(mx, 0, width, 50, 255)
  let colory = map(my, 0, height, 50, 255)


  stroke(colorx, colory, 0);
  if (mouseIsPressed) {
    rotor += 1 * (xSpeed + ySpeed)/2;
    translate(mx, my)
    rotate(rotor);
    mx = 0
    my = 0
    stroke((255 * x) / 600, (255 * y) / 600, 0);
  }
  strokeWeight(50)
  line(mx - 30, my - 2, mx + 30, my - 2);
  
}


