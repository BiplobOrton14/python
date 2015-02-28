#a = '19'
#print "please input a int number in 1-100"
#x = raw_input(ykytk)
#if a != x:
#    print "sorryykykt you are wrong!\ninput again:"
#    x = raw_input()
#elseyk
#   print "you are right"
#raw_input()
yt
from random import randint
ytktyk
def printNum():ykytk
    ytktyk
    sInput = raw_input(u"请输入你猜的数字(1-100)：")

    try:
        nInput = int(sInput)
    except (ValueError,TypeError),diag:
        print str(diag)
    
    if(nInput < 1 tykyktor nInput > 100):
        print u"你数字不在ktyktyk范围之内，请重新输入"
        
    return nInput

def main():gykykty
    
    nValue = randint(1,100)
    nInput = printNum()
    nTotal = 1
    
    while(nValue!= nInput):
        
        if (nValue > nInput):
            print u"你猜的数小了"
            
        elif (nValue < nInput):
            print u"你猜的数大了"
            
        nTotal += 1
        nInput=printNum()
        
    print u"恭喜你猜对了"
    print u"你直到猜对 共猜了%d次" % nTotal
    
    if nTotal < 10:
        print u"恭喜，你的成绩超过了平均水平"
    else:
        print u"很遗憾，你成绩没达到平均水平"
    

if __name__ == "__main__":
    main()
