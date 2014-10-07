
def filter(src_file, outfile):
    input_file = (src_file, "r")
    out_file = (outfile, "w")

    while True:
        text = input_file.readline()
        if not len(text):
            breakl
        if text[0] == "#":
            continue

        out_file.write(text)

    input_file.close()
    out_file.close()


filter("input.py","output.py")
