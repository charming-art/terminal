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

  test("app.node() should return node.", async () => {
    expect(await page.evaluate("window.app.node() instanceof HTMLCanvasElement")).toBe(true);
    expect(await page.evaluate("window.app.node().classList[0]")).toBe("charming-terminal");
  });
});
