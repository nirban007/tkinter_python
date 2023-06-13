import tkinter as tk
from tkinter import *
root = tk.Tk()
root.geometry("1000x800")
root.title("SSC Grade Calculator")
Label(root, text="Bangla 1st paper:",font="23").place(x=30, y="70")
Label(root, text="Bangla 2nd paper:",font="23").place(x=30, y="105")
Label(root, text="English 1st paper:",font="23").place(x=30, y="140") 
Label(root, text="English 2nd paper:",font="23").place(x=30, y="175")
Label(root, text="Physics Theory:",font="23").place(x=30, y="210")
Label(root, text="Physics practical:",font="23").place(x=30, y="245")
Label(root, text="Chemistry Theory:",font="23").place(x=30, y="280")
Label(root, text="Chemistry Practical:",font="23").place(x=30, y="315")
Label(root, text="Higher Math:",font="23").place(x=30, y="350")
Label(root, text="Higher Math Practical:",font="23").place(x=30, y="385")
Label(root, text="Biology Theory:",font="23").place(x=30, y="420")
Label(root, text="Biology practical:",font="23").place(x=30, y="455")
Label(root, text="Total Marks: ", font="impact 13 bold").place(x=30,y=490)
Label(root, text="Average Mark: ", font="impact 13 bold").place(x=30,y=525)
Label(root, text="Grade: ", font="impact 13 bold").place(x=30,y=560)

Label(root, text="Bangla 1st paper Result:",font="23").place(x=500, y="70")
Label(root, text="Bangla 2nd paper Result:",font="23").place(x=500, y="105")
Label(root, text="English 1st paper Result:",font="23").place(x=500, y="140") 
Label(root, text="English 2nd paper Result:",font="23").place(x=500, y="175")
Label(root, text="Physics Theory Result:",font="23").place(x=500, y="210")
Label(root, text="Physics practical Result:",font="23").place(x=500, y="245")
Label(root, text="Chemistry Theory Result:",font="23").place(x=500, y="280")
Label(root, text="Chemistry Practical Result:",font="23").place(x=500, y="315")
Label(root, text="Higher Math Result:",font="23").place(x=500, y="350")
Label(root, text="Higher Math Practical Result:",font="23").place(x=500, y="385")
Label(root, text="Biology Theory Result:",font="23").place(x=500, y="420")
Label(root, text="Biology practical Result:",font="23").place(x=500, y="455")

#Button_Function
def calculate():
    
    bangla_1st_paper = int(bangla_1st_paper_entry.get())

  
    bangla_2nd_paper = int(bangla_2nd_paper_entry.get())  

          
    english_1st_paper = int(english_1st_paper_entry.get())


    english_2nd_paper = int(english_2nd_paper_entry.get())


    physics_theory = int(physics_theory_entry.get())


    physics_practical = int(physics_practical_entry.get())


    chemistry_theory = int(chemistry_theory_entry.get())


    chemistry_practical = int(chemistry_practical_entry.get())


    higher_math = int(higher_math_entry.get())


    higher_math_practical = int(higher_math_practical_entry.get())


    biology_theory =  int(biology_theory_entry.get())


    biology_practical =  int(biology_practical_entry.get())

#bangla first paper
    if(bangla_1st_paper>=80):
        Label(root, text="Got A+ & Grade Point is: 5.00", font="23",border="2").place(x=700,y=70)
        # print("Got A+ in Bangla 1st paper")
        # print('Grade Point In Bangla 1st paper: 5.00')
    elif(80>bangla_1st_paper>=70):
        Label(root, text="Got A & Grade Point is: 4.00", font="23").place(x=700,y=70)

    elif(70>bangla_1st_paper>=60):
        Label(root, text="Got A- & Grade Point is: 3.50", font="23").place(x=700,y=70)
        # print("Got A- in Bangla 1st paper")
        # print('Grade Point In Bangla 1st paper: 3.50')
    elif(60>bangla_1st_paper>=50):
        Label(root, text="Got B & Grade Point is: 3.00", font="23").place(x=700,y=70)
        # print("Got B in Bangla 1st paper")
        # print('Grade Point In Bangla 1st paper: 3.00')
    elif(50>bangla_1st_paper>=40):
        Label(root, text="Got C & Grade Point is: 2.00", font="23").place(x=700,y=70)
        # print("Got C in Bangla 1st paper")
        # print('Grade Point In Bangla 1st paper: 2.00')
    elif(40>bangla_1st_paper>=33):
        Label(root, text="Got D & Grade Point is: 1.00", font="23").place(x=700,y=70)
        # print("Got D in Bangla 1st paper");
        # print('Grade Point In Bangla 1st paper: 1.00')
    else:
        Label(root, text="Opps it's fail. Better Luck Next Time", font="23").place(x=700,y=70)
        # print("Got F in Bangla 1st paper")
        # print('Grade Point In Bangla 1st paper: F \n')
   
  
#bangla 2nd paper
    if(bangla_2nd_paper>=80):
        Label(root, text="Got A+ & Grade Point is: 5.00", font="23").place(x=700,y=105)
    elif(80>bangla_2nd_paper>=70):
        Label(root, text="Got A & Grade Point is: 4.00", font="23").place(x=700,y=105)
    elif(70>bangla_2nd_paper>=60):
        Label(root, text="Got A- & Grade Point is: 3.50", font="23").place(x=700,y=105)
    elif(60>bangla_2nd_paper>=50):
        Label(root, text="Got B & Grade Point is: 3.00", font="23").place(x=700,y=105)
    elif(50>bangla_2nd_paper>=40):
        Label(root, text="Got C & Grade Point is: 2.00", font="23").place(x=700,y=105)
    elif(40>bangla_2nd_paper>=33):
        Label(root, text="Got D & Grade Point is: 1.00", font="23").place(x=700,y=105)
    else:
        Label(root, text="Opps it's fail. Better Luck Next Time", font="23").place(x=700,y=105)
#English 1st paper
    if(english_1st_paper>=80):
        Label(root, text="Got A+ & Grade Point is: 5.00", font="23").place(x=700,y=140)
    elif(80>english_1st_paper>=70):
        Label(root, text="Got A & Grade Point is: 4.00", font="23").place(x=700,y=140)
    elif(70>english_1st_paper>=60):
        Label(root, text="Got A- & Grade Point is: 3.50", font="23").place(x=700,y=140)
    elif(60>english_1st_paper>=50):
        Label(root, text="Got B & Grade Point is: 3.00", font="23").place(x=700,y=140)
        
    elif(50>english_1st_paper>=40):
        Label(root, text="Got C & Grade Point is: 2.00", font="23").place(x=700,y=140)

    elif(40>english_1st_paper>=33):
        Label(root, text="Got D & Grade Point is: 1.00", font="23").place(x=700,y=140)
    else:
        Label(root, text="Opps it's fail. Better Luck Next Time", font="23").place(x=700,y=140)
        

#English 2nd paper
    if(english_2nd_paper>=80):
        Label(root, text="Got A+ & Grade Point is: 5.00", font="23").place(x=700,y=175)
    elif(80>english_2nd_paper>=70):
        Label(root, text="Got A & Grade Point is: 4.00", font="23").place(x=700,y=175)
    elif(70>english_2nd_paper>=60):
        Label(root, text="Got A- & Grade Point is: 3.50", font="23").place(x=700,y=175)
    elif(60>english_2nd_paper>=50):
        Label(root, text="Got B & Grade Point is: 3.00", font="23").place(x=700,y=175)
    elif(50>english_2nd_paper>=40):
        Label(root, text="Got C & Grade Point is: 2.00", font="23").place(x=700,y=175)
    elif(40>english_2nd_paper>=33):
        Label(root, text="Got D & Grade Point is: 1.00", font="23").place(x=700,y=175)
    else:
        Label(root, text="Opps it's fail. Better Luck Next Time", font="23").place(x=700,y=175)
    
#Physics Theory
    if(physics_theory>=80):
        Label(root, text="Got A+ & Grade Point is: 5.00", font="23").place(x=700,y=210)
    elif(80>physics_theory>=70):
        Label(root, text="Got A & Grade Point is: 4.00", font="23").place(x=700,y=210)
    elif(70>physics_theory>=60):
        Label(root, text="Got A- & Grade Point is: 3.50", font="23").place(x=700,y=210)
    elif(60>physics_theory>=50):
        Label(root, text="Got B & Grade Point is: 3.00", font="23").place(x=700,y=210)
    elif(50>physics_theory>=40):
        Label(root, text="Got C & Grade Point is: 2.00", font="23").place(x=700,y=210)
    elif(40>english_2nd_paper>=33):
        Label(root, text="Got C & Grade Point is: 2.00", font="23").place(x=700,y=210)
    else:
        Label(root, text="Opps it's fail. Better Luck Next Time", font="23").place(x=700,y=210)
    
 #Physics practical   
    if(physics_practical>=80):
        Label(root, text="Got A+ & Grade Point is: 5.00", font="23").place(x=700,y=245)
    elif(80>physics_practical>=70):
        Label(root, text="Got A & Grade Point is: 4.00", font="23").place(x=700,y=245)
    elif(70>physics_practical>=60):
        Label(root, text="Got A- & Grade Point is: 3.50", font="23").place(x=700,y=245)
    elif(60>physics_practical>=50):
        Label(root, text="Got B & Grade Point is: 3.00", font="23").place(x=700,y=245)
    elif(50>physics_practical>=40):
        Label(root, text="Got C & Grade Point is: 2.00", font="23").place(x=700,y=245)
    elif(40>physics_practical>=33):
        Label(root, text="Got D & Grade Point is: 1.00", font="23").place(x=700,y=245)
    else:
        Label(root, text="Opps it's fail. Better Luck Next Time", font="23").place(x=700,y=245)

#Chemistry Theory  
    if(chemistry_theory>=80):
        Label(root, text="Got A+ & Grade Point is: 5.00", font="23").place(x=700,y=280)
    elif(80>chemistry_theory>=70):
        Label(root, text="Got A & Grade Point is: 4.00", font="23").place(x=700,y=280)
    elif(70>chemistry_theory>=60):
        Label(root, text="Got A- & Grade Point is: 3.50", font="23").place(x=700,y=280)
    elif(60>chemistry_theory>=50):
        Label(root, text="Got B & Grade Point is: 3.00", font="23").place(x=700,y=280)
    elif(50>chemistry_theory>=40):
        Label(root, text="Got C & Grade Point is: 2.00", font="23").place(x=700,y=280)
    elif(40>chemistry_theory>=33):
        Label(root, text="Got D & Grade Point is: 1.00", font="23").place(x=700,y=280)
    else:
        Label(root, text="Opps it's fail. Better Luck Next Time", font="23").place(x=700,y=280)

#Chemistry Practical 
    if(chemistry_practical>=80):
        Label(root, text="Got A+ & Grade Point is: 5.00", font="23").place(x=700,y=315)
    elif(80>chemistry_practical>=70):
        Label(root, text="Got A & Grade Point is: 4.00", font="23").place(x=700,y=315)
    elif(70>chemistry_practical>=60):
        Label(root, text="Got A- & Grade Point is: 3.50", font="23").place(x=700,y=315)
    elif(60>chemistry_practical>=50):
        Label(root, text="Got B & Grade Point is: 3.00", font="23").place(x=700,y=315)
    elif(50>chemistry_practical>=40):
        Label(root, text="Got C & Grade Point is: 2.00", font="23").place(x=700,y=315)
    elif(40>chemistry_practical>=33):
        Label(root, text="Got D & Grade Point is: 1.00", font="23").place(x=700,y=315)
    else:
        Label(root, text="Opps it's fail. Better Luck Next Time", font="23").place(x=700,y=315)
    
#Higher Math  
    if(higher_math >=80):
        Label(root, text="Got A+ & Grade Point is: 5.00", font="23").place(x=700,y=350)
    elif(80>higher_math >=70):
        Label(root, text="Got A & Grade Point is: 4.00", font="23").place(x=700,y=350)
    elif(70>higher_math >=60):
        Label(root, text="Got A- & Grade Point is: 3.50", font="23").place(x=700,y=350)
    elif(60>higher_math >=50):
        Label(root, text="Got B & Grade Point is: 3.00", font="23").place(x=700,y=350)
    elif(50>higher_math >=40):
        Label(root, text="Got C & Grade Point is: 2.00", font="23").place(x=700,y=350)
    elif(40>higher_math >=33):
        Label(root, text="Got D & Grade Point is: 1.00", font="23").place(x=700,y=350)
    else:
        Label(root, text="Opps it's fail. Better Luck Next Time", font="23").place(x=700,y=350)
    
#Higher Math Practical   
    if(higher_math_practical >=80):
        Label(root, text="Got A+ & Grade Point is: 5.00", font="23").place(x=710,y=385)
    elif(80>higher_math_practical >=70):
        Label(root, text="Got A & Grade Point is: 4.00", font="23").place(x=710,y=385)
    elif(70>higher_math_practical >=60):
        Label(root, text="Got A- & Grade Point is: 3.50", font="23").place(x=710,y=385)
    elif(60>higher_math_practical >=50):
        Label(root, text="Got B & Grade Point is: 3.00", font="23").place(x=710,y=385)
    elif(50>higher_math_practical >=40):
        Label(root, text="Got C & Grade Point is: 2.00", font="23").place(x=710,y=385)
    elif(40>higher_math_practical >=33):
        Label(root, text="Got D & Grade Point is: 1.00", font="23").place(x=710,y=385)
    else:
        Label(root, text="Opps it's fail. Better Luck Next Time", font="23").place(x=710,y=385)
    
    
#Biology Theory   
    if(biology_theory >=80):
        Label(root, text="Got A+ & Grade Point is: 5.00", font="23").place(x=700,y=420)
    elif(80>biology_theory >=70):
        Label(root, text="Got A & Grade Point is: 4.00", font="23").place(x=700,y=420)
    elif(70>biology_theory >=60):
        Label(root, text="Got A- & Grade Point is: 3.50", font="23").place(x=700,y=420)
    elif(60>biology_theory >=50):
        Label(root, text="Got B & Grade Point is: 3.00", font="23").place(x=700,y=420)
    elif(50>biology_theory >=40):
        Label(root, text="Got C & Grade Point is: 2.00", font="23").place(x=700,y=420)
    elif(40>biology_theory >=33):
        Label(root, text="Got D & Grade Point is: 1.00", font="23").place(x=700,y=420)
    else:
        Label(root, text="Opps it's fail. Better Luck Next Time", font="23").place(x=700,y=420)
    
#Biology Practical
    if(biology_practical >=80):
        Label(root, text="Got A+ & Grade Point is: 5.00", font="23").place(x=700,y=455)
    elif(80>biology_practical >=70):
        Label(root, text="Got A & Grade Point is: 4.00", font="23").place(x=700,y=455)
    elif(70>biology_practical >=60):
        Label(root, text="Got A- & Grade Point is: 3.50", font="23").place(x=700,y=455)
    elif(60>biology_practical >=50):
        Label(root, text="Got B & Grade Point is: 3.00", font="23").place(x=700,y=455)
    elif(50>biology_practical >=40):
        Label(root, text="Got C & Grade Point is: 2.00", font="23").place(x=700,y=455)
    elif(40>biology_practical >=33):
        Label(root, text="Got D & Grade Point is: 1.00", font="23").place(x=700,y=455)
    else:
        Label(root, text="Opps it's fail. Better Luck Next Time", font="23").place(x=700,y=455)
    
#Total Marks 
    total_marks = bangla_1st_paper + bangla_2nd_paper + english_1st_paper + english_2nd_paper + physics_theory + physics_practical + chemistry_theory + chemistry_practical + higher_math + higher_math_practical + biology_theory + biology_practical 
    
    Label(root, text=total_marks, font="impack 15 bold").place(x=175,y=485)
    # Average Mark(GPA)
    average_mark = int(total_marks/12);
    Label(root, text=average_mark, font="impack 15 bold").place(x=175,y=520)

# CGPA

    if(average_mark>=80):
        Label(root, text="A+", font="23").place(x=175,y=555)
    elif(80>average_mark >=70):
        Label(root, text="A", font="23").place(x=175,y=555)
    elif(70> average_mark >=60):
        Label(root, text="A-", font="23").place(x=175,y=555)
    elif(60>average_mark >=50):
        Label(root, text="B", font="23").place(x=175,y=555)
    elif(50>average_mark >=40):
        Label(root, text="C", font="23").place(x=175,y=555)
    elif(40>average_mark >=33):
        Label(root, text="D", font="23").place(x=175,y=555)
    else:
        Label(root, text="F", font="23").place(x=175,y=555)
    
    


#Button
Button(root, text="Calculate GPA", font="impack 15 bold", bg="light blue",command=calculate).place(x=350, y = 525)
Button(root, text="Exit", font="impack 15 bold", bg="red", fg="aqua",command=lambda:exit()).place(x=400, y = 600)

bangla_1st_paper_entry = Entry(root, font="20", width=15,bd = 2)
bangla_1st_paper_entry.place(x="180",y=70)

bangla_2nd_paper_entry = Entry(root, font="20", width=15,bd = 2)
bangla_2nd_paper_entry.place(x="180",y=105)

english_1st_paper_entry = Entry(root, font="20", width=15,bd = 2)
english_1st_paper_entry.place(x="180",y=140)

english_2nd_paper_entry = Entry(root, font="20", width=15,bd = 2)
english_2nd_paper_entry.place(x="180",y=175)


physics_theory_entry = Entry(root, font="20", width=15,bd = 2)
physics_theory_entry.place(x="180",y=210)

physics_practical_entry = Entry(root, font="20", width=15,bd = 2)
physics_practical_entry.place(x="180",y=245)

chemistry_theory_entry = Entry(root, font="20", width=15,bd = 2)
chemistry_theory_entry.place(x="180", y=280)

chemistry_practical_entry = Entry(root, font="20", width=15,bd = 2)
chemistry_practical_entry.place(x="180", y=315)

higher_math_entry = Entry(root, font="20", width=15,bd = 2)
higher_math_entry.place(x="180", y=350)

higher_math_practical_entry = Entry(root, font="20", width=15,bd = 2)
higher_math_practical_entry.place(x="190", y=385)

biology_theory_entry = Entry(root, font="20", width=15,bd = 2)
biology_theory_entry.place(x="180", y=420)


biology_practical_entry = Entry(root, font="20", width=15,bd = 2)
biology_practical_entry.place(x="180", y=455)

root.mainloop()
    


    



