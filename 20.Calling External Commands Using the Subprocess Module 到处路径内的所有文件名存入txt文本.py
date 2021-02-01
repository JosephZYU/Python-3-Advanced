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


# Work with context manager ⭐️ 200
"""
with open('20.Ref - output.txt', 'w') as f:
    p1 = subprocess.run(['ls', '-la'], stdout=f, text=True)
"""

# Working with dir NOT existed
p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True)

print()
