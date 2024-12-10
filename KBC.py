# KBC QUIZ GAME


print(""" Namaskar Deviyo aur Sajjano, 

ma Amitabh Bachhan
swagat krta hu apka 
iss Kaun Banega Crorepati ke khel me\n""")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

nam=input("# To kya naam ha apka: ")
place=input("# To kahan se ha aap: ")
age=input("# kya umr ha aapki: ")

res=input("""to kaisa lg rha ha apko aaj 
iss hotseat pr baith ke: """)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

cv2=input("ENTER YOUR FAVOURITE NUMBER FROM 1 AND 2")

print("""Toh khel suru hone se pehle, 
main aapko is khel ke niyamon ke baare mein bata du. 

1. Har sawaal ke liye aapke pas char vikalp honge.
   Aur apko utar 30 second me dena hoga 

2. Aapke pas teen lifeline hain jo aap 
   kisi bhi samay istemal kar sakte hain lekin sirf ek baar

3. ek 50-50 jisme do vikalp kam ho jayenge (type 50 50)
   skip jisme us prshn ki jagah koi aur prashn aa jayega (type skip)
   skip sirf starter round ke liye hi ha
   Ask the expert aap kisise call lgake pooch skte ha

4. khel me 9 sawaal pooche jayenge. Har ek sawal ke baad ka inaam
      Q1 - 5   Q2 - 10   Q3 - 15   Q4 - 20   Q5 - 30  Q6 - 40   (30 sec)  starter  
      Q7 - 50   Q8 - 75  Q9 - 100   (1 min )  mega
      
6. sahi utr dene pr aap age badh jayenge
   aur ek galat utr apka safar khatm kar dega 
      
7. starter round me bahar hone se apko jitne paise jeete ha utne mil jayenge
   lekin mega round me kisi bhi prashn pr out hone se apko sirf 40 rupee hi milenge 

8. aap apna utar A,B,C,D likh kr de skte ha
   
   to Chaliye, shuru karte hain! Best of Luck!
   Press enter""")
cv=input() #to show after a click

#list of questions
l=["""Q1 Who was the first Vice President of India?

A) Zakir Husain
B) Dr. Rajendra Prasad
C) Dr. A P J Abdul Kalam
D) Dr. Sarvepalli Radhakrishnan""","""What is the chemical formula for water?

A) H2O
B) CO2
C) O2
D) NaCl""","""Q3 In which of the following two states were elections recently conducted in India?

A) Punjab and Rajasthan
B) Haryana and Jharkhand
C) Jammu Kashmir and Haryana
D) Jharkhand and Maharashtra""","""Q4 Which is the oldest political party from the following in India?

A) Bharatiya Janata Party (BJP)
B) Indian National Congress (INC)
C) Communist Party of India (CPI)
D) All India Trinamool Congress (AITC)""","""Q5 Who is regarded as "Sadi ka Mahanayak" in ibdian film industry?
  
  A) Rajesh Khanna
  B) Dharmender
  C) Amitabh Bachchan
  D) Shah Rukh Khan""","""Q6 What is the full form of RAM?

A) Read Access Memory
B) Random Access Memory
C) Rapid Access Memory
D) Real Access Memory""","""Q7 What is the scientific name of humans?

A) Homo erectus
B) Homo habilis
C) Homo sapiens
D) Homo neanderthalensis ""","""Q8 What is the capital of New Zealand?

A) Wellington
B) Auckland
C) Christchurch
D) Dunedin""","""Q9 Who has scored most ODI hundreads in cricket?
  
  A) Virat Kohli
  B) Sachin Tendulkar
  C) Don Bradman
  D) Ricky Ponting"""]
#list of answers option
ans=["D","A","C","B","C","B","C","A","A"]
#list of answer
answer=["Correct answer: D) Dr. Sarvepalli Radhakrishnan"
        ,"Correct answer: A) H2O"
        ,"Correct answer: C) Jammu Kashmir and Haryana"
        ,"Correct answer: B) Indian National Congress (INC)"
        ,"Correct answer: C) Amitabh Bachchan"
        ,"Correct answer: B) Random Access Memory"
        ,"Correct answer: C) Homo sapiens"
        ,"Correct answer: A) Wellington"
        ,"Correct answer: A) Virat Kohli"]
#list of 50 50 question
l50=["""Q1 Who was the first Vice President of India?

A) 
B) Dr. Rajendra Prasad
C) 
D) Dr. Sarvepalli Radhakrishnan""","""What is the chemical formula for water?

A) H2O
B) 
C) O2
D) ""","""Q3 In which of the following two states were elections recently conducted in India?

A) 
B) Haryana and Jharkhand
C) Jammu Kashmir and Haryana
D) ""","""Q4 Which is the oldest political party from the following in India?

A) Bharatiya Janata Party (BJP)
B) Indian National Congress (INC)
C) 
D) ""","""Q5 Who is regarded as "Sadi ka Mahanayak" in ibdian film industry?
  
  A) 
  B) 
  C) Amitabh Bachchan
  D) Shah Rukh Khan""","""Q6 What is the full form of RAM?

A) Read Access Memory
B) Random Access Memory
C) 
D) ""","""Q7 What is the scientific name of humans?

A) 
B) Homo habilis
C) Homo sapiens
D)  ""","""Q8 What is the capital of New Zealand?

A) Wellington
B) Auckland
C) 
D) ""","""Q9 Who has scored most ODI hundreads in cricket?
  
  A) Virat Kohli
  B) Sachin Tendulkar
  C) 
  D) """]

#another set 
l1=["""1. Which is the largest planet in our solar system?
A) Mars
B) Earth
C) Jupiter
D) Venus""","""2. Who is known as the "Father of the Nation" in India?
A) Jawaharlal Nehru
B) Subhas Chandra Bose
C) Mahatma Gandhi
D) Bhagat Singh""","""3. Which animal is known as the "Ship of the Desert"?
A) Elephant
B) Horse
C) Camel
D) Lion""","""4. In which direction does the sun rise?
A) North
B) East
C) West
D) South""","""5. Which is the longest river in the world?
A) Amazon
B) Ganga
C) Nile
D) Yamuna""","""6. Who was the first woman Prime Minister of India?
A) Indira Gandhi
B) Pratibha Patil
C) Sushma Swaraj
D) Sonia Gandhi""","""7. Which festival is known as the "Festival of Lights"?
A) Diwali
B) Holi
C) Eid
D) Christmas""","""8. Which sport is often referred to as "The Gentleman's Game"?
A) Football
B) Tennis
C) Cricket
D) Golf""","""9. Who invented the telephone?
A) Alexander Graham Bell
B) Thomas Edison
C) Nikola Tesla
D) Albert Einstein""",
]

ans1=["C","C","C","B","C","A","A","C","A"]

answer1=["C) Jupiter",
    "C) Mahatma Gandhi",
    "C) Camel",
    "B) East",
    "C) Nile",
    "A) Indira Gandhi",
    "A) Diwali",
    "C) Cricket",
    "A) Alexander Graham Bell"]

l501=["""Which is the largest planet in our solar system?
A) Earth
B)
C) Jupiter
D)""","""Who is known as the "Father of the Nation" in India?
A)
B) Subhas Chandra Bose
C) Mahatma Gandhi
D)""","""Which animal is known as the "Ship of the Desert"?
A) Elephant
B)
C) Camel
D)""","""In which direction does the sun rise?
A)
B) East
C) West
D)""","""Which is the longest river in the world?
A) Amazon
B)
C) Nile
D)""","""Who was the first woman Prime Minister of India?
A) Indira Gandhi
B) Pratibha Patil
C)
D)""","""Which festival is known as the "Festival of Lights"?
A) Diwali
B) Holi
C)
D)""","""
Which sport is often referred to as "The Gentleman's Game"?
A)
B)
C) Cricket
D) Golf""","""
Who invented the telephone?
A) Alexander Graham Bell
B) Thomas Edison
C)
D)"""
]


#prize money
prize=[5,10,15,20,30,40,50,75,100]

#for first set
if (cv2 == 1):
   for i in l:
     print(i)
     a1=str(input("ENTER :"))
     print(a1)
     z=list(a1)
     # if 50 50 lifeline is used
     if(a1=="50 50"and "50 50" not in z ):
         print("Apne 50 50 life line ka istemal kiya ha")
         hj=input()
         print(l50[l.index(i)])
         a1=str(input("ENTER :"))
         print(a1)
         if (a1==str(ans[l.index(i)])):
             if(i==l[8]):
                 print("""100 rupees! 100 rupees!
                    Apne jeet liye ha , Apne kar dikaya ha
                    lehro se darkar nauka paar nahi hoti,
                    koshish karne walo ki kabhi haar nahi hoti""")
                 print("Bilkul sahi jawab!\n",answer[l.index(i)])
                 print("Mubarak ho!",nam,"ji Aapne jeet liya hai",prize[l.index(i)],"rupees")
                 break
             else:   
                 print("Bilkul sahi jawab!\n",answer[l.index(i)])
                 print("Mubarak ho!",nam,"ji Aapne jeet liya hai",prize[l.index(i)],"rupees")
                 print("Aur isi ke sath aap agle padaav mein pravesh kar gaye hain.")
                 Jd=input()
         else:
             print("Afsos, yeh galat jawab hai.")
             print("sahi jawab ha",answer[l.index(i)])
             if (l.index(i)==0):
                print("afsos aapko bina kuch jeete hi ghr lautna padega")
             else:
                if l.index(i)<=5 :
                  print("congratulations,",nam,"ji aap jeete ha",prize[l.index(i)-1],"rupees")
                  print("Aapne koshish ki, aur har koshish mein seekhne ko milta hai")
                else:
                    print("congratulation,",nam,"ji aap jeete ha 40 rupees")
                    print("Aapne koshish ki, aur har koshish mein seekhne ko milta hai")           
             break   
     
     # if skip lifeline is used
     elif(a1=="SKIP" and "SKIP" not in z):
         print("apne skip life line ka istemal kiya ha")
         hjk=input()
         print("""Q Who is the current chief minister of Delhi?
A) Arvind Kejriwal
B) Shiela Dixit
C) Atishi Marlena
D) Manish Sisodia""")
         a1=str(input("ENTER :"))
         print(a1)
         if (a1==str(ans[l.index(i)])):
             if(i==l[8]):
                 print("""100 rupees! 100 rupees!
                    Apne jeet liye ha , Apne kar dikaya ha
                    lehro se darkar nauka paar nahi hoti,
                    koshish karne walo ki kabhi haar nahi hoti""")
                 print("Bilkul sahi jawab!\n",answer[l.index(i)])
                 print("Mubarak ho!",nam,"ji Aapne jeet liya hai",prize[l.index(i)],"rupees")
                 break
             else:   
                 print("Bilkul sahi jawab!\n",answer[l.index(i)])
                 print("Mubarak ho!",nam,"ji Aapne jeet liya hai",prize[l.index(i)],"rupees")
                 print("Aur isi ke sath aap agle padaav mein pravesh kar gaye hain.")
                 Jd=input()
         else:
             print("Afsos, yeh galat jawab hai.")
             print("sahi jawab ha",answer[l.index(i)])
             if (l.index(i)==0):
                print("afsos aapko bina kuch jeete hi ghr lautna padega")
             else:
                if l.index(i)<=5 :
                  print("congratulations,",nam,"ji aap jeete ha",prize[l.index(i)-1],"rupees")
                  print("Aapne koshish ki, aur har koshish mein seekhne ko milta hai")
                else:
                    print("congratulation,",nam,"ji aap jeete ha 40 rupees")
                    print("Aapne koshish ki, aur har koshish mein seekhne ko milta hai")           
             break   
     
     # for normal go
     else:
         # for right way
         if (a1==str(ans[l.index(i)])):
             
             # if he wins last question
             if(i==l[8]):
                 print("""100 rupees! 100 rupees!
                    Apne jeet liye ha , Apne kar dikaya ha
                    lehro se darkar nauka paar nahi hoti,
                    koshish karne walo ki kabhi haar nahi hoti""")
                 print("Bilkul sahi jawab!\n",answer[l.index(i)])
                 print("Mubarak ho!",nam,"ji Aapne jeet liya hai",prize[l.index(i)],"rupees")
                 break
             # for moving to next question after right answer
             else:   
                 print("Bilkul sahi jawab!\n",answer[l.index(i)])
                 print("Mubarak ho!",nam,"ji Aapne jeet liya hai",prize[l.index(i)],"rupees")
                 print("Aur isi ke sath aap agle padaav mein pravesh kar gaye hain.")
                 Jd=input()
         # if you answer wrong
         else:
             print("Afsos, yeh galat jawab hai.")
             print("sahi jawab ha",answer[l.index(i)])
             # eliminating at first
             if (l.index(i)==0):
                print("afsos aapko bina kuch jeete hi ghr lautna padega")
             # eliminating at some other question
             else:
                if l.index(i)<=5 :
                  print("congratulations,",nam,"ji aap jeete ha",prize[l.index(i)-1],"rupees")
                  print("Aapne koshish ki, aur har koshish mein seekhne ko milta hai")
                else:
                    print("congratulation,",nam,"ji aap jeete ha 40 rupees")
                    print("Aapne koshish ki, aur har koshish mein seekhne ko milta hai")           
             break   

#for second set
else:
   for i in l1:
     print(i)
     a1=str(input("ENTER :"))
     print(a1)
     z=list(a1)
     if(a1=="50 50"and "50 50" not in z ):
         print("Apne 50 50 life line ka istemal kiya ha")
         hj=input()
         print(l501[l1.index(i)])
         a1=str(input("ENTER :"))
         print(a1)
         if (a1==str(ans1[l1.index(i)])):
             if(i==l1[8]):
                 print("""100 rupees! 100 rupees!
                    Apne jeet liye ha , Apne kar dikaya ha
                    lehro se darkar nauka paar nahi hoti,
                    koshish karne walo ki kabhi haar nahi hoti""")
                 print("Bilkul sahi jawab!\n",answer1[l1.index(i)])
                 print("Mubarak ho!",nam,"ji Aapne jeet liya hai",prize[l1.index(i)],"rupees")
                 break
             else:   
                 print("Bilkul sahi jawab!\n",answer1[l1.index(i)])
                 print("Mubarak ho!",nam,"ji Aapne jeet liya hai",prize[l1.index(i)],"rupees")
                 print("Aur isi ke sath aap agle padaav mein pravesh kar gaye hain.")
                 Jd=input()
         else:
             print("Afsos, yeh galat jawab hai.")
             print("sahi jawab ha",answer[l1.index(i)])
             if (l1.index(i)==0):
                print("afsos aapko bina kuch jeete hi ghr lautna padega")
             else:
                if l1.index(i)<=5 :
                  print("congratulations,",nam,"ji aap jeete ha",prize[l1.index(i)-1],"rupees")
                  print("Aapne koshish ki, aur har koshish mein seekhne ko milta hai")
                else:
                    print("congratulation,",nam,"ji aap jeete ha 40 rupees")
                    print("Aapne koshish ki, aur har koshish mein seekhne ko milta hai")           
             break   
     elif(a1=="SKIP" and "SKIP" not in z):
         print("apne skip life line ka istemal kiya ha")
         hjk=input()
         print("""Q Who is the current chief minister of Delhi?
A) Arvind Kejriwal
B) Shiela Dixit
C) Atishi Marlena
D) Manish Sisodia""")
         a1=str(input("ENTER :"))
         print(a1)
         if (a1==str(ans1[l1.index(i)])):
             if(i==l1[8]):
                 print("""100 rupees! 100 rupees!
                    Apne jeet liye ha , Apne kar dikaya ha
                    lehro se darkar nauka paar nahi hoti,
                    koshish karne walo ki kabhi haar nahi hoti""")
                 print("Bilkul sahi jawab!\n",answer1[l1.index(i)])
                 print("Mubarak ho!",nam,"ji Aapne jeet liya hai",prize[l1.index(i)],"rupees")
                 break
             else:   
                 print("Bilkul sahi jawab!\n",answer1[l1.index(i)])
                 print("Mubarak ho!",nam,"ji Aapne jeet liya hai",prize[l1.index(i)],"rupees")
                 print("Aur isi ke sath aap agle padaav mein pravesh kar gaye hain.")
                 Jd=input()
         else:
             print("Afsos, yeh galat jawab hai.")
             print("sahi jawab ha",answer1[l1.index(i)])
             if (l1.index(i)==0):
                print("afsos aapko bina kuch jeete hi ghr lautna padega")
             else:
                if l1.index(i)<=5 :
                  print("congratulations,",nam,"ji aap jeete ha",prize[l1.index(i)-1],"rupees")
                  print("Aapne koshish ki, aur har koshish mein seekhne ko milta hai")
                else:
                    print("congratulation,",nam,"ji aap jeete ha 40 rupees")
                    print("Aapne koshish ki, aur har koshish mein seekhne ko milta hai")           
             break   
     else:
         if (a1==str(ans1[l1.index(i)])):
             if(i==l1[8]):
                 print("""100 rupees! 100 rupees!
                    Apne jeet liye ha , Apne kar dikaya ha
                    lehro se darkar nauka paar nahi hoti,
                    koshish karne walo ki kabhi haar nahi hoti""")
                 print("Bilkul sahi jawab!\n",answer1[l1.index(i)])
                 print("Mubarak ho!",nam,"ji Aapne jeet liya hai",prize[l1.index(i)],"rupees")
                 break
             else:   
                 print("Bilkul sahi jawab!\n",answer1[l1.index(i)])
                 print("Mubarak ho!",nam,"ji Aapne jeet liya hai",prize[l1.index(i)],"rupees")
                 print("Aur isi ke sath aap agle padaav mein pravesh kar gaye hain.")
                 Jd=input()
         else:
             print("Afsos, yeh galat jawab hai.")
             print("sahi jawab ha",answer1[l1.index(i)])
             if (l1.index(i)==0):
                print("afsos aapko bina kuch jeete hi ghr lautna padega")
             else:
                if l1.index(i)<=5 :
                  print("congratulations,",nam,"ji aap jeete ha",prize[l1.index(i)-1],"rupees")
                  print("Aapne koshish ki, aur har koshish mein seekhne ko milta hai")
                else:
                    print("congratulation,",nam,"ji aap jeete ha 40 rupees")
                    print("Aapne koshish ki, aur har koshish mein seekhne ko milta hai")           
             break   

# termination of game
CV3=input()
print("_______~~~~~~~_______~~~~~~~_______~~~~~~~_______~~~~~~~_______")
print("Iss khel ko khelene ke liye",nam,"ji aapka shukriya")
print("Programmed and coded by knight")

        
      







