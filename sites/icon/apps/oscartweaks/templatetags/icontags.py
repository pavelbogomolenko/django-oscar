__author__ = 'pavelbogomolenko'

from categories.models import CategoryRelation
from oscar.apps.catalogue.models import Category
from django import template

register = template.Library()

@register.filter(name='addcss')
def addcss(value, arg):
	return value.as_widget(attrs={'class': arg})

class RelatedCategoryNode(template.Node):
	def __init__(self, node):
		self.node = template.Variable(node)
	def render(self, context):
		try:
			actual_node = self.node.resolve(context)
			related_relation = CategoryRelation.objects.filter(category=actual_node.pk)
			if not related_relation:
				return ''
			category = Category.objects.filter(pk=related_relation.get().object_id)
			if not category:
				return ''
			context['related_cat_node'] = category.get()
			return ''
		except template.VariableDoesNotExist:
			return ''

@register.tag(name="related_category_node")
def related_category_node(parser, token):
	try:
		tag_name, node = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
	return RelatedCategoryNode(node)

