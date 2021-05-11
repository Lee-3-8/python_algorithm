function solution(array, commands) {
  const result = commands.map((v)=>{
      const [i,j,k] = v
      return array.slice(i-1,j).sort((a,b)=>a-b)[k-1]
  })
  return result
}
console.log('test')
