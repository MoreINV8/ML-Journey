class Youtuber :
    def video(self) -> None:
        print("Filming the video....")
        
class Teacher :
    def teach(self) -> None:
        print("Teaching....")
        
class Student1(Teacher) :
    def study(self) -> None:
        print("Studing....")
        Teacher.teach(self=self)

print("1.")        
s1 = Student1()
s1.study()

#--------------------------------------

class Student2(Teacher, Youtuber) :
    # multiple inherit by SubClass(SuperClass1, SuperClass2, ...)
    def study(self) -> None:
        print("Studing....")
        Teacher.teach(self=self)
        Youtuber.video(self=self)
        
print("2.")
s2 = Student2()
s2.study()