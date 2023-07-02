ones=['','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN']
tens=['','','TWENTY','THIRTY','FORTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINTY']
hundereds=['','ONE HUNDERED','TWO HUNDERED','THREE HUNDERED','FOUR HUNDERED','FIVE HUNDERED','SIX HUNDERED','SEVEN HUNDERED','EIGHT HUNDERED','NINE HUNDERED']

#number=eval(input('Enter a number between 0 to 99 :'))
for number in range(0,999):
    if number==0:
            print(ones[0])
    elif number<=19:
          print(str(number)+' :: '+ones[number])
    elif number <=999:
        #print(tens[number//10]+' '+ones[number%10])
        hundered=number//100
        ten=(number%100)//10
        one=((number%100)//10)%10
        print(str(number)+' :: '+hundereds[hundered]+' AND '+tens[ten]+' '+ones[one])
        
    else:
      print('Enter the number between 1 to 99 only')