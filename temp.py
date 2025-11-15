

import sys
import logging

log = logging.Logger("Alerta")

info = {
    "temperatura": None,
    "umidade": None
}

keys = info.keys()

for  key in keys:
    try:
        info[key] = float(input(f"Qual a {key}?").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)


temp = info["temperatura"]
umi = info ["umidade"]



if temp > 45:
    print("Alerta!!! Temperatura extrema")
