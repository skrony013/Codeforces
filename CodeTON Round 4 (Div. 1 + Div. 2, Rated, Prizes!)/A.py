# Python3 implementation
# To store all increasing subsequence of the given list
st = []


# Method to find increasing subsequence
def find(inp, out):
    if len(inp) == 0:
        if len(out) != 0:
            # storing result
            st.append(out)
        return

    # excluding 1st element
    find(inp[1:], out[:])

    # including first element
    # checking the condition
    # for increasing subsequence
    if len(out) == 0:
        find(inp[1:], inp[:1])
    elif inp[0] > out[-1]:
        out.append(inp[0])
        find(inp[1:], out[:])


# The input list
ls1 = [1, 3, 2]
ls2 = []

# Calling the function
find(ls1, ls2)

# Printing the lists
for i in st:
    print(*i)
