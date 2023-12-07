package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func toNums(fields []string) []int {
	il := make([]int, len(fields))

	for i, s := range fields {
		il[i], _ = strconv.Atoi(strings.TrimSpace(s))
	}

	return il
}

func getCombos(t int, d int) int {
	c := 0

	for i := 0; i < t; i++ {
		if i*(t-i) > d {
			c = c + 1
		}
	}

	return c
}

func processFile(fn string) {
	body, _ := os.ReadFile(fn)
	text := string(body)

	lines := strings.Split(text, "\n")

	time, _ := strconv.Atoi(strings.Replace(strings.Split(lines[0], ": ")[1], " ", "", -1))
	distance, _ := strconv.Atoi(strings.Replace(strings.Split(lines[1], ": ")[1], " ", "", -1))

	fmt.Println(time, distance)

	fmt.Printf("Total combos: %v", getCombos(time, distance))
}

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintf(os.Stderr, "missing input filename\n")
		os.Exit(1)
	}

	processFile(os.Args[1])
}
