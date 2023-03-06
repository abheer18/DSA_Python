n= 5
for i in range(0,n):
    for j in range(i,n):  #print spaces
        print(" ", end=' ')
    for j in range(i+1):   #print element
        print("*",end=' ')
    print("")

    #         *
    #       * *
    #     * * *
    #   * * * *
    # * * * * *