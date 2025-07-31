
### `app/__init__.py`


"""
AI Pentest Tool Package

This package initializes the main application and exposes key modules for scanning and analysis.
"""

from .main import run_scan  # Import the main function to run the app
from .scanner import VulnerabilityScanner  # Import the scanner class

# Package version
__version__ = "0.1.0"

__all__ = ['VulnerabilityScanner', 'run_scan']  # Define public API
