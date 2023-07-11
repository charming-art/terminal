import { describe, test, expect, beforeAll, afterAll } from "vitest";
import { createBrowser, createPage, app, openTerminal } from "./utils";

describe("Terminal Integration Tests", () => {
  let browser;
  let page;

  beforeAll(async () => {
    browser = await createBrowser();
    page = await createPage(browser);
    await page.goto(app("noop"));
    await openTerminal(page);
  });

  afterAll(async () => {
    await browser.close();
  });

  test("new Terminal() should has expected defaults.", async () => {
    const defaults = {
      cols: 80,
      rows: 24,
      fontFamily: "courier-new, courier, monospace",
      fontSize: 15,
      fontWeight: "normal",
      mode: "single",
    };
    for (const [key, value] of Object.entries(defaults)) {
      expect(await page.evaluate(`window.terminal._${key}`)).toBe(value);
    }
  });

  test("terminal.node() should return terminal.", async () => {
    expect(await page.evaluate("window.terminal.node() instanceof HTMLCanvasElement")).toBe(true);
    expect(await page.evaluate("window.terminal.node().classList[0]")).toBe("charming-terminal");
  });

  test("terminal.rows() and terminal.cols() should return dimensions.", async () => {
    expect(await page.evaluate("window.terminal.cols()")).toBe(80);
    expect(await page.evaluate("window.terminal.rows()")).toBe(24);
  });
});
