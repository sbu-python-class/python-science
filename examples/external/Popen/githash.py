import subprocess

prog = ["git", "rev-parse", "--abbrev-ref", "HEAD"]
p0 = subprocess.Popen(prog, stdout=subprocess.PIPE,
                      stderr=subprocess.STDOUT)
stdout0, stderr0 = p0.communicate()

print "stdout: {}".format(stdout0)
print "stderr: {}".format(stderr0)

