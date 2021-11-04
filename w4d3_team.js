function parensValid(str) {

    var open = 0;
    var closes = 0;
    var is_valid = true;
  
    for (let x=0; x<str.length; x++) {
      if (str[x] === "(") {             
        open++;                         
      }
      if (str[x] === ")") {
        closes++;
      }
  
      // if closes is greater than open, it's false
      if (closes > open) {
        is_valid = false;
        return is_valid;
      }
    }
  
    if (open != closes) {
      return false;
    } else {
      return is_valid;
    }
  }