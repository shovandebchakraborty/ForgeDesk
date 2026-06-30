from django.db import models

# Create your models here.
class ProjectStructure(models.Model):
    Project_id = models.AutoField(primary_key=True)
    Icon = models.TextField(default='📁')
    Name = models.CharField(max_length=150)
    Description = models.TextField(blank=True)

    def __str__(self):
        return(
            f"Project ID: {self.Project_id} | "
            f"Project Name: {self.Name} | "
            f"Description: {self.Description[:50]}..."
        )