# -*- coding: utf-8 -*-
"""Log IRC events

This module will handle logging IRC events (e.g., JOIN, PART).  This is really
just for debugging purposes.
"""
from __future__ import absolute_import, unicode_literals

from sopel import logger, module

# List functions/callables to export
__all__ = [
    'log_join_part',
]

# Get logger
logger = logger.get_logger(__name__)


@module.event('JOIN', 'PART')
@module.rule(r'.*')
@module.priority('low')
def log_join_part(bot, trigger):
    # Only trigger for important people
    if any([
        trigger.owner,
        trigger.admin,
        trigger.nick == bot.nick,
    ]):
        logger.debug('{place} {event} {nick}'
                     .format(nick=trigger.nick, event=trigger.event,
                             place=trigger.sender)
                     )