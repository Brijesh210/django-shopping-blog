# multiple FK , give whole tree and give the instance needed
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'accounts.User'  # Equivalent to ``model = myapp.models.User``
