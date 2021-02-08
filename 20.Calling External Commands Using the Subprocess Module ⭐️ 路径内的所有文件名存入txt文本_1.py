import subprocess

# subprocess.run('ls', shell=True)
# subprocess.run('ls -la', shell=True)
# subprocess.run(['ls', '-la'], shell=True)

p1 = subprocess.run(['ls', '-la'], capture_output=True)

# print(p1.args)
# print(p1.returncode)  # 0 -> We run it successfully -> we need 0 code

print(p1.stdout.decode)
print()

p1 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)

print(p1.stdout)
print()


# Work with context manager ⭐️
"""
with open('20.Ref - output.txt', 'w') as f:
    p1 = subprocess.run(['ls', '-la'], stdout=f, text=True)
"""

# Working with dir NOT existed
p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True)
print(p1.stderr)


# Working with dir NOT existed - continued
p1 = subprocess.run(['ls', '-la', 'dne'],
                    stderr=subprocess.DEVNULL)
print(p1.stderr)


# cat command to print out content from file ⭐️

p1 = subprocess.run(['cat', 'require.txt'], capture_output=True, text=True)
print(p1.stdout)

p2 = subprocess.run(['grep', '-n', 'pylint'],
                    capture_output=True, text=True, input=p1.stdout)
print(p2.stdout)

# 13: pylint==2.6.0 -> on line 13 on that output


# PUT IT ALL TOGETHER! ⭐️⭐️⭐️

p3 = subprocess.run('cat require.txt | grep -n pylint',
                    capture_output=True, text=True, shell=True)

print(p3.stdout)
