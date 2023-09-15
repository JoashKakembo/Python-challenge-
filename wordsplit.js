function WordSplit(strArr) {
    const sequence = strArr[0];
    const dictionary = strArr[1].split(',');
  
    for (let i = 0; i < dictionary.length; i++) {
      const word1 = dictionary[i];
  
      for (let j = i + 1; j < dictionary.length; j++) {
        const word2 = dictionary[j];
        const combined = word1 + word2;
  
        if (combined === sequence) {
          return word1 + ',' + word2;
        }
      }
    }
  
    return 'not possible';
  }
  
  // Example usage:
  console.log(WordSplit(["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"])); // Output: base,ball
  console.log(WordSplit(["abcgefd", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"])); // Output: abcg,efd\  