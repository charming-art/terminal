import { describe, test, beforeAll, afterAll } from "vitest";
import path from "path";
import pixelmatch from "pixelmatch";
import { PNG } from "pngjs";
import * as fs from "fs";
import * as apps from "./apps";
import { isMac, createBrowser, createPage, app } from "./utils.js";
import { frameOf } from "./common.js";

async function screenshot(page, path, className = "charming-canvas") {
  await page.locator(`.${className}`).screenshot({ path, scale: "css" });
}

function match(expect, actual, diff, { maxError = 0 } = {}) {
  const expectImage = PNG.sync.read(fs.readFileSync(expect));
  const actualImage = PNG.sync.read(fs.readFileSync(actual));
  const { width, height } = expectImage;
  const diffImage = new PNG({ width, height });
  const mismatch = pixelmatch(expectImage.data, actualImage.data, diffImage.data, width, height, {
    threshold: 0.1,
  });
  const error = mismatch - maxError;
  if (error > 0) {
    fs.writeFileSync(diff, PNG.sync.write(diffImage));
  }
  return error === 0;
}

async function expectMatchSnapshot(page, name, className) {
  const expect = path.resolve(__dirname, `./output/${name}.png`);
  const actual = path.resolve(__dirname, `./output/${name}-actual.png`);
  const diff = path.resolve(__dirname, `./output/${name}-diff.png`);

  if (!fs.existsSync(expect)) {
    if (process.env.CI === "true") {
      throw new Error(`Please generate golden image for ${name}`);
    }
    console.warn(`! generate ${name}`);
    await screenshot(page, expect, className);
  } else {
    await screenshot(page, actual);
    if (match(expect, actual, diff)) {
      if (fs.existsSync(diff)) fs.unlinkSync(diff);
      fs.unlinkSync(actual);
    } else {
      throw new Error(`Mismatch: ${name}`);
    }
  }
}

describe.runIf(isMac())("Snapshots", () => {
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
