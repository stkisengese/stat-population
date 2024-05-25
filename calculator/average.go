package calculate

import (
	"fmt"
)

// Average takes a slice of float64 and returns the calculated mean and error.
func Average(rawData []float64) (float64, error) {
	var sum float64
	if len(rawData) == 0 {
		return 0, fmt.Errorf("no data available for processing")
	}
	for _, count := range rawData {
		sum += count
	}
	return sum / float64(len(rawData)), nil
}
