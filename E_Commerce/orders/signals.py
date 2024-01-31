from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItems
import requests

@receiver(post_save, sender=OrderItems)
def new_order(sender, instance, created, **kwargs):
    pass
    # Construct your data to be sent
#     data_to_send = {'key': 'value', 'other_key': 'other_value'}

#     # Specify the URL where you want to send the data
#     target_url = 'http://127.0.0.1:8000/admin-panel/dashboard'

#     # Send the data asynchronously
#     try:
#         response = requests.post(target_url, json=data_to_send)
#         # Check the response status code or handle any other response details as needed
#         if response.status_code == 200:
#             print("Data sent successfully!")
#         else:
#             print(f"Failed to send data. Status code: {response.status_code}")
#     except requests.RequestException as e:
#         print(f"Error sending data: {e}")
# # post_save.connect(new_order, sender=Order)