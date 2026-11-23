from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model

from wagtail.models import Page


class HomePage(Page):
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True, null=True)

    # Optional foreign key to the custom image model defined in apps/images/models.py
    image = models.ForeignKey(
        # Figures out what the image model is`
        get_image_model(),  # This will resolve to 'images.CustomImage'
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = [
        FieldPanel('subtitle'),
        FieldPanel('body'),
        FieldPanel('image'),
    ]