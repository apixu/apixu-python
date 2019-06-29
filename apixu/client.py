import datetime
import requests

API_URL = 'http://api.apixu.com'
API_VERSION = '1'
FORMAT = 'json'
HTTP_TIMEOUT = 20
DOC_WEATHER_CONDITIONS_URL = 'https://www.apixu.com/doc/Apixu_weather_conditions.%s'


class ApixuException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        message = 'Error code %s: "%s"' % (code, message)
        super(ApixuException, self).__init__(message)


class ApixuClient:
    def __init__(self, api_key=None, api_url=API_URL, lang=None):
        self.api_key = api_key
        self.api_url = api_url.rstrip('/')
        self.lang = lang

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

    def conditions(self):
        url = DOC_WEATHER_CONDITIONS_URL % FORMAT

        return self._get(url)

    def current(self, q=None):
        url = self._url('current')
        args = {}
        if q:
            args['q'] = q
        if self.lang:
            args['lang'] = self.lang

        return self._get(url, args)

    def search(self, q=None):
        url = self._url('search')
        args = {}
        if q:
            args['q'] = q

        return self._get(url, args)

    def forecast(self, q=None, days=None, hour=None):
        url = self._url('forecast')
        args = {}
        if q:
            args['q'] = q
        if days:
            args['days'] = days
        if hour:
            args['hour'] = hour
        if self.lang:
            args['lang'] = self.lang

        return self._get(url, args)

    def history(self, q=None, since=None, until=None):
        url = self._url('history')
        args = {}
        if q:
            args['q'] = q
        if since:
            if not isinstance(since, datetime.date):
                raise ApixuException(message='"since" must be a date', code=0)
            args['dt'] = since.strftime('%Y-%m-%d')
        if until:
            if not isinstance(until, datetime.date):
                raise ApixuException(message='"until" must be a date', code=0)
            args['end_dt'] = until.strftime('%Y-%m-%d')
        if self.lang:
            args['lang'] = self.lang

        return self._get(url, args)
