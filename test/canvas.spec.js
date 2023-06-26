import { describe, test, expect, beforeAll, afterAll } from "vitest";
import { chromium } from "playwright";

function app(name) {
  return `http://localhost:${process.env.TEST_PORT}/?name=${name}`;
}

function isMac() {
  return process.platform === "darwin";
}

describe("Canvas Integration Tests", () => {
  let browser;
  let page;

  beforeAll(async () => {
    browser = await chromium.launch();
    page = await (await browser.newContext()).newPage();
    await page.goto(app("canvas"));
    await page.waitForSelector(".charming-canvas");
  });

  afterAll(async () => {
    await browser.close();
  });

  test("new Canvas() should has expected defaults.", async () => {
    const defaults = {
      cols: 80,
      rows: 24,
      fontFamily: "courier-new, courier, monospace",
      fontSize: 15,
      fontWeight: "normal",
      mode: "single",
    };
    for (const [key, value] of Object.entries(defaults)) {
      expect(await page.evaluate(`window.canvas._${key}`)).toBe(value);
    }
  });

  test.runIf(isMac())("new Canvas() should has expected computed attributes.", async () => {
    const computes = {
      cellWidth: 9,
      cellHeight: 18,
      width: 720,
      height: 432,
    };
    for (const [key, value] of Object.entries(computes)) {
      expect(await page.evaluate(`window.canvas._${key}`)).toBe(value);
    }
  });

  test("canvas.node() should return canvas.", async () => {
    expect(await page.evaluate("window.canvas.node() instanceof HTMLCanvasElement")).toBe(true);
    expect(await page.evaluate("window.canvas.node().classList[0]")).toBe("charming-canvas");
  });
});
