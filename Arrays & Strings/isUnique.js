const isUnique = myString => {
  if (myString.length > 128) return false
  let myTrackerArray = []
  for (var i = 0; i < 128; i++) {
    myTrackerArray[i] = false
  }
  for (var index = 0; index < myString.length; index++) {
    const myCharCode = myString.charCodeAt(index)
    if (myTrackerArray[myCharCode] === true) {
      return 'Not Unique'
    } else {
      myTrackerArray[myCharCode] = true
    }
  }
  return 'Unique'
}

const myString = 'abaa'
console.log(isUnique(myString))
