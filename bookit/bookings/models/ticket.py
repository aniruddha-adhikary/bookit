import base64

import PIL.Image
import qrcode
import uuid

import django.db.models.fields.files
from io import BytesIO

from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models


class Ticket(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    booking = models.ForeignKey(
        to='bookings.Booking'
    )

    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=0,
        )
        qr.add_data(self.uuid)
        qr.make(fit=True)

        img = qr.make_image()

        buffer = BytesIO()

        img.save(buffer, format='PNG')
        return base64.b64encode(buffer.getvalue())



