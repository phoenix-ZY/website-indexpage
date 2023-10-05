from django.db import models
from users.models import User
import requests
from bs4 import BeautifulSoup


# Create your models here.
class LINK(models.Model):
    url = models.URLField(max_length=100, help_text="Enter a link of a website")
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
            response = requests.get(self.url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            favicon = soup.find("link", href=True, type="image/x-icon")["href"]
            if favicon:
                favicon_resp = requests.get(favicon, headers=headers)
                domain = self.url.split("//")[-1].split(".")[0]
                path = "/media/link_image/"
                fullpath = domain + path
                with open(fullpath, "wb") as f:
                    f.write(favicon_resp.content)
                self.image.url = fullpath
            else:
                self.image.url = "/media/static_default/{}.png".format(self.initial)
        return self.image.url
