function solution(participant, completion) {
  const obj1 = {};
  
  participant.forEach(v => {
      obj1[v] = obj1[v] ? obj1[v] + 1 : 1
  });
  completion.forEach(v => {
      obj1[v] = obj1[v] - 1
  });
  
  for (let key in obj1){
      if (obj1[key] === 1){
          return key;
      }
  }
}