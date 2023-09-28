import time
seconds = time.time()
notation_seconds = "{:.2e}".format(seconds)
print("Seconds since January 1, 1970:", seconds, "or ", end="")
print(notation_seconds, "in scientific notation")
local_time = time.localtime(seconds)
Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
Months.extend(["Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
print(Months[local_time.tm_mon - 1], local_time.tm_mday, local_time.tm_year)
