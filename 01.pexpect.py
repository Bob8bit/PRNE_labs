import pexpect

def get_rtable(ip, name):
  devname = name+">"
  wait = "-More-"
  output = ""
  session = pexpect.spawn("telnet "+ip, timeout = 15)
  result = session.expect(["Username", pexpect.TIMEOUT])
  if result != 0:
    print("connection Error!")
    return(-1)
  session.sendline("cisco")
  result = session.expect(["Password", pexpect.TIMEOUT])
  if result != 0:
    print("wrong username!")
    return(-1)
  session.sendline("cisco")
  result = session.expect([devname, pexpect.TIMEOUT])
  if result != 0:
    print("Password mismatch!")
    return(-1)
  session.sendline("show ip route")
  while True:
    result = session.expect([devname,wait,pexpect.TIMEOUT])
#    print("Loop")
#    print(session.before)
    if result == 0:
       output = output + session.before
#       print("LOOP\n"+output)
       return output
    elif result == 1:
       output = output + session.before
 #      print("MORE\n"+output)
       session.sendline(" ")
       continue
    elif result == 2:
       print("You got Timeout")
       return(-1)
    else:
       break
  print("How did i get here?")

def count_routes(file):
  pattern = re.compile()


#main
output = get_rtable("10.30.30.2", "r2")
if output == -1:
  print("Session Terminated with an error")
  exit(-1)
print(output)
