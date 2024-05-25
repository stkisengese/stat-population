package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	calc "calculate/calculator"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Incorrect number of arguments")
	}
	// read the file content
	data, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	populationData := strings.Fields(string(data))
	rawData := make([]float64, 0, len(populationData))
	// convert each string in the slice to a float and store in rawData
	for _, strData := range populationData {
		if strData != "" {
			number, err := strconv.ParseFloat(strData, 64)
			if err != nil {
				fmt.Println("Error parsing float:", err)
				continue
			}
			rawData = append(rawData, number)

		}
	}
	fmt.Println(rawData)
	// Handle errors as we calculate the average
	avg, err := calc.Average(rawData)
	if err != nil {
		fmt.Println("Error calculating average:", err)
	}
	fmt.Println(int(avg))
}
