import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


def factories(request):
    with open("data/seed_factory_data.json") as sf:
        data = json.load(sf)
        data["count"] = len(data["factories"])
        return JsonResponse(data, safe=False)


def factory(request, factory_id):
        with open("data/seed_factory_data.json") as ss:
            data = json.load(ss)
            return JsonResponse(data["factories"][int(factory_id)], safe=False)


def chart_data(request, factory_id):
    with open("data/seed_factory_data.json") as ss:
        data = json.load(ss)
        return JsonResponse(data["factories"][int(factory_id)]["factory"]["chart_data"], safe=False)


def production_actual(request, factory_id):
    with open("data/seed_factory_data.json") as ss:
        data = json.load(ss)
        return JsonResponse(
            data["factories"][int(factory_id)]["factory"]["chart_data"]["sprocket_production_actual"],
            safe=False
        )

def production_goal(request, factory_id):
    with open("data/seed_factory_data.json") as ss:
        data = json.load(ss)
        return JsonResponse(
            data["factories"][int(factory_id)]["factory"]["chart_data"]["sprocket_production_goal"],
            safe=False
        )
    

def time(request, factory_id):
    with open("data/seed_factory_data.json") as ss:
        data = json.load(ss)
        return JsonResponse(
            data["factories"][int(factory_id)]["factory"]["chart_data"]["time"],
            safe=False
        )


def sprockets(request):
    with open("data/seed_sprocket_types.json") as ss:
        data = json.load(ss)
        data["count"] = len(data["sprockets"])
        return JsonResponse(data, safe=False)


def sprocket(request, sprocket_id):
    with open("data/seed_sprocket_types.json") as ss:
        data = json.load(ss)
        return JsonResponse(data["sprockets"][int(sprocket_id)], safe=False)


@require_http_methods(['POST'])
def sprocket_create(request, **kwargs):
    new_sprocket_pkg = {
      "teeth": kwargs.pop("teeth"),
      "pitch_diameter": kwargs.pop("pitch_diameter"),
      "outside_diameter": kwargs.pop("outside_diameter"),
      "pitch": kwargs.pop("pitch")
    }

    with open("data/seed_sprocket_types.json", "rw") as ss:
        data = json.load(ss)
        data["sprockets"].append(new_sprocket_pkg)
        msg = {
            "message": "",
            "status_code": None
        }
        try:
            ss.write(json.dumps(data))
            msg["message"] = "success"
            msg["status_code"] = 200
        except Exception as e:
            msg["message"] = "error"
            msg["error"] = e
            msg["status_code"] = 400

        return JsonResponse(msg)


def sprocket_update(request):
    pass