package calculate

import "testing"

func TestAverage(t *testing.T) {
	tests := []struct {
		name string
		rawData []float64
		//want float64
	}{
		{
			name: "normal mean",
			rawData: []float64{3.0, 5.0, 6.0, 2.0, 4.0},
			//want: 4.0,
		},
		{
			name: "test two",
			rawData: []float64{2, 4, 5},
		},
		{
			name: "empty slice",
			rawData: []float64{},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			Average(tt.rawData)
		})
	}
}
