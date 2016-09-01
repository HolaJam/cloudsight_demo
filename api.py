# coding=utf8
import cloudsight
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class demo(object):
    def __init__(self,url,key):
        self.url = url
        self.key = key
    def conn(self):
        auth = cloudsight.SimpleAuth(key = self.key)
        api = cloudsight.API(auth = auth)
        response = api.remote_image_request(self.url, {
            'image_request[locale]': 'zh-CN',
            'image_request[language]': 'zh-CN',
        })
        return api.image_response(response['token'])
    def analyse_status(self):
        status = self.conn()
        if status['status'] == cloudsight.STATUS_NOT_COMPLETED:
            print 'retry once again'
        elif status['status'] == cloudsight.STATUS_NOT_FOUND:
            print 'url doesn\'t match image'
        elif status['status'] == cloudsight.STATUS_SKIPPED:
            print 'image cann\'t be recognized'
        elif status['status'] == cloudsight.STATUS_TIMEOUT:
            print 'time out'
        else:
            pass


if __name__ == '__main__':
    try:
        url = sys.argv[0]
        key = sys.argv[1]
        run_demo = demo()
        run_demo.analyse_status(url, key)
        pass
    except Exception, e:
        print 'Demo: python *.py url key'
        print 'Error: %s',str(e)
        pass




