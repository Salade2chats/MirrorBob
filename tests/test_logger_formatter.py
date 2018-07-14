import re
from logging import LogRecord

from bob.services.logger.formatter import Formatter


def test_format():
    formatter = Formatter()
    log_record = LogRecord(
        name='fake_name',
        level=10,
        msg='fake_message',
        pathname=None,
        lineno=None,
        args=None,
        exc_info=None
    )
    log = formatter.format(log_record)
    regexp = re.compile(
        r'^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+ - '
        r'fake_name - DEBUG - fake_message$')
    assert re.search(regexp, log)
