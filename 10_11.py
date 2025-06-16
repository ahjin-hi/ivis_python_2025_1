class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.korean_quiz = 0
        self.math_quiz = 0
        self.science_quiz = 0

    def set_korean_quiz(self,num):
        self.korean_quiz = num

    def set_math_quiz(self,num):
        self.math_quiz = num

    def set_science_quiz(self,num):
        self.science_quiz = num

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id

    def get_korean_quiz(self):
        return self.korean_quiz

    def get_math_quiz(self):
        return self.math_quiz

    def get_science_quiz(self):
        return self.science_quiz

    def get_total_score(self):
        return self.korean_quiz + self.math_quiz + self.science_quiz

    def get_avg_score(self):
        return self.get_total_score() / 3

    def __str__(self):
        return (
            f'국어 성적 : {self.korean_quiz}, 수학성적 : {self.math_quiz}, 과학 성적 : {science_quiz}, 합계 : {self.get_total_score()}, 평균 : {self.get_avg_score()}')


name = input('학생의 이름을 입력하세요: ')
student_id = input ('학생의 학번을 입력하세요: ')
student = Student(name,student_id)

korean_quiz = int(input('학생의 국어 성적을 입력하세요:'))
math_quiz = int(input('학생의 수학 성적을 입력하세요: '))
science_quiz = int(input('학생의 과학 성적을 입력하세요:'))

student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)
print(student)