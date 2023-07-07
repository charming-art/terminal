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

export function isMac() {
  return process.platform === "darwin";
}
