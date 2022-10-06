from django.db import models

# Create your models here.

class User_details(models.Model):
    address_id = models.CharField(max_length=400, unique=True)
    username = models.CharField(max_length=300, blank=True, null=True, default="Untitled")
    bio = models.TextField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    website_link = models.URLField(unique=True, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True)
    profile_header_image = models.ImageField(blank=True, null=True)
    verifield = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.username}'


class User_followers(models.Model):
    username = models.OneToOneField(User_details, related_name="nft_address", on_delete=models.CASCADE)
    followers = models.ManyToManyField(User_details, blank=True)

    def __str__(self):
        return f'{self.username}'







class env_key(models.Model):
    string1 = models.CharField(max_length=200)
    string2 = models.CharField(max_length=200)
    string3 = models.CharField(max_length=200)
    string4 = models.CharField(max_length=200)





class User_favorite(models.Model):
    address = models.ForeignKey(User_details, related_name="nft_address_id", on_delete=models.CASCADE)
    favorites_id = models.CharField(max_length=200)

    def __str__(self):
        return str(self.address)




