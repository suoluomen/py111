import psutil
print(psutil.cpu_count()) # CPU逻辑数量
print(psutil.cpu_stats)
print(psutil.cpu_times())
print(psutil.net_if_stats())