from django.db import models
from wagtail.images.models import Image, AbstractImage, AbstractRendition


class CustomImage(AbstractImage):
    # Optional text stored alongside the image.
    caption = models.CharField(max_length=255, blank=True)
    # Include the caption in Wagtail's image editing form.
    admin_form_fields = Image.admin_form_fields + ("caption",)


class CustomRendition(AbstractRendition):
    # Each generated rendition belongs to an image and is deleted with it.
    # Wagtail uses the "renditions" reverse relation to find these variants.
    image = models.ForeignKey(
        CustomImage,
        on_delete=models.CASCADE,
        related_name="renditions"
    )

    # Django reads Meta for configuration specific to this model.
    class Meta:
        # Prevent duplicate combinations of image, transformation, and focal point.
        unique_together = (("image", "filter_spec", "focal_point_key"),)