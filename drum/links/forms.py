
from django.conf import settings
from django.forms.models import modelform_factory
from django.forms import ValidationError

from drum.links.models import Link


BaseLinkForm = modelform_factory(Link, fields=["link", "title", "description"]
                                 , labels={"title":"제목", "link":"링크", "description":"설명"})


class LinkForm(BaseLinkForm):

    def clean(self):
        link = self.cleaned_data.get("link", None)
        title = self.cleaned_data.get("title", None)
        # description = self.cleaned_data.get("description", None)

        if not link or not title:
            raise ValidationError("link and title are required")
        return self.cleaned_data
