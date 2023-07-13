import { describe, test, expect, beforeAll, afterAll, beforeEach } from "vitest";
import { createBrowser, createPage, app, openTerminal } from "./utils";

describe("Terminal Integration Tests", () => {
  let browser;
  let page;

  beforeEach(async () => {
    await page.goto(app("noop"));
  });

  beforeAll(async () => {
    browser = await createBrowser();
    page = await createPage(browser);
  });

  afterAll(async () => {
    await browser.close();
  });

  test("new Terminal() should has expected defaults.", async () => {
    await openTerminal(page);
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
    await openTerminal(page);
    expect(await page.evaluate("window.terminal.node() instanceof HTMLCanvasElement")).toBe(true);
    expect(await page.evaluate("window.terminal.node().classList[0]")).toBe("charming-terminal");
  });

  test("terminal._rows and terminal._cols should return dimensions.", async () => {
    await openTerminal(page);
    expect(await page.evaluate("window.terminal._cols")).toBe(80);
    expect(await page.evaluate("window.terminal._rows")).toBe(24);
  });

  test("terminal.char(ch, i, j, fg, bg) should apply fontSize, fontWeight and fontFamily.", async () => {
    await openTerminal(page, { fontSize: 20, fontWeight: "bold", fontFamily: "PingFang" });
    await page.evaluate("window.terminal.char('@', 0, 0, 'red', 'yellow')");
    expect(await page.evaluate("window.terminal._context.font")).toBe("bold 20px PingFang");
  });
});
