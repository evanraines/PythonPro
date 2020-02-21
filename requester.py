# requests to update tables

class Requester(threading.Thread):
  def __init__(self, url, credentials, payload):
    threading.Thread._init__(self)
    self.url = url
    self.credentials = credentials
    self.payload = payload        
  def run(self):
    # do the post request here
    # you may want to write output (errors and content) to a file
    # rather then just printing it out sometimes when using threads 
    # it gets really messing if you just print everything out