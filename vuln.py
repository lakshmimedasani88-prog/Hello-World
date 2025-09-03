import subprocess

# Hardcoded secret
API_KEY = "superSecret123"

# Dangerous eval
eval("print('Eval executed!')")

# Insecure subprocess
subprocess.call("ls -la", shell=True)
