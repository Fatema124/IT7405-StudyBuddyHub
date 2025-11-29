from django.shortcuts import render
from datetime import datetime
from .forms import JoinStudyGroupForm
from .mongo_connection import groups_col, join_form_requests_col
# Create your views here.
def home(request):
    # Read a few study groups from MongoDB
    groups_cursor = groups_col.find().limit(5)
    groups = list(groups_cursor)

    context = {
        "groups": groups
    }
    return render(request, "core/home.html", context)

def join_group(request):
    if request.method == "POST":
        form = JoinStudyGroupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # insert a new document into MongoDB
            join_form_requests_col.insert_one({
                "full_name": data["full_name"],
                "email": data["email"],
                "course_code": data["course_code"],
                "message": data["message"],
                "requested_at": datetime.utcnow(),
            })
            # appear simple thank you page
            return render(request, "core/join_success.html", {"form": form})
    else:
        form = JoinStudyGroupForm()

    return render(request, "core/join_group.html", {"form": form})
