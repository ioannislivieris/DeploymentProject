import influxdb
from   influxdb import InfluxDBClient
from   influxdb import DataFrameClient


class InfluxDBClient:

    def __init__(self, host = None, port = None, username = None, pwd = None, db = None):
        self.host     = host
        self.port     = port
        self.username = username
        self.pwd      = pwd
        self.db       = db
        
    def initClient(self):
        self.client = InfluxDBClient(self.host, self.port, self.username,  self.pwd, self.db)
        
    def removeHTTPSession(self):
        self.client.close()
        
    def constractMeasurementRecord(self, measurement=None, tags=None, values=None, time=None):
        response = {}
        response['measurement'] = measurement
        response['tags'] = {}
        
        for key, value in tags.items():
            response['tags'][key] = value
        response['time']   = time
        response['fields'] = {}
        
        for key, value in values.items():
            response['fields'][key]=value
        return response
    
    def create_database(self, dbname=None):
        self.client.create_database( dbname )
        
    def writePointsToDb(self, measurement=None):
        self.initClient()
        self.client.write_points(measurement, time_precision='ms')
        self.removeHTTPSession()
        
        
        
class InfluxDataframeDBClient:
    def __init__(self, host = None, port = None, username = None, pwd = None, db = None):
        self.host     = host
        self.port     = port
        self.username = username
        self.pwd      = pwd
        self.db       = db
        
    def initClient(self):
        self.client = DataFrameClient(self.host, self.port, self.username, self.pwd, self.db)


