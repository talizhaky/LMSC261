
//controls height of chessboard
for (number=1; number <= size; number = number + 1) {

//defines size of chessboard
  var size = 11;
  const bird = " #"
  const frog = "# "

  if (number%2==0) {
    console.log(bird.repeat(size/2));
  }

  else {
    console.log(frog.repeat(size/2));
  }
}
