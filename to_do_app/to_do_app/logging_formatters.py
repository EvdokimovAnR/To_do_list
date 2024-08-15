import logging
import json


class CustomJsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'message': record.getMessage(),
            'level': record.levelname,
            'timestamp': self.formatTime(record)
        }
        return json.dumps(log_record, ensure_ascii=False)

