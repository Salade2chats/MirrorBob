from bob.services.logger import Logger


def test_prepare():
    logger = Logger.prepare('root_name', 10)
    assert logger.getEffectiveLevel() == 10


def test_get():
    Logger.prepare('root_name', 10)
    logger = Logger.get('root_name.sub_name')
    assert logger.getEffectiveLevel() == 10
