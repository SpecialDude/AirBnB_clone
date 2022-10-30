#!/usr/bin/env python3

"""Initialization of the models package"""

from .engine.file_storage import FileStorage


storage = FileStorage()

storage.reload()