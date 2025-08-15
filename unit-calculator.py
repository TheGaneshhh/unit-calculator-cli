def temp(cel) :
        f = (cel * 1.8) + 32
        print("{} celsius to Fahrenheit is {}".format(cel,f))   
    



def kilom(kml):
        miles = kml*0.621371
        print("{} KM in miles is : {}".format(kml,miles))
        
        




def weig(kg):
        lbs = kg * 2.20462
        print("{} KG in LBS : {}".format(kg,lbs))
        
        



 
while True :
        print("------ Unit Converter------")
        print("1. Temprature")
        print("2. Distance")
        print("3. Weight")
        print("q. Quite")
        
        opt = input("Choose an option : ")
        if opt == "1" :
                temp(float(input("Enter the Temprature in Celsius : ")))
        elif opt == "2" :
                kilom(float(input("Enter the KM : ")))
        elif opt == "3" :
                weig(float(input("Enter the weight in KG : ")))
        elif opt.lower() == "q" :
                break 
        else :
                print("Invalid input!!")
                
                
                