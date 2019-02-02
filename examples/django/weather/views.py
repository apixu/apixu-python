from rest_framework.response import Response
from rest_framework.views import APIView


class CurrentWeatherView(APIView):
    apixu = None

    def get(self, request):
        query = request.query_params.get('q', None)
        if query is None or query.strip() == '':
            raise ValueError('Empty or missing query.')

        return Response(self.apixu.current(q=query))
