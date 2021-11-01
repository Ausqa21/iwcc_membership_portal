from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Location)
admin.site.register(Branch)
admin.site.register(Role)
admin.site.register(Group)
admin.site.register(GroupRole)
admin.site.register(Member)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(MemberRole)
admin.site.register(GroupMembership)
admin.site.register(GroupMembershipRole)
admin.site.register(GroupEvent)
admin.site.register(EventLocation)
admin.site.register(Event)
