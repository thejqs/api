import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from project.api.models import Factory, Sprocket


def factories(request):
    data = list(Factory.objects.all().values("id", "chart_data"))
    return JsonResponse(data, safe=False)


def factory(request, factory_id):
    data = list(Factory.objects.filter(id=factory_id).values("id", "chart_data"))
    return JsonResponse(data, safe=False)


def chart_data(request, factory_id):
    data = Factory.objects.filter(id=factory_id).values("id", "chart_data")[0]
    return JsonResponse(data["chart_data"], safe=False)


def production_actual(request, factory_id):
    data = Factory.objects.filter(id=factory_id).values("id", "chart_data")[0]
    return JsonResponse(data["chart_data"]["sprocket_production_actual"], safe=False)


def production_goal(request, factory_id):
    data = Factory.objects.filter(id=factory_id).values("id", "chart_data")[0]
    return JsonResponse(data["chart_data"]["sprocket_production_goal"], safe=False)
    

def time(request, factory_id):
    data = Factory.objects.filter(id=factory_id).values("id", "chart_data")[0]
    return JsonResponse(data["chart_data"]["time"], safe=False)


def sprockets(request):
    data = list((Sprocket.objects.all()
        .values("teeth", "pitch", "pitch_diameter", "outside_diameter")
    ))
    return JsonResponse(data, safe=False)


def sprocket(request, sprocket_id):
    data = list((Sprocket.objects.filter(id=sprocket_id)
        .values("teeth", "pitch", "pitch_diameter", "outside_diameter")
    ))
    return JsonResponse(data, safe=False)


def sprocket_create(request, teeth, pitch_diameter, outside_diameter, pitch):
    msg = {
        "message": "",
        "status_code": None
    }

    try:
        s_created = Sprocket.objects.create(
            teeth=teeth,
            pitch_diameter=pitch_diameter,
            outside_diameter=outside_diameter,
            pitch=pitch
        )
        s_created.save()
        msg["message"] = "success"
        msg["status_code"] = 200
    except Exception as e:
        msg["message"] = "error"
        msg["error"] = e
        msg["status_code"] = 400

    return JsonResponse(msg, safe=False)


def sprocket_update(request, sprocket_id, teeth, pitch_diameter, outside_diameter, pitch):
    msg = {
        "message": "",
        "status_code": None
    }

    try:
        to_update = Sprocket.objects.filter(id=sprocket_id)
        to_update.update(
            teeth=teeth,
            pitch_diameter=pitch_diameter,
            outside_diameter=outside_diameter,
            pitch=pitch
        )
        msg["message"] = f"success! updated sprocket ID {sprocket_id}"
        msg["status_code"] = 200
    except Exception as e:
            msg["message"] = "error"
            msg["error"] = e
            msg["status_code"] = 400

    return JsonResponse(msg, safe=False)

