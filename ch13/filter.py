#this is a file filter to extract code excluding comment
# comment
# comment

def filter(src_file, outfile):
    input_file = open(src_file, "r")
    out_file = open(outfile, "w")

    while True:
        text = input_file.readline()
        if not len(text):
            break
        if text[0] == "#":
            continue

        out_file.write(text)

    input_file.close()
    out_file.close()


filter("input.py","output.py")
