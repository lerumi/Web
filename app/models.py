from django.db import models
from django.utils import timezone

# Create your models here.
class QuestionManager(models.Manager):
    def new_questions(self):
        return self.order_by('-created_date', '-rating')

    def hot_questions(self):
        return self.order_by('-rating', '-created_date')
class AnswerManager(models.Manager):

    def hot_answers(self):
        return self.order_by('-rating', '-created_date')
class TagManager(models.Manager):

    def hot_tags(self):
        return self.order_by('-rating')

class base(models.Model):
    text = models.TextField(null=False, max_length=255)
    rating = models.IntegerField(default=0, db_index=True)
    created_date = models.DateTimeField(default=timezone.now, db_index=True)
    class Meta:
        abstract = True

class Profile(models.Model):
    user = models.OneToOneField('user', on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatars', default='avatars/user.png')

class Tag(models.Model):
    text = models.TextField(null=False, max_length=80)
    rating = models.IntegerField(default=0, db_index=True)

    objects = TagManager()

    def __str__(self):
        return f"{self.text}"
class Question(base):
    author = models.ForeignKey('user',
                               on_delete=models.CASCADE, related_name='question_author')
    title = models.CharField(null=False, max_length=255)
    tags = models.ManyToManyField(Tag, null=True, blank=True, max_length=3)
    correct_answer = models.OneToOneField('answer', related_name='+', null=True, blank=True, on_delete=models.CASCADE)
    objects = QuestionManager()
    def __str__(self):
        return f"{self.title}"

class answer(base):
    question = models.ForeignKey('Question', on_delete=models.PROTECT,
                                 related_name='answer_of_question',
                                 default=None, blank=False)
    author = models.ForeignKey('user', on_delete=models.CASCADE, related_name='answer_author')

    objects = AnswerManager()

    def __str__(self):
        return f"{self.author}"

class user(models.Model):
    name = models.CharField(null=False, max_length=255)
    created_date = models.DateTimeField(default=timezone.now, db_index=True)
    rating = models.IntegerField(default=0, db_index=True)
    def __str__(self):
        return f"{self.name}"
class AnswerLike(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    answer = models.ForeignKey(answer, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)

class QuestionLike(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)