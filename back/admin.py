from django.contrib import admin

from back import models


@admin.register(models.Candidates)
class CandidatesAdmin(admin.ModelAdmin):
    list_display = ('id_candidates', 'f_i_o', 'f_i_o', 'add_date', 'description', 'review', 'working_place', 'salary', 'position')


@admin.register(models.Technologies)
class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ('id_tech', 'name')


@admin.register(models.Link)
class LickAdmin(admin.ModelAdmin):
    list_display = ('id_link', 'id_candidates', 'id_tech', 'level')