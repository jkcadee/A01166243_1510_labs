"""
David Han, Janelle Kwok
"""


class Student:

    __students = "A00000000"

    def __init__(self, first_name, last_name, *courses, middle_name=None):
        """
        Initialize a Student object.

        :param first_name: a string
        :param last_name: a string
        :param student_id: a string
        :param courses: tuples
        :param middle_name: a string
        :precondition: first_name, middle_name, and last_name, must be a string
        :precondition: student_id must be a string following the format "A0#######"
        :precondition: courses must be tuples of length 2 following the format (course_name, grade)
        """
        if not middle_name:
            middle_name = ""
        self.__first_name = first_name.title()
        self.__middle_name = middle_name.title()
        self.__last_name = last_name.title()
        self.__id = Student.__students
        self.__courses = dict(courses)
        Student.__students = "A" + f"{(int(Student.__students[1:]) + 1):08}"

    def get_gpa(self):
        """
        Get GPA of current student.

        :precondition: courses must be a non-empty list
        """
        gpa = 0
        for grade in self.__courses.values():
            gpa += grade
        return gpa / len(self.__courses)

    def get_student_information(self):
        """
        Get student's information.

        :postcondition: return a formatted string
        """
        return f"{self.__first_name} {self.__middle_name + ' ' if self.__middle_name else ''}{self.__last_name} " \
               f"({self.__id}) is taking {len(self.__courses)} courses with a GPA of {self.get_gpa():.2f}%!"

    def change_last_name(self, last_name):
        """
        Change student's last name.

        :param last_name: a string
        :precondition: last_name must be a string
        """
        self.__last_name = last_name.title()

    def add_course(self, course_name, grade):
        """
        Add a course to current student's courses.

        :param course_name: a string
        :param grade: a float
        :precondition: course_name must be a string
        :precondition: grade must be a float in the range [0.0, 100.0]
        """
        self.__courses[course_name] = grade


def main():
    student1 = Student("Nicole", "Brooks", ("COMP 1510", 95), ("COMP 1113", 87), ("COMP 1536", 94),
                       middle_name="Paige")
    student2 = Student("Cornelius", "Smith", ("COMM 1116", 45), ("COMP 1930", 65), ("COMP 1712", 75))
    student3 = Student("Harold", "Finch", ("COMP 1510", 37), ("COMP 1712", 40), ("COMM 1116", 0))

    print(student1.get_student_information())
    student1.change_last_name("Wang")
    print(student1.get_student_information())
    print(student2.get_student_information())
    print(student3.get_student_information())


if __name__ == "__main__":
    main()
