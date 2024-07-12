# Statistical Population Calculator

This Program is written in python, calculates basic statistics (average, median, variance, and standard deviation) for a population data set stored in a text file.

## Features:

- Reads population data from a text file.
- Handles errors gracefully:
    - Identifies and reports non-existent files.
    - Detects lines containing non-numeric characters.
- Calculates basic statistics using the `statistics` module.
- Presents statistics in a user-friendly format.
- Includes unit tests for core functionalities.

## Unit Tests:

The script includes unit tests implemented in test_math_skills.py. You can run the tests using:
```bash
    python3 test_math_skills.py
```
## Usage:
```bash
    python3 math_skills.py <filename.txt>
```
Replace `<filename.txt>` with the actual path to your text file containing population data.
Each line in the file should contain a valid integer or floating-point number representing a population value.

#### Example:
```bash
    python3 math_skills.py data.txt
```
#### Output:
```bash
  Average: 16
  Median: 18
  Variance: 23
  Standard Deviation: 5
```
## Installation:

Make sure you have `Python 3.x` installed on your system. You can check by running `python3 --version` in your terminal.
Download the folder containing the program.
```bash
    git clone https://github.com/stkisengese/stat-population
```
## Dependencies:

The script requires the `statistics module`, which is part of the `Python standard library` (available in `Python 3.4` and later).

## Contributing:

Contributions are welcomed to improve this script. Feel free to fork the repository and submit pull requests with enhancements or bug fixes.

## License:
MIT
(see LICENSE file for details).`

## Author(s):
[stkisengese](https://github.com/stkisengese)
