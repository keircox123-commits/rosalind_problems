def main():
    

    def firstLaw(k,m,n):
        pop = float(k+m+n)
        return 1 - ( m*n + .25*m*(m-1) + n*(n-1) ) / ( pop*(pop-1) )
    
    print(firstLaw(2,2,2))


if __name__ == '__main__':
    main()