import time

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

websites = [
    "www.youtube.com",
    "youtube.com",
    "www.instagram.com",
    "instagram.com"
]

print("🌐 Website Blocker Running...")

while True:
    hour = time.localtime().tm_hour

    # Block between 9 and 17
    if 9 <= hour < 17:
        print("🔒 Blocking websites...")

        with open(hosts_path, "r+") as file:
            content = file.read()

            for site in websites:
                if site not in content:
                    file.write(f"{redirect} {site}\n")

    else:
        print("🔓 Unblocking websites...")

        with open(hosts_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)

            for line in lines:
                if not any(site in line for site in websites):
                    file.write(line)

            file.truncate()

    time.sleep(10)