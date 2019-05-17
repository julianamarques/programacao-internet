from django.db import models
from django.utils import timezone


class Processo(models.Model):
    numero = models.CharField(max_length=255, null=False, blank=False)
    texto = models.TextField(null=False, blank=False)
    tipo = models.ForeignKey("Tipo", on_delete=models.CASCADE)
    apensamento = models.ManyToManyField("self", through="Apensamento", symmetrical=False)
    interessados = models.ManyToManyField("Interessado")

    def __str__(self):
        return self.numero


class Interessado(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    data_nascimento = models.DateField(default=timezone.now, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    advogado = models.ForeignKey("Advogado", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Tipo(models.Model):
    TIPO = (
        ("S", "Sigiloso"), 
        ("N", "Normal"),
        ("A", "Administrativo"),
    )
    
    descricao = models.CharField(max_length=1, choices=TIPO)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.descricao

class Advogado(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    registro = models.ForeignKey("Registro", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Registro(models.Model):
    matricula = models.CharField(max_length=255, null=False, blank=False)
    data_validade = models.DateField(default=timezone.now, null=False, blank=False)

    def __str__(self):
        return self.matricula


class Apensamento(models.Model):
    processo_apensado = models.ForeignKey("Processo", on_delete=models.CASCADE, related_name="+")
    processo_original = models.ForeignKey("Processo", on_delete=models.CASCADE, related_name="+")
    data_apensamento = models.DateField(default=timezone.now, null=False, blank=False)
