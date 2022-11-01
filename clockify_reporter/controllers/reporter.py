import requests
import json
import os
from datetime import datetime, timedelta
from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
clockify_api_key = {'x-api-key': api_key}


def get_tasks_report(request):
    user_info_response = requests.get('https://api.clockify.me/api/v1/user', headers=clockify_api_key)
    user_info_json = json.loads(user_info_response.content)
    user_id, workspace_id = user_info_json["id"], user_info_json["activeWorkspace"]

    response = requests.get(f'https://api.clockify.me/api/v1/workspaces/{workspace_id}/user/{user_id}'
                            f'/time-entries', headers=clockify_api_key)
    json_response = json.loads(response.text)
    entity_array = []
    for num, entity in enumerate(json_response):
        project_id = entity['projectId']
        description = entity['description']
        start = entity['timeInterval']['start']
        end = entity['timeInterval']['end']
        duration = entity['timeInterval']['duration']
        entity_array.append({"project_id": project_id, "description": description, "start": start, "end": end,
                             "duration": duration})
        print("===========================================")
        print("Project ID: ", project_id)
        print("Description: ", description)
        print("Start at: ", start)
        print("Ends at: ", end)
        print("Duration: ", duration)

    return render(request, 'main/tasks_report.html', {"entity": entity_array})


def get_summary_report(request):
    user_info_response = requests.get('https://api.clockify.me/api/v1/user', headers=clockify_api_key)
    user_info_json = json.loads(user_info_response.content)
    user_id, workspace_id = user_info_json["id"], user_info_json["activeWorkspace"]
    current_time = datetime.now().isoformat()
    body = {
        "dateRangeStart": "2022-09-01T00:00:00.000",
        "dateRangeEnd": current_time,
        "summaryFilter": {
            "groups": [
                "DATE",
                "TASK",
                "TIMEENTRY"
            ],
        },
        "exportType": "JSON"
    }

    response = requests.post(f'https://reports.api.clockify.me/v1/workspaces/{workspace_id}/reports/summary',
                             headers=clockify_api_key, json=body)
    json_response = json.loads(response.text)
    group_array = []
    total_time = (str(timedelta(seconds=json_response['totals'][0]['totalTime'])))
    print("Total time", total_time)
    for group in json_response['groupOne']:
        date = group['name']
        duration = (str(timedelta(seconds=group['duration'])))
        group_array.append({"date": date, "duration": duration})
        print("===========================================")
        print("Date: ", date)
        print("Duration: ", duration)
    return render(request, 'main/summary_report.html', {"entity": {"total_time": total_time,
                                                                   "group_data": group_array}})
