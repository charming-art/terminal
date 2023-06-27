import { describe, test, beforeAll, afterAll } from "vitest";
import path from "path";
import pixelmatch from "pixelmatch";
import { PNG } from "pngjs";
import * as fs from "fs";
import { isMac, createBrowser, createPage, app } from "./utils";
import * as apps from "./apps";

async function screenshot(page, path, className = "charming-canvas") {
  const { x, y, width, height } = await page.evaluate(
    `window.document.getElementsByClassName('${className}')[0].getBoundingClientRect()`
  );
  await page.screenshot({
    path,
    clip: { x, y, width, height },
  });
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

  const tests = Object.entries(apps).filter(([, render]) => render.snap);

  for (const [name] of tests) {
    test(name, async () => {
      const expect = path.resolve(__dirname, `./output/${name}.png`);
      const actual = path.resolve(__dirname, `./output/${name}-actual.png`);
      const diff = path.resolve(__dirname, `./output/${name}-diff.png`);

      await page.goto(app(name));
      await page.waitForSelector(".charming-canvas");

      if (!fs.existsSync(expect)) {
        if (process.env.CI === "true") {
          throw new Error(`Please generate golden image for ${name}`);
        }
        console.warn(`! generate ${name}`);
        await screenshot(page, expect);
      } else {
        await screenshot(page, actual);
        if (match(expect, actual, diff)) {
          if (fs.existsSync(diff)) fs.unlinkSync(diff);
          fs.unlinkSync(actual);
        } else {
          throw new Error(`Mismatch: ${name}`);
        }
      }
    });
  }
});
