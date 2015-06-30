import requests


class ApixuException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        message = 'Error code %s: "%s"' % (code, message)
        super(ApixuException, self).__init__(message)


class ApixuClient:
    def __init__(self, api_key=None, host_url='http://api.apixu.com'):
        self.api_key = api_key
        self.host_url = host_url.rstrip('/')

    def _get(self, url, args=None):
        new_args = {}
        if self.api_key:
            new_args['key'] = self.api_key
        new_args.update(args or {})
        response = requests.get(url, params=new_args)
        json_res = response.json()
        if 'error' in json_res:
            err_msg = json_res['error'].get('message')
            err_code = json_res['error'].get('code')
            raise ApixuException(message=err_msg, code=err_code)

        return json_res

    def getCurrentWeather(self, q=None):
        url = '%s/v1/current.json' % self.host_url
        args = {}
        if q:
            args['q'] = q

        return self._get(url, args)

    def getForecastWeather(self, q=None, days=None):
        url = '%s/v1/forecast.json' % self.host_url
        args = {}
        if q:
            args['q'] = q
        if days:
            args['days'] = days

        return self._get(url, args)
