from django.contrib import admin


from categories.admin import Category, CategoryAdmin
from categories.models import CategoryRelation

class MyInlineCategoryRelation(admin.options.InlineModelAdmin):
	model = CategoryRelation
	template = 'admin/edit_inline/gen_coll_tabular.html'


class IconCategoryAdmin(CategoryAdmin):
	inlines = [MyInlineCategoryRelation, ]


#fix broken InlineCategoryRelation
admin.site.unregister(Category)
admin.site.register(Category, IconCategoryAdmin)