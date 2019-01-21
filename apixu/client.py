import requests, datetime

API_URL='http://api.apixu.com'
API_VERSION='1'
FORMAT='json'
HTTP_TIMEOUT=20


class ApixuException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        message = 'Error code %s: "%s"' % (code, message)
        super(ApixuException, self).__init__(message)


class ApixuClient:
    def __init__(self, api_key=None, api_url=API_URL):
        self.api_key = api_key
        self.api_url = api_url.rstrip('/')

    def _get(self, url, args=None):
        new_args = {}
        if self.api_key:
            new_args['key'] = self.api_key
        new_args.update(args or {})
        response = requests.get(url, params=new_args, timeout=HTTP_TIMEOUT)
        res = response.json()
        if 'error' in res:
            err_msg = res['error'].get('message')
            err_code = res['error'].get('code')
            raise ApixuException(message=err_msg, code=err_code)

        return res

    def _url(self, method):
        return '%s/v%s/%s.%s' % (self.api_url, API_VERSION, method, FORMAT)

    def getCurrentWeather(self, q=None):
        url = self._url('current')
        args = {}
        if q:
            args['q'] = q

        return self._get(url, args)

    def search(self, q=None):
        url = self._url('search')
        args = {}
        if q:
            args['q'] = q

        return self._get(url, args)

    def getForecastWeather(self, q=None, days=None):
        url = self._url('forecast')
        args = {}
        if q:
            args['q'] = q
        if days:
            args['days'] = days

        return self._get(url, args)

    def getHistoryWeather(self, q=None, since=None):
        url = self._url('history')
        args = {}
        if q:
            args['q'] = q
        if since:
            if not isinstance(since, datetime.date):
                raise ApixuException(message='"since" must be a date', code=0)
            args['dt'] = since.strftime('%Y-%m-%d')

        return self._get(url, args)
