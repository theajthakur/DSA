const array = [-232, 83, 2, -21, 4, 59, 38, -1, 48, -28];

for (let i = 0; i < array.length - 1; i++) {
  let minIndex = i; // Assume the minimum is the first element of the unsorted part

  // Find the index of the smallest element in the unsorted part
  for (let j = i + 1; j < array.length; j++) {
    if (array[j] < array[minIndex]) {
      minIndex = j; // Update minIndex if a smaller element is found
    }
  }

  // Swap the found minimum element with the first element of the unsorted part
  if (minIndex !== i) {
    const temp = array[i];
    array[i] = array[minIndex];
    array[minIndex] = temp;
  }
}

console.log(array);
