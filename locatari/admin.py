from django.contrib import admin
from .models import Apartament, FacturiIntretinere, Aviz, Reclamatii


admin.site.register(Apartament)
admin.site.register(Aviz)


class FacturiIntretinereAdmin(admin.ModelAdmin):
    list_display = ('luna', 'suma_plata', 'contor_valoare', 'data_adaugarii')
    list_filter = ('luna',)
    search_fields = ('luna',)


admin.site.register(FacturiIntretinere, FacturiIntretinereAdmin)


class ReclamatiiAdmin(admin.ModelAdmin):
    list_display = ('user', 'titlu', 'category', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('user__username', 'titlu', 'description')
    actions = ['mark_as_in_progress', 'mark_as_resolved']

    def mark_as_in_progress(self, queryset):
        queryset.update(status='in_progress')

    mark_as_in_progress.short_description = 'Mark selected complaints as in progress'

    def mark_as_resolved(self, queryset):
        queryset.update(status='resolved')

    mark_as_resolved.short_description = 'Mark selected complaints as resolved'


admin.site.register(Reclamatii, ReclamatiiAdmin)

