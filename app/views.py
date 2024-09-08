import json
import os
from pathlib import Path
import subprocess

from django.views import View
from django.shortcuts import render, HttpResponse
from django.conf import settings

from .models import ButtonTable, File

# Create your views here.
PARSER_PATH = settings.BASE_DIR / "parser/script.py"
MEDIA_ROOT = path = Path(settings.MEDIA_ROOT)


def decode_request(request):
    body_unicode = request.body.decode('utf-8')
    received_json = json.loads(body_unicode)

    return received_json


class IndexView(View):
    def get(self,request):
        button = ButtonTable.objects.first()
        files = File.objects.all()

        file_names = []

        for file in files:
            path = file.file
            last_slash_index = path.rfind('/', 0)

            file_name = path[last_slash_index + 1:]

            file_names.append(file_name)

        context = {
            "button": button,
            "files": file_names[::-1],
        }

        return render(request,"index.html", context=context)

    def post(self,request):
        button = ButtonTable.objects.first()
        button.change_status()

        business_type = decode_request(request)["business_type"]

        try:
            subprocess.run(["python3", PARSER_PATH, "--bt", f'{business_type}'])
        except:
            button.change_status()

        files = MEDIA_ROOT.glob("*_merge.xlsx")

        latest_xlsx = max(files, key=lambda x: x.stat().st_ctime)

        File.create(latest_xlsx)

        button.change_status()
        return HttpResponse()


class DeleteView(View):
    def post(self,request):
        files = File.objects.all()

        for file in files:
            os.remove(file.file)
            file.delete()

        return HttpResponse()