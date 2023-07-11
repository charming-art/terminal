import { describe, test, beforeAll, afterAll, expect } from "vitest";
import path from "path";
import * as fs from "fs";
import * as apps from "./apps";
import { createBrowser, createPage, app } from "./utils.js";
import { frameOf } from "./common.js";

async function screenshot(page, path) {
  const string = await page.evaluate(`"" + (window.app ? window.app._canvas : window.canvas)`);
  if (string === "undefined") throw new Error(`Nothing to compare: ${path}`);
  fs.writeFileSync(path, string, { encoding: "utf-8" });
}

function match(expectPath, actualPath) {
  const expectString = fs.readFileSync(expectPath, { encoding: "utf8", flag: "r" });
  const actualString = fs.readFileSync(actualPath, { encoding: "utf8", flag: "r" });
  expect(expectString).toBe(actualString);
}

async function expectMatchSnapshot(page, name) {
  const dir = path.resolve(__dirname, "./output");
  const expect = path.resolve(__dirname, `./output/${name}.txt`);
  const actual = path.resolve(__dirname, `./output/${name}-actual.txt`);

  if (!fs.existsSync(dir)) fs.mkdirSync(dir);
  if (!fs.existsSync(expect)) {
    if (process.env.CI === "true") throw new Error(`Please generate golden image for ${name}`);
    console.warn(`! generate ${name}`);
    await screenshot(page, expect);
  } else {
    await screenshot(page, actual);
    match(expect, actual);
    fs.unlinkSync(actual);
  }
}

describe("Snapshots", () => {
  let browser;
  let page;

  beforeAll(async () => {
    browser = await createBrowser();
    page = await createPage(browser);
  });

  afterAll(async () => {
    await browser.close();
  });

  const onlys = Object.entries(apps).filter(([, render]) => render.only === true);
  if (process.env.CI === "true" && onlys.length) throw new Error("Remove .only for tests.");

  const tests = onlys.length ? onlys : Object.entries(apps).filter(([, render]) => render.snap !== undefined);
  for (const [name, render] of tests) {
    const { snap } = render;
    test(name, async () => {
      await page.goto(app(name));
      if (typeof snap === "number") await page.getByText(frameOf(snap)).click();
      else await page.waitForSelector(".charming-canvas");
      await expectMatchSnapshot(page, name);
    });
  }
});
