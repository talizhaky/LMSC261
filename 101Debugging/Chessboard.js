//defines size of chessboard
var size = 8;
const bird = " #"
const frog = "# "

//controls height of chessboard
for (number=1; number <= size; number = number + 1) {
  if (number%2==0) {
    console.log(bird.repeat(4));
  }

  else {
    console.log(frog.repeat(4));
  }
}
