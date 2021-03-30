def split_and_join(line):
    # write your code here
    T = line.split(" ")
    print "-".join(T)

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result