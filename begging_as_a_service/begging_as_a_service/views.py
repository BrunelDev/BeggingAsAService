import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import random



class Begging(APIView):
    def get(self, request):
        lang = self.request.GET.get("lang")
        if(not lang):
            lang = "eng"
            with open("begging-bank.json", "r") as file:
                begging = file.read()
                res = list(json.loads(begging))
                file.close()
        return Response(random.choice(res)["phrase"], status=200)
            
        
            
        