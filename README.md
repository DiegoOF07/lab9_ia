# Laboratorio 9 - IA

## 📌 Descripción

Este proyecto implementa un modelo probabilístico basado en una **Red Bayesiana** para el problema clásico de **Robo–Terremoto–Alarma**, con el objetivo de demostrar el fenómeno de *Explain Away* mediante inferencia probabilística.

---

## 🧩 Modelo Utilizado

Variables:

* **B**: Robo (Burglary) ∈ {0,1}
* **E**: Terremoto (Earthquake) ∈ {0,1}
* **A**: Alarma (Alarm) ∈ {0,1}

Parámetros:

* (P(B=1) = 0.01)
* (P(E=1) = 0.01)
* (A = B \lor E) (modelo determinístico)
  
---

## 🧠 Conclusión (Explain Away)

Al observar únicamente la alarma, la probabilidad de robo es alta debido a la incertidumbre entre múltiples causas posibles. No obstante, al incorporar evidencia adicional (terremoto), la probabilidad de robo disminuye significativamente, ya que la nueva evidencia explica la activación de la alarma.

---

## ▶️ Ejecución

```bash
python main.py
```

---
