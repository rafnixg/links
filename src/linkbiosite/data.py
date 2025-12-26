"""
LinkBioSite Data Loading and Validation Module

This module handles loading and validating site configuration data.
"""

import json
from datetime import date
from pathlib import Path
from typing import Dict, Any, Optional


def load_data(data_file: Optional[Path] = None) -> Dict[str, Any]:
    """
    Load site data from JSON file.

    Args:
        data_file: Path to the data JSON file. If None, looks for 'data.json' in current directory.

    Returns:
        Dictionary containing site configuration and data.

    Raises:
        FileNotFoundError: If data file is not found.
        json.JSONDecodeError: If data file contains invalid JSON.
    """
    if data_file is None:
        data_file = Path.cwd() / "data.json"

    if not data_file.exists():
        raise FileNotFoundError(f"Data file not found: {data_file}")

    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Add dynamic data
    if "footer" in data and "copyright" in data["footer"]:
        data["footer"]["copyright"] = data["footer"]["copyright"].format(
            year=date.today().year
        )

    return data


def validate_data(data: Dict[str, Any]) -> bool:
    """
    Validate the structure of site data.

    Args:
        data: Data dictionary to validate.

    Returns:
        True if validation passes.

    Raises:
        ValueError: If required keys are missing or data structure is invalid.
    """
    required_keys = ["bio", "links", "footer", "analytics", "meta"]
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")

    # Check bio section
    bio_required = ["name", "greeting", "subtitle", "handle", "avatar", "avatar_alt"]
    for key in bio_required:
        if key not in data["bio"]:
            raise ValueError(f"Missing bio key: {key}")

    return True


def save_data(data: Dict[str, Any], data_file: Optional[Path] = None) -> None:
    """
    Save site data to JSON file.

    Args:
        data: Data dictionary to save.
        data_file: Path where to save the data. If None, saves to 'data.json' in current directory.
    """
    if data_file is None:
        data_file = Path.cwd() / "data.json"

    data_file.parent.mkdir(parents=True, exist_ok=True)

    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
