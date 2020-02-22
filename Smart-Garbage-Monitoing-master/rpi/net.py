import commands
cmd = 'iwconfig | grep "Link Quality"'
output = commands.getoutput(cmd)
#print(output)
link=output.split("=")
signal=link[2].split(" ")
signal=signal[0]
print(signal)
link=link[1].split("/")
#link=link[1].split(" ")
link=link[0]
print(link)

