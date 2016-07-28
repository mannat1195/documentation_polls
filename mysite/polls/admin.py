from django.contrib import admin

from .models import Choice,Question
# Register your models here.

#class ChoiceInline(admin.StackedInline): This takes a lot of space.
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3
#admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
	#fields=['pub_date , 'question_text']
	#adding fielsdets when there are more fields.
	#1st element of each tuple contains name of the fieldset.

	list_display=('question_text','pub_date','was_published_recently')
	list_filter=['pub_date']
	search_fields=['question_text']
	fieldsets=[
			(None,{'fields':['question_text']}),
			('Date information',{'fields':['pub_date'],'classes':['collapse']}),
	]
	inlines=[ChoiceInline]

admin.site.register(Question,QuestionAdmin)
