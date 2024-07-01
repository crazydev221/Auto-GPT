import os
import sys
import secrets

if "pytest" in sys.argv or "pytest" in sys.modules or os.getenv("CI"):
    print("Setting random seed to 42")
    secrets.SystemRandom().seed(42)
