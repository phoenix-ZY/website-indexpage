from django.db import models
from users.models import User
import requests
from bs4 import BeautifulSoup
import os
from django.core.files.base import ContentFile
import pypinyin

def get_first_pinyin_letter(chinese):
    pinyin = pypinyin.pinyin(chinese[0], style=pypinyin.STYLE_NORMAL)[0][0]
    return pinyin[0].upper()
# Create your models here.
class LINK(models.Model):
    url = models.URLField(
        max_length=100, help_text="Enter a link of a website", unique=True
    )
    name = models.CharField(max_length=100, help_text="Enter the name of a website")
    user = models.ManyToManyField(User)
    image = models.ImageField(upload_to="link_image", null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.url

    @property
    def initial(self):
        if pypinyin.pinyin(self.name[0]):
            return get_first_pinyin_letter(self.name[0]).upper()
        return self.name[0].upper()

    @property
    def image_url(self):
        if self.image == "":
            # return "/media/static_default/{}.png".format(self.initial)
            headers = {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 6.2; WOW64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/30.0.1599.17 Safari/537.36"
                )
            }  # 伪装请求头
            try:
                response = requests.get(self.url, headers=headers, timeout=0.5)
            except:
                return "/media/static_default/{}.png".format(self.initial)
            soup = BeautifulSoup(response.text, "html.parser")
            favicon = soup.find(
                "link", href=True,  rel=lambda x: x and "icon" in x
            )
            # favicon = favicon[0] if favicon else None
            if favicon:
                favicon = favicon["href"]
            else:
                return "/media/static_default/{}.png".format(self.initial)
            if favicon.startswith("//"):
                favicon = "https:" + favicon
            elif favicon.startswith("/"):
                favicon = self.url + favicon
            if favicon:
                favicon_resp = requests.get(favicon, headers=headers)
                domain = self.url.split("//")[-1].split(".")[1]
                path = "media/link_image/"
                fullpath = path + domain + ".png"
                name = domain + ".png"
                self.image.save(name, ContentFile(favicon_resp.content))
            else:
                return "/media/static_default/{}.png".format(self.initial)
        return self.image.url
