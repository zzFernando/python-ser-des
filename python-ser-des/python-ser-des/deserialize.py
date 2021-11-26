from pykson import Pykson, JsonObject, IntegerField, StringField, ObjectListField

class Course(JsonObject):
    name = StringField()
    teacher = StringField()


class Score(JsonObject):
    score = IntegerField()
    course = Course()


class Student(JsonObject):

    first_name = StringField()
    last_name = StringField()
    age = IntegerField()
    scores = ObjectListField(Score)


json_text = '{"first_name":"John", "last_name":"Smith", "age": 25, "scores": [ {"course": {"name": "Algebra", "teacher" :"Mr. Schmidt"}, "score": 100}, {"course": {"name": "Statistics", "teacher": "Mrs. Lee"}, "score": 90} ]}'
student = Pykson().from_json(json_text, Student)

print(student)