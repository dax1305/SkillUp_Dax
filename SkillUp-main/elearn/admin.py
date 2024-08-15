from django.contrib import admin

from elearn.models import User, Profile, Announcement, Course, Tutorial, Notes, Quiz, Question, Answer, Learner, \
    Instructor, TakenQuiz, LearnerAnswer

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Announcement)
admin.site.register(Course)
admin.site.register(Tutorial)
admin.site.register(Notes)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Learner)
admin.site.register(Instructor)
admin.site.register(TakenQuiz)
admin.site.register(LearnerAnswer)


