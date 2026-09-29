let img;
let video;
let ascii =
    "\$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^$";
let resolution = 5

async function setup() {
    createCanvas(1900, 1050);
    // img = await loadImage("./Img/0.jpg");

    // await img.resize(width / resolution, 0);

    video = createCapture(VIDEO);
    video.size(width / resolution, height / resolution);
    
    noStroke()

}

function draw() {
    background(200);
    video.loadPixels();

    for (let i = 0; i < video.width; i++) {
        for (let j = 0; j < video.height; j++) {
            let index = (i + j * video.width) * 4;
            let r = video.pixels[index];
            let g = video.pixels[index + 1];
            let b = video.pixels[index + 2];
            let brght = (r + g + b) / 3;
            let cIndex = floor(map(brght, 0, 255, 0, ascii.length - 1));
            let c = ascii.charAt(cIndex);

            fill(r, g, b);
            text(c, i * resolution + resolution / 2, j * resolution + resolution / 2)
        }
    }
}