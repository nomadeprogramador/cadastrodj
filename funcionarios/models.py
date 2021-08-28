from django.db import models

# Create your models here.
class Funcionario(models.Model):
    sexo_op=(
        ('masculino','Masculino'),
        ('feminono','Feminino'),
    )
    nome = models.CharField(max_length=150)
    data_nascimento= models.DateField()
    cargo = models.CharField(max_length=100)
    sexo = models.CharField(choices=sexo_op,max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)


    def __str__(self) -> str:
        return self.nome