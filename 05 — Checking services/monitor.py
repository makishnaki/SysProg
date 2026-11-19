import json
import socket
import time
import urllib.error
import urllib.request
from datetime import datetime


def check_service(service: dict) -> tuple[str, str]:
    url = service["url"]
    timeout = service.get("timeout_seconds", 1)

    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            code = response.getcode()
            body = response.read().decode("utf-8", errors="ignore").strip().lower()
            if code == 200:
                return "up", f"http {code} ({body})"
            return "error", f"http {code} ({body})"

    except urllib.error.HTTPError as e:
        return "http_error", f"http {e.code} ({str(e.reason).lower()})"

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            return "timeout", f"превышен таймаут ({timeout} сек)"
        if isinstance(e.reason, ConnectionRefusedError):
            return "down", "порт недоступен (соединение отклонено)"
        return "down", f"ошибка сети: {str(e.reason).lower()}"

    except (socket.timeout, TimeoutError):
        return "timeout", f"превышен таймаут ({timeout} сек)"


def run_checks(config_path: str = "services.json", log_path: str = "monitor.log"):
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    services = data.get("services", [])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [f"--- проверка от {timestamp} ---"]
    for svc in services:
        name = svc["name"].lower()
        url = svc["url"].lower()
        status, details = check_service(svc)
        lines.append(f"[{timestamp}] {name:<10} | {status:<10} | {url} -> {details}")

    report = "\n".join(lines)
    print(report)

    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(report + "\n\n")


if __name__ == "__main__":
    try:
        while True:
            run_checks()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nмониторинг остановлен.")