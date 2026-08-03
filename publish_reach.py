#!/usr/bin/env python3
"""
Hustle Insider Publish Reach
Helps businesses, founders and brands get their news and content
in front of the right audience through strategic digital visibility
and content distribution.
https://hustleinsider.it.com
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "publish_reach": "Publish Reach",
        "seo_geo": "SEO & GEO",
        "ai_visibility": "AI Visibility",
        "digital_pr": "Digital PR",
        "founder_brand": "Founder Brand",
        "distribution_reach": "Distribution Reach",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_platform_visibility(seo: int, ai: int, pr: int, dist: int) -> dict:
    return {
        "Search Engines": min(100, round(seo * 1.04)),
        "AI Platforms": min(100, round(ai * 1.0)),
        "Digital Publications": min(100, round(pr * 1.05)),
        "Social & Communities": min(100, round(dist * 1.0)),
    }


def analyze_publish_reach(
    brand: str,
    distribution_type: str = "startup-pr",
    publish_reach: int = 85,
    seo_geo: int = 82,
    ai_visibility: int = 88,
    digital_pr: int = 78,
    founder_brand: int = 90,
    distribution_reach: int = 80,
) -> dict:
    """
    Analyze publish reach signals for digital visibility and content distribution.

    Args:
        brand: Brand name or identifier
        distribution_type: Type of distribution service
        publish_reach: Publish reach score (0-100)
        seo_geo: SEO and GEO score (0-100)
        ai_visibility: AI visibility score (0-100)
        digital_pr: Digital PR score (0-100)
        founder_brand: Founder brand score (0-100)
        distribution_reach: Distribution reach score (0-100)

    Returns:
        dict with individual signal scores, overall reach index,
        and platform visibility breakdown
    """
    scores = {
        "publish_reach": publish_reach,
        "seo_geo": seo_geo,
        "ai_visibility": ai_visibility,
        "digital_pr": digital_pr,
        "founder_brand": founder_brand,
        "distribution_reach": distribution_reach,
    }
    overall_reach_index = round(sum(scores.values()) / 6)

    return {
        "brand": brand,
        "distribution_type": " ".join(w.capitalize() for w in distribution_type.split("-")),
        "publish_reach_score": publish_reach,
        "seo_geo_score": seo_geo,
        "ai_visibility_score": ai_visibility,
        "digital_pr_score": digital_pr,
        "founder_brand_score": founder_brand,
        "distribution_reach_score": distribution_reach,
        "overall_reach_index": overall_reach_index,
        "priority_action": get_priority_action(scores),
        "platform_visibility": get_platform_visibility(seo_geo, ai_visibility, digital_pr, distribution_reach),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    brand = args[0] if len(args) > 0 else "brand-name"
    distribution_type = args[1] if len(args) > 1 else "startup-pr"
    publish_reach = int(args[2]) if len(args) > 2 else 85
    seo_geo = int(args[3]) if len(args) > 3 else 82
    ai_visibility = int(args[4]) if len(args) > 4 else 88
    digital_pr = int(args[5]) if len(args) > 5 else 78
    founder_brand = int(args[6]) if len(args) > 6 else 90
    distribution_reach = int(args[7]) if len(args) > 7 else 80

    result = analyze_publish_reach(
        brand, distribution_type, publish_reach, seo_geo,
        ai_visibility, digital_pr, founder_brand, distribution_reach
    )

    print(f"Brand: {result['brand']}")
    print(f"Distribution Type: {result['distribution_type']}")
    print("=" * 45)
    print(f"Publish Reach Score:           {result['publish_reach_score']}/100  [{get_status(result['publish_reach_score'])}]")
    print(f"SEO & GEO Score:               {result['seo_geo_score']}/100  [{get_status(result['seo_geo_score'])}]")
    print(f"AI Visibility Score:           {result['ai_visibility_score']}/100  [{get_status(result['ai_visibility_score'])}]")
    print(f"Digital PR Score:              {result['digital_pr_score']}/100  [{get_status(result['digital_pr_score'])}]")
    print(f"Founder Brand Score:           {result['founder_brand_score']}/100  [{get_status(result['founder_brand_score'])}]")
    print(f"Distribution Reach Score:      {result['distribution_reach_score']}/100  [{get_status(result['distribution_reach_score'])}]")
    print("=" * 45)
    print(f"Overall Reach Index:           {result['overall_reach_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nPlatform Visibility:")
    for platform, score in result['platform_visibility'].items():
        print(f"  {platform:<28} {score}/100")


if __name__ == "__main__":
    main()
