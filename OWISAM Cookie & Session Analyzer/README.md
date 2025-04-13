# Owichan
 Open Wireless Security Assessment Methodology

# 🛡️ Owichan - Herramientas OWISAM para Auditoría Wi-Fi

Owichan es un conjunto de herramientas diseñadas para evaluar la seguridad de redes inalámbricas, basadas en la metodología **OWISAM** (Open Wireless Security Assessment Methodology). Este proyecto busca facilitar auditorías Wi-Fi mediante la automatización de controles y pruebas de seguridad, ayudando a identificar vulnerabilidades en infraestructuras inalámbricas.

# OWISAM Cookie & Session Analyzer

Herramienta de análisis automático de cookies y gestión de sesiones basada en la metodología OWISAM.

## Descripción

Este proyecto permite auditar de forma automatizada las cookies y las sesiones de un sitio web, detectando posibles fallos de seguridad relacionados con su configuración y tratamiento.

Se centra específicamente en las categorías OWISAM-COO (Cookies) y OWISAM-SES (Sesiones).

---

## Características principales

- Detección y análisis de cookies:
  - Nombre, valor y dominio.
  - Flags de seguridad: `Secure`, `HttpOnly`, `SameSite`.
  - Expiración y persistencia.
  - Detección de cookies de terceros.

- Análisis de sesiones:
  - Identificación de cookies de sesión.
  - Predicción o estructura del ID de sesión.
  - Rotación de sesión tras login.
  - Duración y expiración de la sesión.
  - Existencia de tokens CSRF.

- Generación de informe en:
  - HTML
  - PDF (opcional)

---

## Pruebas OWISAM implementadas

| Código | Descripción | Categoría |
|--------|-------------|------------|
| OWISAM-COO-001 | Detección de cookies inseguras | Cookies |
| OWISAM-COO-002 | Ausencia de flag HttpOnly | Cookies |
| OWISAM-COO-003 | Ausencia de flag Secure en HTTPS | Cookies |
| OWISAM-COO-004 | SameSite mal configurado o ausente | Cookies |
| OWISAM-SES-001 | ID de sesión predecible o débil | Sesiones |
| OWISAM-SES-002 | No rotación de ID de sesión tras login | Sesiones |
| OWISAM-SES-003 | Ausencia de expiración de sesión | Sesiones |
| OWISAM-SES-004 | Formularios críticos sin token CSRF | Sesiones |

---

## Instalación

Pendiente