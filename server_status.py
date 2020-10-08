# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import socket
import sys

import psutil


def python_version():
    """
    Return system version info
    """
    sys.version_info


def ip_addresses():
    hostname = socket.gethostname()

    addresses = socket.getaddrinfo(hostname, None)
    address_info = []
    for address in addresses:
        address_info.append(address[0].name, address[4][0])
    return address_info


def cpu_load():
    return psutil.cpu_percent()


def ram_available():
    """
    Show available ram
    """
    psutil.virtual_memory().available


def ac_connected():
    """
    Show whether AC Power is connected.
    """
    psutil.sensors_battery().power_plugged
