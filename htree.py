import stddraw,sys # import

#-----------------------
# H tree.py
#-----------------------

def Htree(n,l,x,y):   # n is int
    if n==0:
        return
    x0=x-(l/2)
    x1=x+(l/2)
    y0=y-(l/2)
    y1=y+(l/2)

    stddraw.line(x0,y0,x0,y1)
    stddraw.line(x1,y0,x1,y1)
    stddraw.line(x0,y,x1,y)

    Htree(n-1 ,l/2,x0,y0)
    Htree(n-1,l/2,x0,y1)
    Htree(n-1,l/2,x1,y0)
    Htree(n-1,l/2,x1,y1)

def main():
    stddraw.setPenRadius(0.0)
    n=int(sys.argv[1])
    Htree(n,0.5,0.5,0.5)
    stddraw.show()

if __name__ == '__main__':
    main()

