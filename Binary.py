def encode(text,dictionary):
   ranges=[0]   
   for i in dictionary:
      ranges.append(float(ranges[len(ranges)-1])+dictionary[i])
   i=1
   smallest=1
   while i<len(ranges):
      if smallest>ranges[i]-ranges[i-1]:
         smallest=ranges[i]-ranges[i-1]
      i=i+1
   k=0
   while(float(1/2**k)>smallest):
      k=k+1
   dic={}
   dicc={}
   index=0
   for i in dictionary:
      dic[i]=[ranges[index],ranges[index+1]]
      dicc[i]=[dictionary[i],ranges[index],ranges[index+1]]
      index=index+1
   string=""
   lower=0
   upper=1
   for i in range (0,len(text)):
      lower=dicc[text[i]][1]
      upper=dicc[text[i]][2] 
      while (not((lower<0.5 and upper>0.5))):
         if (lower<0.5 and upper<0.5):
            string=string+'0'
            lower=lower*2
            upper=upper*2
         elif(lower>0.5 and upper>0.5):
            string=string+'1'
            lower=(lower-0.5)*2
            upper=(upper-0.5)*2
      for j in dic:
         dicc[j][1]=float(lower+ (upper-lower) * dic[j][0])
         dicc[j][2]=float(lower+ (upper-lower) * dic[j][1])
   x=decToBinConversion(0.5,k)
   string=string+x[1:]
   return string

def decode (text,dictionary,n):
   ranges=[0]   
   for i in dictionary:
      ranges.append(float(ranges[len(ranges)-1])+dictionary[i])
   i=1
   smallest=1
   while i<len(ranges):
      if smallest>ranges[i]-ranges[i-1]:
         smallest=ranges[i]-ranges[i-1]
      i=i+1
   k=0
   while(float(1/2**k)>smallest):
      k=k+1
   dic={}
   dicc={}
   index=0
   final=""
   for i in dictionary:
      dic[i]=[ranges[index],ranges[index+1]]
      dicc[i]=[dictionary[i],ranges[index],ranges[index+1]]
      index=index+1
   index=0
   count=0
   upper=1
   lower=0
   while count<n:
      string=text[index:index+k]
      sum=0
      for i in range (0,len(string)):
         sum=float(sum+int(string[i])*2**(len(string)-i-1))
      sum=float(sum/2**k)
      code=float((sum-lower)/(upper-lower))
      for i in dicc:
         if code>dic[i][0] and code<dic[i][1]:
            final=final+i
            count=count+1
            break
      o=final[len(final)-1]
      lower=dicc[o][1]
      upper=dicc[o][2]
      
      while (not((lower<=0.5 and upper>=0.5))):
         
         if (lower<0.5 and upper<0.5):
            index=index+1
            lower=lower*2
            upper=upper*2
         elif(lower>0.5 and upper>0.5):
            index=index+1
            lower=(lower-0.5)*2
            upper=(upper-0.5)*2
      for j in dicc:
         dicc[j][1]=float(lower+ (upper-lower) * dic[j][0])
         dicc[j][2]=float(lower+ (upper-lower) * dic[j][1])
   return final

def decToBinConversion(no, precision): 
    binary = ""  
    IntegralPart = int(no)  
    fractionalPart = no- IntegralPart
    #to convert an integral part to binary equivalent
    while (IntegralPart):
        re = IntegralPart % 2 
        binary += str(re)  
        IntegralPart //= 2
    binary = binary[ : : -1]    
    binary += '.'
    #to convert an fractional part to binary equivalent
    while (precision):
        fractionalPart *= 2
        bit = int(fractionalPart)
        if (bit == 1) :   
            fractionalPart -= bit  
            binary += '1'
        else : 
            binary += '0'
        precision -= 1
    return binary  
   










      
   

   


   
   
   







dictionary={}
file= open("encode.txt", 'r')
data = file.read()
lines=data.splitlines()
stringToEncode=lines[0]
newList = lines[1].split(",")
for word in newList:
   if word == '':
      break
   newword = word.split(":")
   dictionary[newword[0]]=float(newword[1])
s=encode(stringToEncode,dictionary)
output = open("encoded.txt","w+")
output.write("".join(s))
print("Encoded file generated as encoded.txt")



dictionary={}
file= open("decode.txt", 'r')
data = file.read()
lines=data.splitlines()
stringToDecode=lines[0]
newList = lines[1].split(",")
n=int(lines[2])
for word in newList:
   if word == '':
      break
   newword = word.split(":")
   dictionary[newword[0]]=float(newword[1])
s=decode(stringToDecode,dictionary,n)
output = open("decoded.txt","w+")
output.write("".join(s))
print("Decoded file generated as decoded.txt")
