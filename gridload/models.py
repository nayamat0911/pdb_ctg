from django.db import models

# Create your models here.
class GridLoad(models.Model):    # -------------------------grid load------------------------
    grid_load = models.CharField( max_length=20);
    
    def __str__(self):
        return self.grid_load


class PDBShed(models.Model):     # --------------------------pdb shed----------------------------
    shed_pdb = models.CharField(max_length=20)


class REBShed(models.Model):     #-------------------------reb shed----------------------------------
    shed_reb = models.CharField(max_length=20)

class GridLoad_1(models.Model):     #-----------------------------grid load------------------------
    madunaghat = models.CharField(max_length=40)
    madunaghat1 = models.IntegerField()

    hathazari = models.CharField(max_length=20)
    hathazari1 = models.IntegerField()

    baklia = models.CharField(max_length=20)
    baklia1 = models.IntegerField()

    khulshi = models.CharField(max_length=20)
    khulshi1 = models.IntegerField()

    halishahor = models.CharField(max_length=20)
    halishahor1 = models.IntegerField()

    Agrabad = models.CharField(max_length=20)
    Agrabad1 = models.IntegerField()

    chandraghuna = models.CharField(max_length=20)
    chandraghuna1 = models.IntegerField()


    # baraulia = models.IntegerField(max_length=20)
    # cox_bazar = models.IntegerField(max_length=20)
    # dohazari = models.IntegerField(max_length=20)
    # matartbari = models.IntegerField(max_length=20)
    # shikolbaha = models.IntegerField(max_length=20)
    # baraiyarhat = models.IntegerField(max_length=20)
    # tk = models.IntegerField(max_length=20)

    # def __str__(self):
    #     return self.title


class MadunaghatREB(models.Model):     #-----------------------------grid load------------------------
    madunaghatGrid = (
        ('nowapara', 'nowapara'),
        ('Cuet', 'Cuet'),
        )
    gridName = models.ForeignKey(GridLoad, on_delete=models.CASCADE , max_length=100, default=False, choices=madunaghatGrid)
    nowapara = models.IntegerField()
    CUET = models.IntegerField()
    
    def __str__(self):
        return self.gridName
    
    
    # hathazari = models.IntegerField(max_length=20)

    # baklia = models.IntegerField(max_length=20)
    # khulshi = models.IntegerField(max_length=20)
    # halishahor = models.IntegerField(max_length=20)
    # Agrabad = models.IntegerField(max_length=20)
    # chandraghuna = models.IntegerField(max_length=20)
    # baraulia = models.IntegerField(max_length=20)
    # cox_bazar = models.IntegerField(max_length=20)
    # dohazari = models.IntegerField(max_length=20)
    # matartbari = models.IntegerField(max_length=20)
    # shikolbaha = models.IntegerField(max_length=20)
    # baraiyarhat = models.IntegerField(max_length=20)
    # tk = models.IntegerField(max_length=20)