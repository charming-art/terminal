import { describe, test, expect, beforeAll, afterAll } from "vitest";
import { createBrowser, createPage, app } from "./utils";

describe("Canvas Integration Tests", () => {
  let browser;
  let page;

  beforeAll(async () => {
    browser = await createBrowser();
    page = await createPage(browser);
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

  test("canvas.node() should return canvas.", async () => {
    expect(await page.evaluate("window.canvas.node() instanceof HTMLCanvasElement")).toBe(true);
    expect(await page.evaluate("window.canvas.node().classList[0]")).toBe("charming-canvas");
  });

  test("canvas.rows and canvas.cols should return dimensions.", async () => {
    expect(await page.evaluate(`window.canvas.cols`)).toBe(80);
    expect(await page.evaluate(`window.canvas.rows`)).toBe(24);
  });
});
