import subprocess

service = input("Enter service name: ")

result = subprocess.run(
    ["systemctl", "is-active", "--quiet", service]
)

if result.returncode == 0:
    print(f"{service} is running.")
else:
    print(f"{service} is not running.")
