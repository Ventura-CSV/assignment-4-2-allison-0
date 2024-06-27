def main():
    result = []
    a1 = int(input('Enter your first number: '))
    a2 = int(input('Enter your second number: '))
    N = int(input('Enter the number of sequences: '))
    result.append(a1)
    result.append(a2)
    num = result[0] + result[-1]
    for i in range(N):
        num = result[-2] + result [-1]
        result.append(num)
        print(num)
    """
    ########################################
    Code Your Program here
    ########################################
    """

    ########################################
    # Do not delete the return statement
    ########################################
    return result



if __name__ == '__main__':
    main()
