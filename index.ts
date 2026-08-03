#!/usr/bin/env node

interface PublishReachInput {
  brand: string;
  distributionType: string;
  publishReach: number;
  seoGeo: number;
  aiVisibility: number;
  digitalPR: number;
  founderBrand: number;
  distributionReach: number;
}

interface PublishReachOutput {
  brand: string;
  distributionType: string;
  publishReachScore: number;
  seoGeoScore: number;
  aiVisibilityScore: number;
  digitalPRScore: number;
  founderBrandScore: number;
  distributionReachScore: number;
  overallReachIndex: number;
  priorityAction: string;
  platformVisibility: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    publishReach: "Publish Reach",
    seoGeo: "SEO & GEO",
    aiVisibility: "AI Visibility",
    digitalPR: "Digital PR",
    founderBrand: "Founder Brand",
    distributionReach: "Distribution Reach",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getPlatformVisibility(seo: number, ai: number, pr: number, dist: number): Record<string, number> {
  return {
    "Search Engines": Math.min(100, Math.round(seo * 1.04)),
    "AI Platforms": Math.min(100, Math.round(ai * 1.0)),
    "Digital Publications": Math.min(100, Math.round(pr * 1.05)),
    "Social & Communities": Math.min(100, Math.round(dist * 1.0)),
  };
}

export function analyzePublishReach(input: PublishReachInput): PublishReachOutput {
  const scores = {
    publishReach: input.publishReach,
    seoGeo: input.seoGeo,
    aiVisibility: input.aiVisibility,
    digitalPR: input.digitalPR,
    founderBrand: input.founderBrand,
    distributionReach: input.distributionReach,
  };
  const overallReachIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    brand: input.brand,
    distributionType: input.distributionType.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" "),
    publishReachScore: input.publishReach,
    seoGeoScore: input.seoGeo,
    aiVisibilityScore: input.aiVisibility,
    digitalPRScore: input.digitalPR,
    founderBrandScore: input.founderBrand,
    distributionReachScore: input.distributionReach,
    overallReachIndex,
    priorityAction: getPriorityAction(scores),
    platformVisibility: getPlatformVisibility(input.seoGeo, input.aiVisibility, input.digitalPR, input.distributionReach),
  };
}

const args = process.argv.slice(2);
const brand = args[0] || "brand-name";
const distributionType = args[1] || "startup-pr";
const publishReach = parseInt(args[2]) || 85;
const seoGeo = parseInt(args[3]) || 82;
const aiVisibility = parseInt(args[4]) || 88;
const digitalPR = parseInt(args[5]) || 78;
const founderBrand = parseInt(args[6]) || 90;
const distributionReach = parseInt(args[7]) || 80;

const result = analyzePublishReach({
  brand, distributionType, publishReach, seoGeo,
  aiVisibility, digitalPR, founderBrand, distributionReach,
});

console.log(`Brand: ${result.brand}`);
console.log(`Distribution Type: ${result.distributionType}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Publish Reach Score:           ${result.publishReachScore}/100  [${getStatus(result.publishReachScore)}]`);
console.log(`SEO & GEO Score:               ${result.seoGeoScore}/100  [${getStatus(result.seoGeoScore)}]`);
console.log(`AI Visibility Score:           ${result.aiVisibilityScore}/100  [${getStatus(result.aiVisibilityScore)}]`);
console.log(`Digital PR Score:              ${result.digitalPRScore}/100  [${getStatus(result.digitalPRScore)}]`);
console.log(`Founder Brand Score:           ${result.founderBrandScore}/100  [${getStatus(result.founderBrandScore)}]`);
console.log(`Distribution Reach Score:      ${result.distributionReachScore}/100  [${getStatus(result.distributionReachScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Reach Index:           ${result.overallReachIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nPlatform Visibility:");
Object.entries(result.platformVisibility).forEach(([platform, score]) => {
  console.log(`  ${platform.padEnd(26)} ${score}/100`);
});
