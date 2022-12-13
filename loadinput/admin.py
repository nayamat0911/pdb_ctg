from django.contrib import admin
from .models import khulshiGrid,HathazariGrid,HalishahorGrid,BakliaGrid,AgrabadGrid,RampurGrid ,SholoshahorGrid
from .models import KalurghatGrid,BarauliaGrid,ShahmirpurGrid,JuldaGrid, MadunaghatGrid,ChandroghunaGrid
from .models import DuhazariGrid,CoxBazarGrid,MatarbariGrid, KhagrachariGrid,RanghamatiGrid,BarairhatGrid
from .models import AKS132kvGrid ,KsrmGrid,MSMLGrid,SASMGrid, ShikalbhahaGrid,KaptaiGrid,TKGrid

# 230 KV 
from .models import ASK230KVGrid,BSRM230KVGrid,GPH230KVGrid,MirashoraiEZ
# reb 
from .models import Madunaghat_REB

# Register your models here.
admin.site.register(khulshiGrid)
admin.site.register(RampurGrid)
admin.site.register(AgrabadGrid)
admin.site.register(SholoshahorGrid)
admin.site.register(BarauliaGrid)
admin.site.register(KalurghatGrid)
admin.site.register(ShahmirpurGrid)
admin.site.register(RanghamatiGrid)
admin.site.register(ShikalbhahaGrid)
admin.site.register(BarairhatGrid)
admin.site.register(SASMGrid)
admin.site.register(MSMLGrid)
admin.site.register(TKGrid)
admin.site.register(AKS132kvGrid)
admin.site.register(HathazariGrid)
admin.site.register(KhagrachariGrid)
admin.site.register(ChandroghunaGrid)
admin.site.register(JuldaGrid)
admin.site.register(BakliaGrid)
admin.site.register(KaptaiGrid)
admin.site.register(MatarbariGrid)
admin.site.register(DuhazariGrid)
admin.site.register(HalishahorGrid)
admin.site.register(MadunaghatGrid)
admin.site.register(CoxBazarGrid)
admin.site.register(KsrmGrid)



# 230 KV industry load
admin.site.register(ASK230KVGrid)
admin.site.register(BSRM230KVGrid)
admin.site.register(GPH230KVGrid)
admin.site.register(MirashoraiEZ)

# reb 
admin.site.register(Madunaghat_REB)