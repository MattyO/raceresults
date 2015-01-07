from django.contrib import admin
import common.models

admin.site.register(common.models.Org)
admin.site.register(common.models.BoatType)
admin.site.register(common.models.Boat)
admin.site.register(common.models.Race)
admin.site.register(common.models.RaceResult)
admin.site.register(common.models.Series)
