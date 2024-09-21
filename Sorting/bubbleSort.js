const array = [5, 2, 84, 21, -43, 9, 32, -54, 35];
let picked;
const startTime = Date.now();
for (let ind = 0; ind < array.length; ind++) {
  for (let index = 1; index < array.length; index++) {
    picked = array[index - 1];
    const element = array[index];
    if (picked > element) {
      array[index - 1] = element;
      array[index] = picked;
    }
  }
}

console.log(JSON.stringify(array));
console.log(`It took ${Date.now() - startTime} milliseconds`);
