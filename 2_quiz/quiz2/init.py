from gistogramm.models import Gistogramm, Choice
from django.utils import timezone

p = Gistogramm(question="What's your name?", pub_date=timezone.now())
p.save()
p.id
p.choice_set.create(choice='A', votes=0)
p.choice_set.create(choice='B', votes=0)
p.choice_set.create(choice='C', votes=0)
p.choice_set.create(choice='D', votes=0)
p.save()
p.id