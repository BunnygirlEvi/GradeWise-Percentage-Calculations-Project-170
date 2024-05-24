from tkinter import *
root = Tk()
root.title("Gradewise Percentage Calculation")
root.geometry("500x600")

percentage_grade_3_label = Label(root)
percentage_grade_5_label = Label(root)
percentage_grade_10_label = Label(root)
class grade_3:
    def __init__(self, language_arts, mathematics):
        self.language_arts = language_arts
        self.mathematics = mathematics
    def percentage(self):
        total_marks = self.language_arts + self.mathematics
        total_marks_with_100 = total_marks * 100
        grade_3_percentage = total_marks_with_100/200
        percentage_grade_3_label["text"] = grade_3_percentage
         
class grade_5:
    def __init__(self, language_arts, mathematics, social_studies):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies
        total_marks_with_100 = total_marks * 100
        grade_5_percentage = total_marks_with_100/200
        percentage_grade_5_label["text"] = grade_5_percentage

class grade_10:
    def __init__(self, language_arts, mathematics, social_studies, art):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        self.art = art
    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies + self.art
        total_marks_with_100 = total_marks * 100
        grade_10_percentage = total_marks_with_100/200
        percentage_grade_10_label["text"] = grade_10_percentage
        
obj_grade_3 = grade_3(40,50)
obj_grade_5 = grade_5(40,50,90)
obj_grade_10 = grade_10(40,50,90,120)

grade_3_btn = Button(root, text="Grade 3", command = obj_grade_3.percentage)

percentage_grade_3_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)

grade_3_btn.place(relx = 0.5, rely = 0.3, anchor = CENTER)

grade_5_btn = Button(root, text="Grade 5", command = obj_grade_5.percentage)

grade_5_btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

percentage_grade_5_label.place(relx = 0.5, rely = 0.4, anchor = CENTER)

grade_10_btn = Button(root, text="Grade 10", command = obj_grade_10.percentage)

grade_10_btn.place(relx = 0.5, rely = 0.7, anchor = CENTER)

percentage_grade_10_label.place(relx = 0.5, rely = 0.6, anchor = CENTER)



root.mainloop() 

   
    
    