"""
GitHub Trending Repo Scraper

Scrapes trending repos from https://github.com/trending and saves them
to a CSV file. Runs once or on a repeating schedule.

"""

from __future__ import annotations
import argparse, csv, sys, time
from datetime import datetime
from pathlib import Path
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://github.com/trending"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
OUTPUT_DIR = Path("scraped_data")
OUTPUT_DIR.mkdir(exist_ok=True)


def fetch_page(language: str | None = None) -> str:
    """Download the trending page HTML, optionally filtered by language."""
    url = f"{BASE_URL}/{language}" if language else BASE_URL
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.text


def parse_trending(html: str) -> list[dict]:
    """Extract repo name, description, language, and stars from the page."""
    soup = BeautifulSoup(html, "html.parser")
    repos = []
    for row in soup.select("article.Box-row"):
        link_tag = row.select_one("h2.lh-condensed a")
        if not link_tag:
            continue
        repo_path = link_tag.get("href", "").strip("/")
        desc_tag = row.select_one("p")
        lang_tag = row.select_one("span[itemprop='programmingLanguage']")
        star_tag = row.select_one("a.Link--muted")
        repos.append({
            "repo": repo_path.replace("/", " / "),
            "description": desc_tag.get_text(strip=True) if desc_tag else "",
            "language": lang_tag.get_text(strip=True) if lang_tag else "N/A",
            "stars": star_tag.get_text(strip=True) if star_tag else "0",
            "url": f"https://github.com/{repo_path}",
        })
    return repos


def save_to_csv(repos: list[dict]) -> Path:
    """Save scraped repos to a timestamped CSV file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = OUTPUT_DIR / f"github_trending_{timestamp}.csv"
    fieldnames = ["repo", "description", "language", "stars", "url"]
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(repos)
    return filepath


def scrape_once(language: str | None = None) -> None:
    """Run a single scrape: fetch, parse, print, and save."""
    label = f" ({language})" if language else ""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Fetching GitHub Trending{label}...")
    try:
        html = fetch_page(language)
    except requests.RequestException as e:
        print(f"  ERROR: Could not reach GitHub ({e})")
        return
    repos = parse_trending(html)
    if not repos:
        print("  No repos found — the site's HTML structure may have changed.")
        return
    print(f"  Found {len(repos)} trending repos:\n")
    for r in repos:
        print(f"  * {r['stars']:>7}  {r['repo']}  [{r['language']}]")
    print(f"\n  Saved to {save_to_csv(repos)}\n")


def run_scheduled(interval_minutes: int, language: str | None = None) -> None:
    """Run the scraper on a repeating schedule until interrupted (Ctrl+C)."""
    import schedule
    schedule.every(interval_minutes).minutes.do(scrape_once, language=language)
    print(f"Scheduler started: every {interval_minutes} minute(s). Ctrl+C to stop.\n")
    scrape_once(language)
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped.")
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Scrape GitHub Trending repositories.")
    parser.add_argument("--language", type=str, default=None, help="e.g. python, javascript")
    parser.add_argument("--schedule", type=int, metavar="MINUTES", help="Run every N minutes")
    args = parser.parse_args()
    if args.schedule:
        run_scheduled(args.schedule, language=args.language)
    else:
        scrape_once(language=args.language)


if __name__ == "__main__":
    main()