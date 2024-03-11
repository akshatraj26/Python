class University:
    def __init__(self, uni_name):
        self.uni_name= uni_name
        
    def show_details(self):
        return f"Calling University class University Name: {self.uni_name}"
    
    
class Course(University):
    def __init__(self, uni_name, course):
        super().__init__(uni_name)
        self.course= course
        
    def show_details(self):
        return f"Using Course Class to call Course Name: {self.course} and University Name: {self.uni_name}"
    
class Branch(University):
    def __init__(self,uni_name, branch):
        super().__init__(uni_name)
        self.branch= branch
        
    def show_details(self):
        return f"Using Branch Class to call Branch Name: {self.branch} and University Name: {self.uni_name}"
    
class Student(Course, Branch):
    def __init__(self,student_name,uni_name='uni_name', branch='branch', course ='course'):
        Course.__init__(self, uni_name, course)
        Branch.__init__(self, uni_name, branch)
        
        # super().__init__()
        # super(Course, self).__init__(uni_name=uni_name, branch=branch)
        
        self.student_name= student_name
        
    def show_details(self):
        return f"Using Student Class to call Student Name: {self.student_name}, University Name: {self.uni_name}, Branch Name: {self.branch} and Course Name: {self.course} "


class Faculty(Branch):
    def __init__(self,branch, uni_name, faculty):
        super().__init__(branch, uni_name)
        self.faculty= faculty
        
    def show_details(self):
        return f"Calling Faculty class {self.faculty} and branch name {self.branch}, University Name: {self.uni_name}"
    


u = University('RGPV')
print(u.show_details()) 
c = Course('Rajiv Gandhi Pyoudyogiki', 'Masters')
print(c.show_details())


b = Branch('RGPV', 'Computer Science')
print(b.show_details())

f = Faculty('Computer Engineering', "RGPV",'Rajesh Tiwari SIr')
print(f.show_details())

s = Student("Akshat Raj", "Rajiv Gandhi Proudyogiki", 'Computer Science', 'B-Tech')
print(s.show_details())
