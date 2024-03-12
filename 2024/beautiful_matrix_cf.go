package main

import "fmt"


// Pseudo code
/*
  1. get index of 1
  2. find distance of mid index from index of 1
  3. sum the distance (no diagonal movement hence answer)
*/

func main() {
  var val int
  var s1, s2 int  

  for i := 0; i < 5; i++ {
    for j := 0; j < 5; j++ {
      fmt.Scan(&val);

      if val == 1 {
        s1 = (2 - i);
	s2 = (2 - j); 
      }
    }	
  }

  if (s1 < 0) { 
    s1 *= -1;
  }

  if (s2 < 0) {
    s2 *= -1;
  }

  fmt.Print(s1 + s2);
}
