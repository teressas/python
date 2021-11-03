/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

  const str1 = "aaaabbcddd";
  const expected1 = "a4b2c1d3";
  
  
  const str2 = "";
  const expected2 = "";
  
  const str3 = "a";
  const expected3 = "a";
  
  const str4 = "bbcc";
  const expected4 = "bbcc";
  
  const str5 = "aaaabbaaacddd";
  const expected5 = "a4b2a3c1d3";
  /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs only if the
   * character occurs more than two time.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   */
  function encodeStr(str) {}
  
  // ***********************************************
  
  /* 
    String Decode  
  */
  
  const two_str1 = "a3b2c1d3";
  const two_expected1 = "aaabbcddd";
  
  const two_str2 = "a3b2c12d10";
  const two_expected2 = "aaabbccccccccccccdddddddddd";
  
  /**
   * Decodes the given string by duplicating each character by the following int
   * amount if there is an int after the character.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str An encoded string with characters that may have an int
   *    after indicating how many times the character occurs.
   * @returns {string} The given str decoded / expanded.
   */
  function decodeStr(str) {}


  // def function
// make var for letter
// make varnext letter
// make var for newstring
// counter for letters
// loop through the string
// check letter if they are ==
// += the letter into our new string
// += value of the counter
// then reset the counter





function encodeString(str){
  var letter = ""
  var nextletter = ""
  var newstring = ""
  var counter = 1
  for( var i=0; i<str.length; i++){
      letter = str[i];
      nextletter = str[i+1];
      // console.log(letter);
      // console.log(nextletter);
      if(letter == nextletter){
          counter+=1;
          // console.log(counter)
      }
      else {
          newstring += letter;
          newstring += counter;
          letter = "";
          counter = 1;


      }
  }
  if(newstring.length >= str.length){
      newstring = str;

  }
  console.log(newstring)
}



var str2 = "aabb"
var str1 = "aaaabbcddd"
encodeString(str2)
encodeString(str1)

// def function
// make var for letter
// make var nextspace 
// loop through string
// check if letter is a string and if nextspace is an int
// if so print letter nextspace times 


function decodeString(str){
  var letter = "";
  var nextspace = 0;
  for(var i=0; i<str.length; i++){
      letter = str[i];
      nextspace = str[i+1];
      if(nextspace > 0){
          console.log(nextspace)
      }
  }


}

str3 = "a4b2"

decodeString(str3)