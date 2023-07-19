import { describe, test, expect, beforeAll, afterAll } from "vitest";
import { createBrowser, createPage, app, openApp } from "./utils";

describe("App Integration Tests", () => {
  let browser;
  let page;

  beforeAll(async () => {
    browser = await createBrowser();
    page = await createPage(browser);
    await page.goto(app("noop"));
    await openApp(page);
  });

  afterAll(async () => {
    await browser.close();
  });

  test("new App() should have expected defaults.", async () => {
    const defined = ["memory", "renderer", "terminal"];
    for (const key of defined) {
      expect(await page.evaluate(`window.app._${key}`)).toBeTruthy();
    }
  });

  test("app.point(x, y) should return this.", async () => {
    expect(await page.evaluate("window.app.point(0, 0) === window.app")).toBe(true);
  });

  test("app.stroke(ch, fg, bg) should return this.", async () => {
    expect(await page.evaluate("window.app.stroke('@', 'yellow', 'red') === window.app")).toBe(true);
  });

  test("app.scene(color) should return this.", async () => {
    expect(await page.evaluate("window.app.scene('yellow') === window.app")).toBe(true);
  });

  test("app.render() should return this.", async () => {
    expect(await page.evaluate("window.app.render() === window.app")).toBe(true);
  });

  test("app.cols() should return cols.", async () => {
    expect(await page.evaluate("window.app.cols()")).toBe(80);
  });

  test("app.rows() should return rows.", async () => {
    expect(await page.evaluate("window.app.rows()")).toBe(24);
  });

  test("app.height() should return height.", async () => {
    expect(await page.evaluate("window.app.height()")).toBeTypeOf("number");
  });

  test("app.width() should return width.", async () => {
    expect(await page.evaluate("window.app.width()")).toBeTypeOf("number");
  });

  test("app.cellWidth() should return cellWidth.", async () => {
    expect(await page.evaluate("window.app.cellWidth()")).toBeTypeOf("number");
  });

  test("app.cellHeight() should return cellHeight.", async () => {
    expect(await page.evaluate("window.app.cellHeight()")).toBeTypeOf("number");
  });

  test("app.fontWeight() should return fontWeight.", async () => {
    expect(await page.evaluate("window.app.fontWeight()")).toBe("normal");
  });

  test("app.fontSize() should return fontSize.", async () => {
    expect(await page.evaluate("window.app.fontSize()")).toBe(15);
  });

  test("app.fontFamily() should return fontFamily.", async () => {
    expect(await page.evaluate("window.app.fontFamily()")).toBe("courier-new, courier, monospace");
  });

  test("app.node() should return node.", async () => {
    expect(await page.evaluate("window.app.node() instanceof HTMLCanvasElement")).toBe(true);
    expect(await page.evaluate("window.app.node().classList[0]")).toBe("charming-terminal");
  });

  test("app.pixels(x, y, render) should return app.", async () => {
    expect(await page.evaluate(`window.app.pixels(0, 0, () => {}) === window.app`)).toBe(true);
  });

  test("app.call(function[, ...arguments]) should return app.", async () => {
    expect(await page.evaluate("window.app.call(() => {}, 0, 0) === window.app")).toBe(true);
  });
});
