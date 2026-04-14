def evaluate_safety(person_count: int):
    alerts = []

    if person_count == 0:
        alerts.append("Şantiyede çalışan tespit edilmedi.")
    elif person_count > 0:
        alerts.append(f"{person_count} çalışan tespit edildi.")
        alerts.append("KKE analizi bir sonraki sürümde eklenecek.")
        alerts.append("Risk izleme sistemi aktif.")

    risk_level = "Düşük"

    if person_count >= 3:
        risk_level = "Orta"
    if person_count >= 6:
        risk_level = "Yüksek"

    return {
        "risk_level": risk_level,
        "alerts": alerts
    }