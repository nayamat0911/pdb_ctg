from django.db import models

# Create your models here.
# Create your models here.
class khulshiGrid(models.Model):    # -------------------------Khulshi grid load--1----------------------
    Time = models.DateTimeField(auto_now=True)
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    BSRM = models.PositiveIntegerField()


class HathazariGrid(models.Model):    # -------------------------Hathazari grid load---2---------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    shed_reb = models.PositiveIntegerField()


class Hathazari_REB(models.Model):    # ---------------------REB load---3---------------------
    Fotikchori = models.PositiveIntegerField()
 

class HalishahorGrid(models.Model):    # -------------------------halishahor grid load---3---------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    


class BakliaGrid(models.Model):    # ------------------------- Baklia grid load---4---------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    
    

class AgrabadGrid(models.Model):    # ------------------------- Agrabad grid load--5----------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    

class RampurGrid(models.Model):    # ------------------------- Rampur grid load----6--------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    

class SholoshahorGrid(models.Model):    # ------------------------- Sholoshahor grid load---7---------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    

class KalurghatGrid(models.Model):    # ------------------------- Kalurghat grid load---8---------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    

class BarauliaGrid(models.Model):    # ------------------------- Baraulia grid load-----9-------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    Reb_Shed = models.PositiveIntegerField()

class Baraulia_REB(models.Model):    # -----------------------REB load-----9-------------------
    doom = models.PositiveIntegerField();
    

class ShahmirpurGrid(models.Model):    # ------------------------- shahmirpur grid load----10--------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    reb_shed = models.PositiveIntegerField()

class Shahmirpur_REB(models.Model):    # --------------------REB load----10--------------------
    Anowara = models.PositiveIntegerField()
    HM_Steel = models.PositiveIntegerField()
    Bashkhali = models.PositiveIntegerField()

class JuldaGrid(models.Model):    # ------------------------- Julda grid load----11--------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    Reb_Shed = models.PositiveIntegerField()

class Julda_REB(models.Model):    # ------------------------- Julda grid load----11--------------------
    Julda_reb = models.PositiveIntegerField()

class MadunaghatGrid(models.Model):    # ------------------------- Madunaghat grid load---12---------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    Reb_Shed = models.PositiveIntegerField()

class Madunaghat_REB(models.Model): #----------------------reb----------------------------
    # grid = models.ForeignKey(MadunaghatGrid , on_delete=models.CASCADE, default=True)
    CUET = models.PositiveIntegerField()
    Nowapara = models.PositiveIntegerField()


class ChandroghunaGrid(models.Model):    # ------------------------- Chandroghuna grid load----13--------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    Reb_Shed = models.PositiveIntegerField()

class Chandroghuna_REB(models.Model):   # ------------------------- reb------------------------
    # grid = models.ForeignKey(ChandroghunaGrid,on_delete=models.CASCADE, null=True);
    Rangunia = models.PositiveIntegerField()
    Kodala = models.PositiveIntegerField()

class DuhazariGrid(models.Model):    # ------------------------- Duhazari grid load----14--------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    Reb_Shed = models.PositiveIntegerField()

class Duhazari_REB(models.Model):    # ------------------------- Duhazari REB load----14--------------------
    Patiya = models.PositiveIntegerField()
    Lohagora = models.PositiveIntegerField()
    Chondanaish = models.PositiveIntegerField()
    keranirhat = models.PositiveIntegerField()
    Bashkhali = models.PositiveIntegerField()

class CoxBazarGrid(models.Model):    # ------------------------- Cox'sBazar grid load----15--------------------
    Grid_Load = models.PositiveIntegerField( );
    PDB_Shed = models.PositiveIntegerField()
    Reb_Shed = models.PositiveIntegerField()

class CoxBazar_REB(models.Model):    # ------------------ REB load----15--------------------
    Sodor = models.PositiveIntegerField()
    Ukiya = models.PositiveIntegerField()
    Teknaf = models.PositiveIntegerField()
    chokoria = models.PositiveIntegerField()

class MatarbariGrid(models.Model):    # ------------------------- Matarbari grid load----16--------------------
    Grid_Load = models.PositiveIntegerField();
    Reb_Shed = models.PositiveIntegerField()

class Matarbari_REB(models.Model):    # -------------------- REB load----16--------------------
    Chokoriya = models.PositiveIntegerField()
    Moheskhali = models.PositiveIntegerField()
    CoalPower = models.PositiveIntegerField()
    Singapur = models.PositiveIntegerField()

class KhagrachariGrid(models.Model):    # ------------------------- Khagrachari grid load----17--------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    Reb_Shed = models.PositiveIntegerField()

class RanghamatiGrid(models.Model):    # ------------------------- Ranghamati grid load-----18-------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    Reb_Shed = models.PositiveIntegerField()

class BarairhatGrid(models.Model):    # ------------------------- Barairhat grid load----19--------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    Reb_Shed = models.PositiveIntegerField()

class Barairhat_REB(models.Model):    # ---------------------REB load----19--------------------
    Bariryarhat = models.PositiveIntegerField()


class AKS132kvGrid(models.Model):    # ------------------------- AKS132 grid load----20--------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    

class KsrmGrid(models.Model):    # ------------------------- KSRM grid load------21------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    

class MSMLGrid(models.Model):    # ------------------------- MSML grid load-----22-------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    

class SASMGrid(models.Model):    # ------------------------- SASM grid load------23------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
   

class ShikalbhahaGrid(models.Model):    # ------------------------- shikalbaha grid load-----24-------------------
    Grid_Load = models.PositiveIntegerField()
    PDB_Shed = models.PositiveIntegerField()
    Reb_Shed = models.PositiveIntegerField()

class Shikalbhaha_REB(models.Model):    # ----------------------REB load-----24-------------------
    Anowara = models.PositiveIntegerField()
    Boalkhali = models.PositiveIntegerField()
    

class TKGrid(models.Model):    # ------------------------- TK grid load-----25-------------------
    Grid_Load = models.PositiveIntegerField();
    PDB_Shed = models.PositiveIntegerField()
    Reb_Shed = models.PositiveIntegerField()
    def __str__(self):
        return self.grid_load,"TK 132 kv"

class TK_REB(models.Model):    # ----------------------REB load-----25-------------------
    Bashkhali = models.PositiveIntegerField();
    Potiya = models.PositiveIntegerField()
    

class KaptaiGrid(models.Model):    # ------------------------- Kkaptai grid load----26--------------------
    Grid_Load = models.PositiveIntegerField()
    PDB_Shed = models.PositiveIntegerField()
    Reb_Shed = models.PositiveIntegerField()


# Industray 230 kv 
class ASK230KVGrid(models.Model):    # ------------------------- ASK 230KV grid load----27--------------------
    Grid_Load = models.PositiveIntegerField(null=False)
    def __str__(self):
        return self.grid_load,"AKS 230 kv"

class BSRM230KVGrid(models.Model):    # ------------------------- BSRM 230KV Grid load----28--------------------
    Grid_Load = models.PositiveIntegerField(null=False)
    
class GPH230KVGrid(models.Model):    # ------------------------- GPH 230KV Grid load----29--------------------
    Grid_Load = models.PositiveIntegerField(null=True)
    
class MirashoraiEZ(models.Model):    # ------------------------- MirashoraiEZ 230KV Grid load----30--------------------
    Grid_Load = models.PositiveIntegerField(null=True)
    
    
    