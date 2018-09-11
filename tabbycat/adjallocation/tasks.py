from __future__ import absolute_import, unicode_literals

import logging

from celery.decorators import task

logger = logging.getLogger(__name__)


# Test task
@task(name="debug_task")
def debug_task():
    logger.info("CELERY SAYS HI")
