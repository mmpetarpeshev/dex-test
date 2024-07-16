import argparse

def main():
    parser = argparse.ArgumentParser(description="Print two named arguments.")
    parser.add_argument('--arg1', required=True, help='First argument')
    parser.add_argument('--arg2', required=True, help='Second argument')
    
    args = parser.parse_args()
    
    print(f"Argument 1: {args.arg1}")
    print(f"Argument 2: {args.arg2}")

if __name__ == "__main__":
    main()
