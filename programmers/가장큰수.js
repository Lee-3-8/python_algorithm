function isBigger(a,b){
  const n = Math.max(a.length,b.length)
  for ( let i = 0; i<n; i++){
      const x = a[i] !== undefined ? a[i] : a[a.length - 1]
      const y = b[i] !== undefined ? b[i] : b[b.length - 1]
      if (x == y) continue;
      else return x > y ? -1 : 1
  }
  return 1
}

function solution(numbers) {

  // const result =  numbers.map(String).sort(isBigger).join("")
  const result =  numbers.map(String).sort(isBigger)

  return result ? result : '0'
}

console.log(solution( [90,908,89,898,10,101,1,8,9]))
