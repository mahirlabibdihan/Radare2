import r2pipe


def analyze_binary(binary_path):
    # Open the binary in Radare2
    r2 = r2pipe.open(binary_path)
    # r2.cmd("e bin.relocs.apply=true")

    # Perform analysis
    r2.cmd("aaa")  # Analyze all (functions, data, and references)

    # Get information about the binary
    architecture = r2.cmd("e asm.arch")  # Get the architecture
    bits = r2.cmd("e asm.bits")  # Get the number of bits (e.g., 32 or 64)

    print(f"Binary information: {architecture} {bits}-bit")

    # List functions
    functions = r2.cmdj("aflj")  # Get a JSON array of functions
    print("Functions:")
    for function in functions:
        print(f"{function['offset']} {function['name']}")

    # Close the Radare2 session
    r2.quit()


if __name__ == "__main__":
    # compile a c file first
    # gcc -g -o a.out script.c
    
    binary_path = "a.out"
    analyze_binary(binary_path)
