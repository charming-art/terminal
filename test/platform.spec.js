import { describe, beforeAll, test, expect } from "vitest";
import { createBrowser, createPage, openTerminal, app } from "./utils";

describe("textBaseline in Chromium", () => {
  let browser;
  let page;

  beforeAll(async () => {
    browser = await createBrowser();
    page = await createPage(browser);
    await page.goto(app("noop"));
  });

  test("textBaseline should be ideographic in Chromium.", async () => {
    await openTerminal(page);
    await page.evaluate("window.terminal.char('@', 0, 0, 'red', 'red')");
    expect(await page.evaluate("window.terminal._context.textBaseline")).toBe("ideographic");
  });
});

describe("textBaseline in FireFox", () => {
  let browser;
  let page;

  beforeAll(async () => {
    browser = await createBrowser({ type: "firefox" });
    page = await createPage(browser);
    await page.goto(app("noop"));
  });

  test("textBaseline should be bottom in Firefox.", async () => {
    await openTerminal(page);
    await page.evaluate("window.terminal.char('@', 0, 0, 'red', 'red')");
    expect(await page.evaluate("window.terminal._context.textBaseline")).toBe("bottom");
  });
});
