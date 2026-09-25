from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BugForm
from .models import Bug

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

@login_required
def dashboard(request):
    bugs = Bug.objects.all()
    context = {
        "total": bugs.count(),
        "open_count": bugs.filter(status="Open").count(),
        "progress_count": bugs.filter(status="In Progress").count(),
        "resolved_count": bugs.filter(status="Resolved").count(),
        "critical_count": bugs.filter(priority="Critical").count(),
        "recent_bugs": bugs[:5],
    }
    return render(request, "dashboard.html", context)

@login_required
def bug_list(request):
    q = request.GET.get("q", "").strip()
    status = request.GET.get("status", "")
    priority = request.GET.get("priority", "")
    category = request.GET.get("category", "")

    bugs = Bug.objects.select_related("reported_by", "assigned_to")

    if q:
        bugs = bugs.filter(
            Q(title__icontains=q) | Q(description__icontains=q)
        )

    if status:
        bugs = bugs.filter(status=status)

    if priority:
        bugs = bugs.filter(priority=priority)

    if category:
        bugs = bugs.filter(category=category)

    return render(request, "bug_list.html", {
        "bugs": bugs,
        "q": q,
        "selected_status": status,
        "selected_priority": priority,
        "selected_category": category,
    })

@login_required
def bug_create(request):
    if request.method == "POST":
        form = BugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.reported_by = request.user
            bug.save()
            messages.success(request, "Bug reported successfully.")
            return redirect("bug_list")
    else:
        form = BugForm()
    return render(request, "bug_form.html", {"form": form, "page_title": "Report New Bug"})

@login_required
def bug_detail(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    return render(request, "bug_detail.html", {"bug": bug})

@login_required
def bug_update(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    if request.method == "POST":
        form = BugForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            messages.success(request, "Bug updated successfully.")
            return redirect("bug_detail", pk=bug.pk)
    else:
        form = BugForm(instance=bug)
    return render(request, "bug_form.html", {"form": form, "page_title": "Edit Bug"})

@login_required
def bug_delete(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    if request.method == "POST":
        bug.delete()
        messages.success(request, "Bug deleted successfully.")
        return redirect("bug_list")
    return render(request, "bug_confirm_delete.html", {"bug": bug})
