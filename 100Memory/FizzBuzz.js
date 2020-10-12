

let number = 1;
while (number <= 100) {

//prints FizzBuzz if divisible by both 3 and 5
  if (number%3 == 0 && number%5 == 0) {
  console.log("FizzBuzz");
  number = number+1;
  }
//prints Fizz if divisible by 3
  if (number%3 == 0) {
  console.log("Fizz");
  number = number+1;
  }
//prints Buzz if divisible by 5
  if (number%5 == 0) {
  console.log("Buzz");
  number = number+1;
  }
//prints integer if none applies
  else {
  console.log(number);
  number = number + 1;
  }
}
