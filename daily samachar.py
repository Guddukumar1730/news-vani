import requests
def top_headlines():
   main_url="https://newsapi.org/v2/top-headlines?country=in&apiKey=3553f8760e674035b4742b80e15f20bd"
   req=requests.get(main_url)
   headlines=req.json()

   article=headlines["articles"]
   result=[]

   for ar in article:
      result.append(ar["title"])
   for i in range(len(result)):
      print(i + 1 ,result[i])

   from win32com.client import Dispatch
   speak=Dispatch("SAPI.Spvoice")
   speak.Speak(result)


def business():
   main_url="https://newsapi.org/v2/top-headlines?category=business&apiKey=3553f8760e674035b4742b80e15f20bd"
   req=requests.get(main_url)
   b=req.json()

   article=b["articles"]
   result=[]

   for ar in article:
      result.append(ar["title"])
   for i in range(len(result)):
      print(i + 1 ,result[i])

   from win32com.client import Dispatch
   speak=Dispatch("SAPI.Spvoice")
   speak.Speak(result)

def technology():
   main_url="https://newsapi.org/v2/top-headlines?category=technology&apiKey=3553f8760e674035b4742b80e15f20bd"
   req=requests.get(main_url)
   tech=req.json()

   artile=tech["articles"]
   result=[]

   for ar in artile:
      result.append(ar["title"])
   for i in range(len(result)):
      print(i + 1 ,result[i])

   from win32com.client import Dispatch
   speak=Dispatch("SAPI.Spvoice")
   speak.Speak(result)

def entertainment():
   main_url="https://newsapi.org/v2/top-headlines?categorgy=entertainment&apiKey=3553f8760e674035b4742b80e15f20bd"
   req=requests.get(main_url)
   entertain=req.json()

   artile=entertain["articles"]
   result=[]

   for ar in artile:
      result.append(ar["title"])
   for i in range(len(result)):
      print(i + 1 ,result[i])

   from win32com.client import Dispatch
   speak=Dispatch("SAPI.Spvoice")
   speak.Speak(result)

def sports():
   main_url="https://newsapi.org/v2/top-headlines?categorgy=sports&apiKey=3553f8760e674035b4742b80e15f20bd"
   req=requests.get(main_url)
   khel=req.json()

   artile=khel["articles"]
   result=[]

   for ar in artile:
      result.append(ar["title"])
   for i in range(len(result)):
      print(i + 1 ,result[i])

   from win32com.client import Dispatch
   speak=Dispatch("SAPI.Spvoice")
   speak.Speak(result)

def health():
   main_url="https://newsapi.org/v2/top-headlines?category=health&apiKey=3553f8760e674035b4742b80e15f20bd"
   req=requests.get(main_url)
   fit=req.json()

   artile=fit["articles"]
   result=[]

   for ar in artile:
      result.append(ar["title"])
   for i in range(len(result)):
      print(i + 1 ,result[i])

   from win32com.client import Dispatch
   speak=Dispatch("SAPI.Spvoice")
   speak.Speak(result)

def science():
   main_url="https://newsapi.org/v2/top-headlines?category=scienceapiKey=3553f8760e674035b4742b80e15f20bd"
   req=requests.get(main_url)
   sci_fi=req.json()

   artile=sci_fi["articles"]
   result=[]

   for ar in artile:
      result.append(ar["title"])
   for i in range(len(result)):
      print(i + 1 ,result[i])

   from win32com.client import Dispatch
   speak=Dispatch("SAPI.Spvoice")
   speak.Speak(result)
   return science()




if __name__ == '__main__':

   print("Enter your choice")
   print('1-India')
   print('2-Business')
   print('3-Technology')
   print('4-Entertainment')
   print('5-Sports')
   print('6-Health')
   print('7-Science')
   print(input("ENTER HERE:"))
   user_choice=input(" ")
   if user_choice=="1":
      print(top_headlines)
   elif user_choice=="2":
      print(business)
   elif user_choice=="3":
      print(technology)
   elif user_choice=="4":
      print(entertainment)
   elif user_choice=="5":
      print(sports)
   elif user_choice=="6":
      print(health)
   elif user_choice=="7":
      print(science)








