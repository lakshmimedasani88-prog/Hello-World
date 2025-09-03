# Hardcoded secret (Semgrep should flag this)
API_KEY = "12345-SECRET-KEY"

# Insecure eval (Semgrep should flag this)
user_input = "print('Hello from eval')"
eval(user_input)

# Insecure subprocess (Semgrep should flag this)
import subprocess
subprocess.call("ls -la", shell=True)
