const URLify = str => {
  return str.split(' ').join('%20')
}

console.log(URLify('My John Doe'))
