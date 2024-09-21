const quickSort = (array) => {
  if (array.length <= 1) {
    return array; // Base case: an array of zero or one element is sorted
  }

  const pivot = array[array.length - 1]; // Choose the last element as the pivot
  const left = []; // Elements less than the pivot
  const right = []; // Elements greater than the pivot

  // Partitioning
  for (let i = 0; i < array.length - 1; i++) {
    if (array[i] < pivot) {
      left.push(array[i]);
    } else {
      right.push(array[i]);
    }
  }

  // Recursively sort left and right, and combine
  return [...quickSort(left), pivot, ...quickSort(right)];
};

const array = [21, 32, 31, -32, 94, 8, 88];
const sortedArray = quickSort(array);
console.log(sortedArray);
