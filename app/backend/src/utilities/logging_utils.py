import json
import logging
from datetime import datetime, timezone

class JsonFormatter(logging.Formatter):

    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, tz=timezone.utc)
        return dt.strftime(datefmt or self.default_time_format)
    
    def format(self, record):
        log_record = {
            'time': self.formatTime(record, self.datefmt),
            'level': record.levelname,        
            'message': record.getMessage(),   
        }

        return json.dumps(log_record)