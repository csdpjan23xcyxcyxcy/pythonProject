import hashlib, time, itertools


# record the start time
start_time = time.time()

# on screen message
a = """ ================================================
                    Main menu
================================================
1. Crack using a specified word file
2. Crack using dictionary brute force attack
================================================
Enter your option 1 or 2: 

"""

# on screen message
b = """
Please enter the path and filename for the:
- i hashfile, 
- w word file, 
- o output file 

"""

# on screen message
c = """
This will perform brute force cracking.
All possible combinations of alphanumeric 
characters (5 char len) will be match against
the hash file.
Please enter the path and filename for the:
- i hashfile, 
- o output file 

"""


# function for opening a file in read only mode, and return each line
def read_file(filename):
    with open(filename, "r") as f:
        return f.readlines()


# function for hashing whatever string that was passed through the argument text1
def hash_text(text1):
    md5 = hashlib.md5(str(text1).encode()).hexdigest()
    return md5


# make a comparison of the specified hash file against a specified word list (that is in plain text), saving the
# result to a text file with filename of user's choice
def compare_hash(plain_text_file1, hash_file1, output_filename):
    with open(output_filename, "x") as file:
        for text in hash_file1:
            for text2 in plain_text_file1:
                hashed = hash_text(text2.strip())
                # print("text: ", text, "hashed: ", hashed)
                # print(text + " and " + text2)
                if hashed == text.strip():
                    # Use the print function and redirect its output to the file
                    print(text, " = ", text2, file=file)
            """else:
                 """
    return ()


# make a comparison of the specified hash file against a combination list
# the dictionary list will be hashed and matched to the hash file
def compare_hash2(hash_file2, output_filename2):
    with open(output_filename2, "x") as file:
        for text in hash_file2:
            for text2 in combinations:
                hashed = hash_text(text2.strip())
                # print("text: ", text, "hashed: ", hashed)
                # print(text + " and " + text2)
                if hashed == text.strip():
                    # Use the print function and redirect its output to the file
                    print(text, " = ", text2, file=file)
    return ()


# creating the combination list that has 5 characters of alphanumeric lowercase
alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
combination_length = 5
combinations = [''.join(i) for i in itertools.product(alphanumeric, repeat=combination_length)]


sel_opt1 = input(a)

if sel_opt1 == "1":
    input1, input2, input3 = input(b).split()
    plain_text_file = read_file(input2)
    hash_file = read_file(input1)
    compare_hash(plain_text_file, hash_file, input3)
    print("Time elapsed: {:.2f} seconds".format(time.time() - start_time))
elif sel_opt1 == "2":
    op2_input1, op2_input3 = input(c).split()
    hash_file = read_file(op2_input1)
    compare_hash2(hash_file, op2_input3)
    print("Time elapsed: {:.2f} seconds".format(time.time() - start_time))