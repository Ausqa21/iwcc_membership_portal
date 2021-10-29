from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    primary = models.TextField()
    secondary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.primary} || {self.secondary}"


class Branch(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class GroupRole(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    SINGLE = "SINGLE"
    ENGAGED = "ENGAGED"
    MARRIED = "MARRIED"
    WIDOWED = "WIDOWED"
    COMPLICATED = "COMPLICATED"

    MARITAL_STATUS = [
        (SINGLE, "Single"),
        (ENGAGED, "Engaged"),
        (MARRIED, "Married"),
        (WIDOWED, "Widowed"),
        (COMPLICATED, "Complicated"),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    marital_status = models.CharField(max_length=15, choices=MARITAL_STATUS, default=SINGLE)
    occupation = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, through="GroupMembership")
    roles = models.ManyToManyField(Role, through="MemberRole")
    group_roles = models.ManyToManyField(GroupRole, through="GroupMembershipRole")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contact(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    mobile_1 = models.CharField(max_length=12)
    mobile_2 = models.CharField(max_length=12)
    work = models.CharField(max_length=12)
    ice_1 = models.CharField(max_length=12)
    ice_2 = models.CharField(max_length=12)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.mobile_1}, {self.work}, {self.ice_1}, {self.email}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Event(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    end_date = models.DateField()
    branches = models.ManyToManyField(Branch, through="EventLocation")
    groups = models.ManyToManyField(Group, through="GroupEvent")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MemberRole(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    date_assigned = models.DateField()
    date_expired = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} - {self.role.name}"


class GroupMembership(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_exited = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} - {self.group.name}"


class GroupMembershipRole(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    group_role = models.ForeignKey(GroupRole, on_delete=models.CASCADE)
    date_assigned = models.DateField()
    date_expired = models.DateField()
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} - {self.group_role.name}"


class GroupEvent(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.group.name} {self.event.name}"


class EventLocation(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.branch.name} - {self.event.name}"
