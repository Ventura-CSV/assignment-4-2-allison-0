def main():
    result = []
    a1 = int(input('Enter your first number: '))
    a2 = int(input('Enter your second number: '))
    N = int(input('Enter the number of sequences: '))
    if N >= 2:
        result.append(a1)
        result.append(a2)
        for i in range(N-2):
            num = result[-2] + result [-1]
            result.append(num)
        else:
            print(result)
    else:
        print("Please input more than two sequences")    
        

    ########################################
    # Do not delete the return statement
    ########################################
    return result



if __name__ == '__main__':
    main()
