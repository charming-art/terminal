// TODO Set text baseline conditionally by browser.
// https://github.com/xtermjs/xterm.js/blob/096fe171356fc9519e0a6b737a98ca82d0587e91/src/browser/renderer/shared/Constants.ts#LL14C1-L14C1
export const TEXT_BASELINE = "ideographic";

function createContext(document, width = 640, height = 480, dpi = null) {
  if (dpi == null) dpi = window.devicePixelRatio;
  const canvas = document.createElement("canvas");
  canvas.width = width * dpi;
  canvas.height = height * dpi;
  canvas.style.width = width + "px";
  canvas.style.height = height + "px";
  const context = canvas.getContext("2d");
  context.scale(dpi, dpi);
  return context;
}

function measureText(text, styles) {
  const span = document.createElement("span");

  // Hide span.
  span.style.visibility = "hidden";
  span.style.position = "absolute";
  span.style.display = "inline-block";
  span.style.left = "-9999em";
  span.style.top = "0";
  span.style.lineHeight = "normal";
  span.setAttribute("aria-hidden", true);

  // Font attributes.
  span.style.fontSize = `${styles.fontSize}px`;
  span.style.fontFamily = styles.fontFamily;

  span.textContent = text;
  document.body.appendChild(span);

  const bbox = span.getBoundingClientRect();
  return { width: Math.floor(bbox.width), height: Math.floor(bbox.height) };
}

function dimensionOf(pixel, count, unit) {
  if (pixel === undefined) return count;
  return (pixel / unit) | 0;
}

// Default options from: https://github.com/xtermjs/xterm.js/blob/ac0207bf2e8a923d0cff95cc383f6f3e36a2e923/src/common/services/OptionsService.ts#LL12C1-L12C1
export class Canvas {
  constructor({
    document = window.document,
    mode = "single",
    cols = mode === "single" ? 80 : 40,
    rows = 24,
    fontFamily = "courier-new, courier, monospace",
    fontSize = 15,
    fontWeight = "normal",
    width,
    height,
  } = {}) {
    this._mode = mode;
    this._fontSize = fontSize;
    this._fontFamily = fontFamily;
    this._fontWeight = fontWeight;

    const { width: tw, height: th } = measureText("W", {
      fontSize,
      fontFamily,
      fontWeight,
    });

    this._cellWidth = mode === "double" ? tw * 2 : tw;
    this._cellHeight = th;
    this._cols = dimensionOf(width, cols, this._cellWidth);
    this._rows = dimensionOf(height, rows, this._cellHeight);
    this._width = this._cols * this._cellWidth;
    this._height = this._rows * this._cellHeight;
    this._context = createContext(document, this._width, this._height, 2);
    this._context.canvas.classList.add("charming-canvas");
  }
  background(color) {
    this._context.fillStyle = color;
    this._context.fillRect(0, 0, this._width, this._height);
    return this;
  }
  char(char, i, j, fg, bg, wide = false) {
    const x = this._cellWidth * i;
    const y = this._cellHeight * j;
    if (bg) {
      this._context.fillStyle = bg;
      this._context.fillRect(x, y, this._cellWidth, this._cellHeight);
    }
    this._context.fillStyle = fg;
    this._context.font = `${this._fontSize}px ${this._fontFamily}`;
    this._context.textBaseline = TEXT_BASELINE;
    this._context.fillText(char, x, y + this._cellHeight);
    if (this._mode === "double" && !wide) {
      this._context.fillText(char, x + this._cellWidth / 2, y + this._cellHeight);
    }
    return this;
  }
  get cols() {
    return this._cols;
  }
  get rows() {
    return this._rows;
  }
  node() {
    return this._context.canvas;
  }
}
