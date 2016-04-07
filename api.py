# coding=utf8
import cloudsight

def api(url):
    auth = cloudsight.SimpleAuth('CYPM46vO1M7oMZ2OUq-yXw')
    api = cloudsight.API(auth)

    response = api.remote_image_request(url, {
        'image_request[locale]': 'zh-CN',
        'image_request[language]': 'zh-CN',
    })

    status = api.image_response(response['token'])
    if status['status'] == cloudsight.STATUS_NOT_COMPLETED:
        print 'retry once again'
    elif status['status'] == cloudsight.STATUS_NOT_FOUND:
        print 'url doesn\'t match image'
    elif status['status'] == cloudsight.STATUS_SKIPPED:
        print 'image cann\'t be recognized'
    elif status['status'] == cloudsight.STATUS_TIMEOUT:
        print 'time out'
    elif status['status'] == cloudsight.STATUS_COMPLETED:
        status = api.wait(response['token'], timeout=30)
        print status[u'name']
    else:
        pass

try:
    url = ''
    api(url)
except Exception, e:
    print 'Usage: cloudsightapi.py http://pic_url.com/test.jpg'
    print 'Error: %s' % str(e)
    pass