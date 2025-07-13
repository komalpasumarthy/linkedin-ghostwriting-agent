import json
import os
from typing import Dict, List, Union, Optional, Dict
import pandas as pd


def get_user_tone_from_url(linkedin_url: str) -> Dict[str, Optional[str]]:
    """
    Retrieves the user's tone profile from data.json based on their LinkedIn URL.

    If tone exists, return it. Otherwise:
    - Load the associated CSV file from the stored 'path'
    - Filter rows with non-empty and non-dash '-' descriptions
    - Sample 3 valid posts and return their combined descriptions as a corpus

    Args:
        linkedin_url (str): The LinkedIn profile URL of the user should be a perfect Linkedin URL in this format: https://www.linkedin.com/in/username.

    Returns:
        Dict[str, Optional[str]]: 
            - Cached tone if available
            - If missing: {"text_corpus": "<combined sample text>"}
            - On error: {"error": "<error message>"}
    """
    data_file = "multi_tool_agent\data.json"

    if not os.path.exists(data_file):
        return {"error": f"{data_file} not found."}

    try:
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        return {"error": f"Failed to parse {data_file}."}

    profile = next((item for item in data if item.get("linkedin_url") == linkedin_url), None)
    if not profile:
        return {"error": f"No profile found for URL: {linkedin_url}"}

    if profile.get("person_tone"):
        return profile["person_tone"]

    path = profile.get("path")
    if not path or not os.path.exists(path):
        return {"error": f"CSV path invalid or not found for profile: {linkedin_url}"}

    try:
        df = pd.read_csv(path)
        if "Media Description" not in df.columns:
            return {"error": "CSV must contain a 'Media Description' column."}

        # Filter valid descriptions
        valid_posts = df[df["Media Description"].notna() & (df["Media Description"].str.strip() != "-")]
        if valid_posts.empty:
            return {"error": "No valid post descriptions found in CSV."}

        sampled_posts = valid_posts.sample(n=min(3, len(valid_posts)))
        text_corpus = "\n\n".join(sampled_posts["Media Description"].tolist())
        return {"text_corpus": text_corpus}
    except Exception as e:
        return {"error": f"Failed to process CSV: {str(e)}"}




def update_user_tone(
    linkedin_url: str,
    tone: str,
    structure: str,
    themes: List[str]
) -> Dict[str, str]:
    """
    Updates the user’s tone information in data.json for the given LinkedIn URL.

    Args:
        linkedin_url (str): The LinkedIn profile URL of the user should be a perfect Linkedin URL in this format: https://www.linkedin.com/in/username.
        tone (str): The predicted writing tone (e.g., 'casual', 'inspirational').
        structure (str): The typical structure of their posts (e.g., 'story-driven').
        themes (List[str] or comma-separated str): Key themes/topics the user writes about.

    Returns:
        Dict[str, str]: Confirmation or error message.
    """
    data_file = "multi_tool_agent\data.json"

    if not os.path.exists(data_file):
        return {"error": f"{data_file} not found."}

    try:
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        return {"error": "Failed to parse data.json."}

    profile_found = False
    for profile in data:
        if profile.get("linkedin_url") == linkedin_url:
            profile_found = True
            # Normalize themes input
            if isinstance(themes, str):
                themes = [t.strip() for t in themes.split(",") if t.strip()]
            profile["person_tone"] = {
                "tone": tone,
                "structure": structure,
                "themes": themes
            }
            break

    if not profile_found:
        return {"error": f"No profile found for LinkedIn URL: {linkedin_url}"}

    try:
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        return {"error": f"Failed to write to data.json: {str(e)}"}

    return {"success": f"Tone updated for {linkedin_url}"}
