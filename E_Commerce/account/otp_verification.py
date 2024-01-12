import random
from django.conf import settings
from twilio.rest import Client
from datetime import datetime, timedelta


class OneTimePassword:

    def get_otp(self):
        OneTimePassword.otp_input = str(random.randint(100000,999999))
        OneTimePassword.exp_time = datetime.now() + timedelta(minutes=3)
        print("Generated OTP : ", self.otp_input)
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        # message = client.messages.create(
        #         body=f"The otp for verify your registration is : {OneTimePassword.otp_input}",
        #         from_='+13038168118',
        #         to='+917050876135'
        #     )

    def validate_otp(otp,request):
        if datetime.now() < OneTimePassword.exp_time:

            if OneTimePassword.otp_input == request.POST.get('otp'):
                print("Otp validation successful")
                return True

    