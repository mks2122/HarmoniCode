import sys
from harmoni_parser import parse
from runtime import execute

def main():
    if len(sys.argv) != 2:
        print("Usage: HarmoniCode <program_name>.hc")
        sys.exit(1)

    filename = sys.argv[1]
    
    if not filename.endswith('.hc'):
        print("Error: File must have a .hc extension")
        sys.exit(1)

    try:
        with open(filename, 'r') as file:
            code = file.read()
        
        ast = parse(code)
        execute(ast)
    
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        sys.exit(1)
    
    except Exception as e:
        print(f"Error 1121: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
