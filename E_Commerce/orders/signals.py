from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItems

@receiver(post_save, sender=OrderItems)
def new_order(sender, instance, created, **kwargs):
    if created:
        print('----------------------------------------------')
        print('Post save signal on creation of new orders')
        print('Sender: ', sender)
        print('Instance: ', instance)
        print('Created: ', created)
        print(f'kwargs: {kwargs}')
    else:
        print('----------------------------------------------')
        print('Post save signal on update of orders')
        print('Sender: ', sender)
        print('Instance: ', instance.quantity)
        print('Created: ', created)
        print(f'kwargs: {kwargs}')

# post_save.connect(new_order, sender=Order)