class SubfieldsInAI():
    def subfields():
        a=('''Sub-fields in AI are:
Machine Learning
Neural Networks
Vision
Robotics
Speech Processing
Natural Language Processing''')
        return a
    
class oddEven():
    def oddEven():
        Num=(int(input("Enter a number:")))
        if (Num%2 == 0):
            result=(str(Num)+" is Even number")
        else:
            result=(str(Num)+" is odd number")
        return result
    
class ElegiblityForMarriage():
    def Elegible():
        gen=input("Enter your Gender:")
        age=int(input("Enter your age:"))
        gen1='''Your Gender:'''+gen
        age1='''Your Gender:'''+str(age)
        if (gen=='male' and age>21):
            el='ELIGIBLE'
        elif (gen=='female' and age>18):
            el='ELIGIBLE'
        else:    
            el=' Not ELIGIBLE'
        return gen1,age1,el
    
    
class findPercent():
    def percentage():        
        s1=int(input("Enter te subject1 mark:"))
        s2=int(input("Enter te subject2 mark:"))
        s3=int(input("Enter te subject3 mark:"))
        s4=int(input("Enter te subject4 mark:"))
        s5=int(input("Enter te subject5 mark:"))
        tot=s1+s2+s3+s4+s5
        per=tot/5
        print("Total:",tot)
        print("Percentage:",per)
        
class triangle():
    def triangle():
        Height=int(input("Enter the height:"))
        Breadth=int(input("Enter the Breadth:"))
        A=(Height*Breadth)/2

        Height1=int(input("Enter the height1:"))
        Height2=int(input("Enter the height2:"))
        Breadth1=int(input("Enter the Breadth1:"))
        P= Height1+Height2+Breadth1      

        print("Height:",Height) 
        print("Breadth:",Breadth)     
        print("Area formula:(Height*Breadth)/2")
        Area=("Area of Triangle:"+str(A))
        print("Area of Triangle:",A)

        print("Height1:",Height1) 
        print("Height2:",Height2)
        print("Breadth1:",Breadth1) 
        print("perimeter formula:(Height1+Height2+Breadth)")
        Perimeter=("Perimeter of Triagnle:"+str(P))
        print("Perimeter of Triagnle:",P)

        return Area,Perimeter             
    
    
    
    
    
    