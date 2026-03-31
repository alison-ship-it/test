/**
 * Assorted helper functions (JavaScript).
 */

/**
 * Capitalize the first letter of a string.
 * @param {string} str
 * @returns {string}
 */
function capitalize(str) {
  if (!str) return "";
  return str.charAt(0).toUpperCase() + str.slice(1);
}

/**
 * Deep-clone a plain object or array using JSON round-trip.
 * @param {*} obj
 * @returns {*}
 */
function deepClone(obj) {
  return JSON.parse(JSON.stringify(obj));
}

/**
 * Return a new array with duplicate values removed.
 * @param {Array} arr
 * @returns {Array}
 */
function unique(arr) {
  return [...new Set(arr)];
}

/**
 * Simple debounce implementation.
 * @param {Function} fn
 * @param {number} ms - delay in milliseconds
 * @returns {Function}
 */
function debounce(fn, ms) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), ms);
  };
}

module.exports = { capitalize, deepClone, unique, debounce };
