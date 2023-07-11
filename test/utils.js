import { chromium } from "playwright";

export async function createBrowser() {
  return await chromium.launch();
}

export async function createPage(browser) {
  return await (await browser.newContext({ deviceScaleFactor: 2 })).newPage();
}

export function app(name) {
  return `http://localhost:${process.env.TEST_PORT}/?name=${name}`;
}

export async function openApp(page, options = {}) {
  await page.evaluate(`(async () => window.app = await createApp(${JSON.stringify(options)}))()`);
  await page.evaluate("window.app.size()");
  await page.evaluate("document.body.appendChild(window.app.node())");
  await page.waitForSelector(".charming-terminal");
}

export async function openTerminal(page, options = {}) {
  await page.evaluate(`window.terminal = new Terminal(${JSON.stringify(options)})`);
  await page.evaluate("document.body.appendChild(window.terminal.node())");
  await page.waitForSelector(".charming-terminal");
}
