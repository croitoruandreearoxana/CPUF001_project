from process import read_input, write_output
from calc_sum import calculate_sum
from calc_min_max import calculate_min_max
from calc_mean import calculate_mean
from calc_median import calculate_median
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "output.txt"

    # Read data
    data = read_input(input_file)
    
    # Perform calculations
    result = {}
    result["Sum"] = calculate_sum(data)
    result["Min"], result["Max"] = calculate_min_max(data)
    result["Mean"] = calculate_mean(data)
    result["Median"] = calculate_median(data)

    # Write output
    write_output(output_file, result)
    print(f"Output stored in {output_file}")

if __name__ == "__main__":
    main()
