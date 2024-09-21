const array = [5, 9, 3, 2, 4, 3, 4, 3, 9, 2];

// Step 1: Find the range
const min = Math.min(...array);
const max = Math.max(...array);

// Step 2: Create the count array
const count = new Array(max - min + 1).fill(0);

// Step 3: Count occurrences
for (const element of array) {
  count[element - min]++; // Increment the count for each element
}

// Step 4: Sort the array
const sortedArray = [];
for (let i = 0; i < count.length; i++) {
  const occurrences = count[i];
  for (let j = 0; j < occurrences; j++) {
    sortedArray.push(i + min); // Push the actual element
  }
}

console.log(sortedArray);
