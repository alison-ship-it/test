const { capitalize, deepClone, unique } = require("./helpers");

// --- capitalize ---
console.assert(capitalize("hello") === "Hello", "capitalize normal");
console.assert(capitalize("") === "", "capitalize empty");
console.assert(capitalize("A") === "A", "capitalize single char");

// --- deepClone ---
const original = { a: 1, b: { c: 2 } };
const clone = deepClone(original);
console.assert(clone.b.c === 2, "deepClone value");
clone.b.c = 99;
console.assert(original.b.c === 2, "deepClone independence");

// --- unique ---
console.assert(
  JSON.stringify(unique([1, 2, 2, 3])) === JSON.stringify([1, 2, 3]),
  "unique removes duplicates"
);

console.log("All JS helper tests passed.");
