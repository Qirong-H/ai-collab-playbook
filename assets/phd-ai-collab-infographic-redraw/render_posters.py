#!/usr/bin/env python3
from __future__ import annotations

import asyncio
import json
from pathlib import Path

from PIL import Image
from playwright.async_api import async_playwright


ROOT = Path(__file__).resolve().parent
DOCS_FIGS = ROOT.parent.parent / "docs" / "figs"
EXPORTS = ROOT / "exports"

POSTERS = [
    {
        "html": ROOT / "index.html",
        "doc_png": DOCS_FIGS / "phd-ai-collab-overview.png",
        "export_png": EXPORTS / "phd-ai-collab-infographic-final.png",
        "hd_png": EXPORTS / "phd-ai-collab-infographic-final-hd.png",
    },
    {
        "html": ROOT / "learning-guide.html",
        "doc_png": DOCS_FIGS / "phd-ai-learning-guide.png",
        "export_png": EXPORTS / "phd-ai-learning-guide.png",
        "hd_png": EXPORTS / "phd-ai-learning-guide-hd.png",
    },
    {
        "html": ROOT / "agent-framework.html",
        "doc_png": DOCS_FIGS / "phd-ai-agent-framework.png",
        "export_png": EXPORTS / "phd-ai-agent-framework.png",
        "hd_png": EXPORTS / "phd-ai-agent-framework-hd.png",
    },
    {
        "html": ROOT / "learning-roadmap.html",
        "doc_png": DOCS_FIGS / "phd-ai-learning-roadmap.png",
        "export_png": EXPORTS / "phd-ai-learning-roadmap.png",
        "hd_png": EXPORTS / "phd-ai-learning-roadmap-hd.png",
    },
]


async def validate_page(page) -> list[dict]:
    return await page.evaluate(
        """
        () => {
          const poster = document.querySelector('[data-poster-root]');
          if (!poster) {
            return [{ type: 'missing-poster-root', selector: '[data-poster-root]' }];
          }

          const issues = [];
          const posterRect = poster.getBoundingClientRect();

          if (Math.ceil(poster.scrollWidth) > Math.ceil(poster.clientWidth + 1)) {
            issues.push({
              type: 'poster-scroll-width',
              selector: '[data-poster-root]',
              scrollWidth: poster.scrollWidth,
              clientWidth: poster.clientWidth,
            });
          }

          if (Math.ceil(poster.scrollHeight) > Math.ceil(poster.clientHeight + 1)) {
            issues.push({
              type: 'poster-scroll-height',
              selector: '[data-poster-root]',
              scrollHeight: poster.scrollHeight,
              clientHeight: poster.clientHeight,
            });
          }

          const watched = poster.querySelectorAll('[data-fit-check]');
          for (const el of watched) {
            const rect = el.getBoundingClientRect();
            const style = getComputedStyle(el);
            const selector =
              el.tagName.toLowerCase() +
              (el.className ? '.' + String(el.className).trim().replace(/\\s+/g, '.') : '');

            if (rect.right > posterRect.right + 1 || rect.bottom > posterRect.bottom + 1) {
              issues.push({
                type: 'boundary-overflow',
                selector,
                right: rect.right,
                bottom: rect.bottom,
                posterRight: posterRect.right,
                posterBottom: posterRect.bottom,
              });
            }

            if (style.overflow !== 'visible' || style.overflowX !== 'visible' || style.overflowY !== 'visible') {
              if (Math.ceil(el.scrollWidth) > Math.ceil(el.clientWidth + 1)) {
                issues.push({
                  type: 'inner-overflow-x',
                  selector,
                  scrollWidth: el.scrollWidth,
                  clientWidth: el.clientWidth,
                });
              }

              if (Math.ceil(el.scrollHeight) > Math.ceil(el.clientHeight + 1)) {
                issues.push({
                  type: 'inner-overflow-y',
                  selector,
                  scrollHeight: el.scrollHeight,
                  clientHeight: el.clientHeight,
                });
              }
            }
          }

          return issues;
        }
        """
    )


async def render_one(browser, spec: dict) -> None:
    context = await browser.new_context(
        viewport={"width": 2200, "height": 2200},
        device_scale_factor=1,
    )
    page = await context.new_page()
    await page.goto(spec["html"].as_uri(), wait_until="load")
    await page.evaluate("() => document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()")
    await page.wait_for_timeout(250)

    issues = await validate_page(page)
    if issues:
      print(json.dumps({"html": spec["html"].name, "issues": issues}, ensure_ascii=False, indent=2))
      raise SystemExit(f"validation failed for {spec['html'].name}")

    poster = page.locator("[data-poster-root]")
    spec["doc_png"].parent.mkdir(parents=True, exist_ok=True)
    spec["export_png"].parent.mkdir(parents=True, exist_ok=True)
    await poster.screenshot(path=str(spec["doc_png"]))
    await poster.screenshot(path=str(spec["export_png"]))
    await context.close()

    hd_context = await browser.new_context(
        viewport={"width": 2200, "height": 2200},
        device_scale_factor=2,
    )
    hd_page = await hd_context.new_page()
    await hd_page.goto(spec["html"].as_uri(), wait_until="load")
    await hd_page.evaluate("() => document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()")
    await hd_page.wait_for_timeout(250)
    hd_poster = hd_page.locator("[data-poster-root]")
    await hd_poster.screenshot(path=str(spec["hd_png"]))
    await hd_context.close()

    if spec["html"].name == "index.html":
        webp_path = EXPORTS / "phd-ai-collab-infographic-final.webp"
        with Image.open(spec["export_png"]) as img:
            img.save(webp_path, "WEBP", quality=94, method=6)


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            channel="chrome",
            headless=True,
            args=["--font-render-hinting=medium"],
        )
        for spec in POSTERS:
            await render_one(browser, spec)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
