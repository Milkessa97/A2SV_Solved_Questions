def split_and_join(line):
    # write your code here
    my_words = line.split(" ")
    return "-".join(my_words)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
