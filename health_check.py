#!/usr/bin/env python3

import shutil
import psutil
import os

path = os.cwd()
disk_usage_stats = shutil.disk_usage(path)

print("Total Disk Utilisation : {}".format(disk_usage_stats.free/disk_usage_stats.total))

