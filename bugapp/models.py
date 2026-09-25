from django.contrib.auth.models import User
from django.db import models


class Bug(models.Model):
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Critical", "Critical"),
    ]

    STATUS_CHOICES = [
        ("Open", "Open"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
    ]

    CATEGORY_CHOICES = [
        ("UI/UX", "UI/UX"),
        ("Functional", "Functional"),
        ("Database", "Database"),
        ("Security", "Security"),
        ("Performance", "Performance"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="Medium"
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="Functional"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Open"
    )
    reported_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reported_bugs"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_bugs"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title