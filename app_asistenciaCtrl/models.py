from django.db import models

# Create your models here.

class CompanyModels(models.Model):
    """Modelo para representar una empresa."""
    name = models.CharField(max_length=100, verbose_name="Nombre de la Empresa")
    location = models.CharField(max_length=100, verbose_name="Ubicación")
    established_date = models.DateField(verbose_name="Fecha de Establecimiento")

    def __str__(self):
        return self.name

class WorkerModels(models.Model):
    """Modelo para representar a un trabajador."""
    name = models.CharField(max_length=100, verbose_name="Nombre del Trabajador")
    position = models.CharField(max_length=100, verbose_name="Cargo")
    company = models.ForeignKey(CompanyModels, related_name='workers', on_delete=models.CASCADE, verbose_name="Empresa")

    def __str__(self):
        return self.name

class AttendanceModels(models.Model):
    """Modelo para registrar la asistencia diaria."""
    worker = models.ForeignKey(WorkerModels, related_name='attendances', on_delete=models.CASCADE, verbose_name="Trabajador")
    date = models.DateField(verbose_name="Fecha")
    present = models.BooleanField(default=False, verbose_name="Presente")

    def __str__(self):
        return f"{self.worker.name} - {self.date} - {'Presente' if self.present else 'Ausente'}"
