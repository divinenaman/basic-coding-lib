package main

import "fmt"

// Psuedo code
/*
  1. create string arr of 3 elements
  2. parse input and add number to arr using position of number
  3. concat using '+' and handle empty cases
*/

func main() {
	var input string
	arr := [3]string{"", "", ""}

	fmt.Scanln(&input)

	for _, v := range input {
		if v == '+' {
			continue
		}

		if arr[int(v-'0')-1] != "" {
			arr[int(v-'0')-1] += "+"
		}
		arr[int(v-'0')-1] += string(v)
	}

	ans := arr[0]

	if arr[1] != "" {
		if ans != "" {
			ans += "+"
		}
		ans += arr[1]
	}

	if arr[2] != "" {
		if ans != "" {
			ans += "+"
		}
		ans += arr[2]
	}
	fmt.Print(ans)
}
