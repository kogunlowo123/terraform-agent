#!/bin/bash
set -euo pipefail
echo "Setting up Terraform Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
