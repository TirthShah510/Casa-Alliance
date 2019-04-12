from django.contrib import admin
from basic_app.models import Profile, Property, HouseholdTypes, HouseholdServices, ComplaintPost, NoticePost, Hall, \
    Report, Prediction, \
    Visitor, Vendor, Committee, Choice, Question, VoteDone, Blog, CommentAdd, Vehicle, Staff

# Register your models here.

admin.site.register(Property)
admin.site.register(HouseholdTypes)
admin.site.register(HouseholdServices)
admin.site.register(ComplaintPost)
admin.site.register(NoticePost)
admin.site.register(Hall)
admin.site.register(Profile)
admin.site.register(Report)
admin.site.register(Prediction)
admin.site.register(Visitor)
admin.site.register(Vendor)
admin.site.register(Committee)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(VoteDone)

admin.site.register(Blog)
admin.site.register(CommentAdd)

admin.site.register(Vehicle)
admin.site.register(Staff)
