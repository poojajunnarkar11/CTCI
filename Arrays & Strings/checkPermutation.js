//checking case sensitive permutation and considering whitespace
const checkPermutation = (string1, string2) => {
  return string1.split('').sort().join('') === string2.split('').sort().join('')
}

console.log(checkPermutation('onion', 'oNOni'))
