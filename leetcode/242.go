package main

func main() {
	func isAnagram(s string, t string) bool {
		counts := make(map[rune]int)

		for _, ch := range s {
			counts[ch]++
		}
		for _, ch := range t {
			counts[ch]--
			if counts[ch] < 0 {
				return false // t has too many of this character
			}
		}

		// ensure all counts are zero (anagrams should cancel out exactly)
		for _, v := range counts {
			if v != 0 {
				return false
			}
		}
		return true
	}

	isAnagram("racecar", "carrace")
}