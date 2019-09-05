from rest_framework.permissions import BasePermission
from datetime import date


class IsOwner(BasePermission):

	def has_object_permission(self, request, view, obj):
		if obj.user == request.user or request.user.is_staff:
			return True
		return False

class IsFuture(BasePermission):

	def has_object_permission(self, request, view, obj):
		days_left = (obj.date - date.today()).days
		if  days_left > 3:
			return True
		return False


