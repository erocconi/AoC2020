package main

import (
	"os"
	"log"
	"fmt"
	"bufio"
)

func main() {
	// Open file and create scanner on top of it
	file, err := os.Open("./input/d1.txt")
	if err != nil {
		log.Fatal(err)
	}
	scanner := bufio.NewScanner(file)
}
