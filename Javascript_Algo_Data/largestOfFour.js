function largestOfFour(arr) {
  let newArr=[]
  for (let i=0; i<=arr.length;i++){
    if (arr[i]!=undefined){
      newArr.push(Math.max(...arr[i]))
      //console.log(newArr)
    }
  }
  return newArr;
}

//largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
largestOfFour([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]])
