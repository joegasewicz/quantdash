import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(name)s] %(message)s",
)

logger = logging.getLogger("quantdash")
