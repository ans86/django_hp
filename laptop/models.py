from django.db import models

class Laptop(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Image/")
    details = models.TextField()
    generation = models.TextField()
    ram = models.PositiveIntegerField(help_text="RAM in GB")  # ✅ Only positive numbers
    ssd = models.PositiveIntegerField(help_text="SSD in GB")  # ✅ Only positive numbers
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Laptop Entry: {self.name} | {self.ram}GB RAM, {self.ssd}GB SSD"
