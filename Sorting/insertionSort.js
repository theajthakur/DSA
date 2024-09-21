const array = [21, -64, 28, 74, 4, 9, -42, -47, 28, 20];

for (let index = 1; index < array.length; index++) {
  const element = array[index];

  let j = index - 1;
  while (j >= 0 && array[j] > element) {
    array[j + 1] = array[j];
    j--;
  }
  array[j + 1] = element;
}

console.log(JSON.stringify(array));
