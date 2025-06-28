[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
# Quantdash
**QuantDash** is a lightweight Python framework for building real-time, data-driven dashboards for traders, analysts, and financial engineers.

**WIP** 🌱 *Please call back soon...*

```python
chart1 = Chart(
    data={},
    type="bar",
)

card1 = Card(
    title="Chart #1",
    chart=chart1,
)

page1 = Page(
    route="/",
    cards=[card1]
)

qd = QuantDash(pages=[page1])
qd.run()
```