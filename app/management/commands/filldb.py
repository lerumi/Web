from django.core.management import BaseCommand
from random import randint
from faker import Faker

from app.models import Tag, Question, answer, user, Profile, AnswerLike, QuestionLike

fake = Faker()


class Command(BaseCommand):
    help = "Fills database with fake data"

    def add_arguments(self, parser):
        parser.add_argument("ratio", type=int)

    def handle(self, *args, **kwargs):
        ratio = kwargs['ratio']
        tags = [
            Tag(
                text=fake.sentence(nb_words=1),
                rating = fake.random_int(min=0, max=ratio),
            ) for _ in range(ratio)
        ]
        Tag.objects.bulk_create(tags)
        tags = Tag.objects.all()

        users = [
            user(
                name = fake.first_name(),
                created_date = str(fake.date_between(start_date='-20y', end_date='-1d')),
                rating = fake.random_int(min=0, max=ratio),
            ) for _ in range(ratio)
        ]
        user.objects.bulk_create(users)
        users =user.objects.all()
        users_count = users.count()
        profiles = [
            Profile(
                user=users[i],
                nick_name = fake.sentence(nb_words=2)
            )for i in range(ratio)
        ]
        Profile.objects.bulk_create(profiles)
        questions=[
            Question(
                author = users[fake.random_int(min=0, max=users_count - 1)],
                title = fake.sentence(nb_words=3),
                text=fake.sentence(nb_words=10),
                created_date=str(fake.date_between(start_date='-20y', end_date='-1d')),

            )for _ in range(ratio*10)
        ]

        Question.objects.bulk_create(questions)
        questions = Question.objects.all()
        for i in questions:
            a=randint(1, 20)
            for_teg=[]
            for j in range(a-1):
                for_teg.append(tags[randint(0, ratio-1)])
            i.tags.add(*for_teg)
            i.save()
            for_teg.clear()

        answers = [
            answer(
                question=questions[fake.random_int(min=0, max=ratio*10 - 1)],
                author = users[fake.random_int(min=0, max=users_count - 1)],
                text = fake.sentence(nb_words=10),
                created_date=str(fake.date_between(start_date='-20y', end_date='-1d')),
            )for _ in range(ratio*100)
        ]
        answer.objects.bulk_create(answers)
        answers = answer.objects.all()

        for _ in range(ratio*100):
            like = QuestionLike(
                question=questions[fake.random_int(min=0, max=ratio*10 - 1)],
                user=users[fake.random_int(min=0, max=users_count - 1)],
                is_like=bool(randint(0, 1))
            )
            like_ans = AnswerLike(
                answer=answers[fake.random_int(min=0, max=ratio * 10 - 1)],
                user=users[fake.random_int(min=0, max=users_count - 1)],
                is_like=bool(randint(0, 1))
            )
            like.save()
            like_ans.save()
            if like.is_like:
                like.question.rating += 1
            like.question.save()

            if like_ans.is_like:
                like_ans.answer.rating += 1
            like_ans.answer.save()
