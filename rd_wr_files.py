#write in a file
def w_write():
    outfile = open("student.txt", "w")
    outfile.write("Sam Liu\n")
    outfile.write("John Doe\n")
    outfile.write("Brian Chesky\n")

    outfile.close()

#w_write()

#read from a file   
def r_read():
    with open("student.txt", "r") as fd:
        print(fd.read())
        fd.close()

r_read()