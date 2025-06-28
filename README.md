[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
# Quantdash
**QuantDash** is a lightweight Python framework for building real-time, data-driven dashboards for traders, analysts, and financial engineers.

**WIP** 🌱 *Please call back soon...*

```python
from quantdash import QuantDash

qd = QuantDash()
qd.run()
```

## API Endpoints

| Method | Path      | Description       | Response Example |
|--------|-----------|-------------------|------------------|
| GET    | `/health` | Health check with version | `{ "status": "OK", "version": "0.0" }` |