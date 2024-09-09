from django.db import models
import os

class Skill(models.Model):
    image = models.ImageField(upload_to="skills/img")
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    experience = models.IntegerField()
    file_pdf = models.FileField(upload_to="skills/pdf", null=True, blank=True) 
    
    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if self.pk:  # Si el objeto ya existe, es una actualización
            old_instance = Skill.objects.get(pk=self.pk)
            
            # Manejo de la imagen
            if old_instance.image and self.image != old_instance.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
            
            # Manejo del archivo PDF
            if old_instance.file_pdf and self.file_pdf != old_instance.file_pdf:
                if os.path.isfile(old_instance.file_pdf.path):
                    os.remove(old_instance.file_pdf.path)
        
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Eliminar la imagen si existe
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        
        # Eliminar el archivo PDF si existe
        if self.file_pdf:
            if os.path.isfile(self.file_pdf.path):
                os.remove(self.file_pdf.path)
        
        super().delete(*args, **kwargs)

    
