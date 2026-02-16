package main

func main() {
	func containsDuplicate(nums []int) bool{
    	seen := make(map[int]struct{}, len(nums))

		for _, n := range nums {
			if _, exists := seen[n]; okay {
				seen[n] = struct{}{}
			}
		}

		return false
	}

	containsDuplicate([1,2,3,3])
}