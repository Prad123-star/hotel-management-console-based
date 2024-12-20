#hotel management system
db={1:"trollybag",2:"biscuits",3:"choclates",4:"wheat",5:"rise",6:"waterbottle"}
price={1:100,2:20,3:40,4:70,5:90,6:50}
items=[]
qu=[]
print("-"*100)
 
print(f"{''*60} hotel godavari")
print("-"*100)
while True:
     print("""  
              1.trollybag       4.wheat  
               2.biscuits       5.rise
               3.choclates      6.waterbottle""")
     i=int(input("enter your choice:"))
     q=int(input("enter your quantity:"))
     items.append(i)
     qu.append(q)
     sum=0
     c=input("do you want to continue(yes/no):")
     if c=="no":
       print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("sr.no","items", "quantity","price","amount"))
       print("-"*100)   
       for i in range(len(items)):
          print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i+1,db[items[i]],qu[i],
             price[items[i]],price[items[i]]*qu[i]))
          sum=sum+price[items[i]]*qu[i]
          print(f"you total amount is{sum}")
          print("f thank you visit again ")
          break
                                           



