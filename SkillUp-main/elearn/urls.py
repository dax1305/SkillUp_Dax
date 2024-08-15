from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Shared URLs
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('lsign/', views.LearnerSignUpView.as_view(), name='lsign'),
    path('login_form/', views.login_form, name='login_form'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('password-reset/', PasswordResetView.as_view(template_name='password_reset_form.html'),
         name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    # Admin URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('course/', views.course, name='course'),
    path('isign/', login_required(views.InstructorSignUpView.as_view(), login_url='login_form'), name='isign'),
    path('addlearner/', login_required(views.AdminLearner.as_view(), login_url='login_form'), name='addlearner'),
    path('apost/', login_required(views.AdminCreatePost.as_view(), login_url='login_form'), name='apost'),
    path('alpost/', login_required(views.AdminListTise.as_view(), login_url='login_form'), name='alpost'),
    path('alistalltise/', login_required(views.ListAllTise.as_view(), login_url='login_form'), name='alistalltise'),
    path('adpost/<int:pk>', login_required(views.ADeletePost.as_view(), login_url='login_form'), name='adpost'),
    path('aluser/', login_required(views.ListUserView.as_view(), login_url='login_form'), name='aluser'),
    path('aduser/<int:pk>', login_required(views.ADeleteuser.as_view(), login_url='login_form'), name='aduser'),
    path('create_user_form/', views.create_user_form, name='create_user_form'),
    path('create_user/', views.create_user, name='create_user'),
    path('acreate_profile/', views.acreate_profile, name='acreate_profile'),
    path('auser_profile/', views.auser_profile, name='auser_profile'),

    # Instructor URLs
    path('instructor/', views.home_instructor, name='instructor'),
    path('quiz_add/', login_required(views.QuizCreateView.as_view(), login_url='login_form'), name='quiz_add'),
    path('question_add/<int:pk>', views.question_add, name='question_add'),
    path('quiz/<int:quiz_pk>/<int:question_pk>/', views.question_change, name='question_change'),
    path('llist_quiz/', login_required(views.QuizListView.as_view(), login_url='login_form'), name='quiz_change_list'),
    path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', login_required(views.QuestionDeleteView.as_view(), login_url='login_form'),
         name='question_delete'),
    path('quiz/<int:pk>/results/', login_required(views.QuizResultsView.as_view(), login_url='login_form'), name='quiz_results'),
    path('quiz/<int:pk>/delete/', login_required(views.QuizDeleteView.as_view(), login_url='login_form'), name='quiz_delete'),
    path('quizupdate/<int:pk>/', login_required(views.QuizUpdateView.as_view(), login_url='login_form'), name='quiz_change'),
    path('ipost/', login_required(views.CreatePost.as_view(), login_url='login_form'), name='ipost'),
    path('llchat/', login_required(views.TiseList.as_view(), login_url='login_form'), name='llchat'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('post/', views.publish_tutorial, name='publish_tutorial'),
    path('itutorial/', views.itutorial, name='itutorial'),
    path('itutorials/<int:pk>/', login_required(views.ITutorialDetail.as_view(), login_url='login_form'), name="itutorial-detail"),
    path('listnotes/', login_required(views.LNotesList.as_view(), login_url='login_form'), name='lnotes'),
    path('iadd_notes/', views.iadd_notes, name='iadd_notes'),
    path('publish_notes/', views.publish_notes, name='publish_notes'),
    path('update_file/<int:pk>', views.update_file, name='update_file'),

    # Learner URl's
    path('learner/', views.home_learner, name='learner'),
    path('singlecourse/<int:course_type>', views.single_course, name='singlecourse'),
    path('ltutorial/', views.ltutorial, name='ltutorial'),
    path('llistnotes/', login_required(views.LLNotesList.as_view(), login_url='login_form'), name='llnotes'),
    path('ilchat/', login_required(views.ITiseList.as_view(), login_url='login_form'), name='ilchat'),
    path('luser_profile/', views.luser_profile, name='luser_profile'),
    path('lcreate_profile/', views.lcreate_profile, name='lcreate_profile'),
    path('tutorials/<int:pk>/', login_required(views.LTutorialDetail.as_view(), login_url='login_form'), name="tutorial-detail"),
    path('interests/', login_required(views.LearnerInterestsView.as_view(), login_url='login_form'), name='interests'),
    path('learner_quiz/', login_required(views.LQuizListView.as_view(), login_url='login_form'), name='lquiz_list'),
    path('taken/', login_required(views.TakenQuizListView.as_view(), login_url='login_form'), name='taken_quiz_list'),
    path('quiz/<int:pk>/', views.take_quiz, name='take_quiz'),




    path('config/', views.stripe_config),  # new
    path('create-checkout-session/', views.create_checkout_session),  # new
    path('success/', views.SuccessView.as_view()),  # new
    path('cancelled/', views.CancelledView.as_view()),  # new

]
