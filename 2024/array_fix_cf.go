package main

import "fmt"

// Complexity : 2 * n
// Patterns
/*
  1. If element at i can be transformed as non-decreasing digits, elem at i-1 should also. As an individual digit can only be less than another digit.
  2. For each element 3 cases occur :
    a. i-1 & i are ordered naturally
    b. transform(i - 1) & transform(i) are ordered
    c. transform(i - 1) & i are ordered
*/

func main() {

	var t, n int

	fmt.Scanln(&t)

	ans := make([]bool, t)

	for i := 0; i < t; i++ {
		fmt.Scanln(&n)

		prev_val := 0
		var curr int
		isOrdered, canSeparate := true, true

		for j := 1; j <= n; j++ {
			fmt.Scan(&curr)

			if curr < prev_val && (canSeparate == false || (curr < prev_val%10)) {
				isOrdered = false
			}

			curr_val := curr
			prev := curr % 10
			curr /= 10

			for curr > 0 {
				val := curr % 10

				if val > prev {
					canSeparate = false
					break
				}

				curr /= 10
				prev = val

			}

			if canSeparate && prev < (prev_val%10) {
				canSeparate = false
			}
			prev_val = curr_val
		}
		ans[i] = canSeparate || isOrdered
	}

	for idx, i := range ans {
		if idx != 0 {
			fmt.Println()
		}
		if i {
			fmt.Print("YES")
		} else {
			fmt.Print("NO")
		}
	}
}
