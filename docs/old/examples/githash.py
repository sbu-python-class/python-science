import subprocess
import string

# issue the command 'git rev-parse HEAD'
prog = ["git", "rev-parse", "HEAD"]
p0 = subprocess.Popen(prog, stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)
stdout0, stderr0 = p0.communicate()

print "stdout: {}".format(stdout0)
print "stderr: {}".format(stderr0)


