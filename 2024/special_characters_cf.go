package main

import "fmt"

// Complexity : n/2
// Psuedo code
/*
  1. Special number need atleast one pair of consecutively repeated letters
  2. Consecutively repeated letters gives us exactly 2 special numbers
  3. Odd number of special numbers cannot be achived because of point 2
*/

func main() {

	var t int

	fmt.Scanln(&t)

	inp := make([]int, t)

	for i := 0; i < t; i++ {
		fmt.Scanln(&inp[i])
	}
	for i, n := range inp {
		if i != 0 {
			fmt.Println()
		}
		if n%2 != 0 {
			fmt.Print("NO")
		} else {
			ch := 65
			offset := 0
			fmt.Println("YES")

			for j := 1; j <= (n / 2); j++ {
				fmt.Print(string(ch+offset) + string(ch+offset))
				offset++

				// max 27 alphabets
				offset %= 28
			}
		}
	}
}
