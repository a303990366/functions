from datetime import datetime

class timePackage():
    def stamp2datetime(self,timestamp):
        dt_object = datetime.fromtimestamp(timestamp)
        return dt_object
    #datetime.datetime to str
    def datetime2str(self,time):
        date_time = time.strftime("%Y-%m-%d")
        return date_time
    #datetime.datetime to timestamp
    def datetime2stamp(self,date):
        return date.timestamp()#當地伺服時間
    #str to datetime.datetime
    def str2datetime(self,string,format_time='%Y-%m-%d'):
        return datetime.strptime(string,format_time)
    #stmamp to string
    def stamp2str(self,stamp):
        stamp=self.stamp2datetime(stamp)
        string=self.datetime2str(stamp)
        return string
    #string to timestamp
    def str2stamp(self,string):
        string=self.str2datetime(string)
        return self.datetime2stamp(string)
    #get three format of time's dict
    def all_items(self,source):
        items=dict()
        self.type=type(source)
        if self.type==datetime:
            items['datetime']=source
            items['timestamp']=self.datetime2stamp(source)
            items['string']=self.datetime2str(source)
        elif self.type==str:
            items['string']=source
            items['datetime']=self.str2datetime(source)
            items['timestamp']=self.str2stamp(source)
        elif self.type==float or self.type==int:
            items['timestamp']=source
            items['datetime']=self.stamp2datetime(source)
            items['string']=self.stamp2str(source)
        return items
