// TODO Set text baseline conditionally by browser.
// https://github.com/xtermjs/xterm.js/blob/096fe171356fc9519e0a6b737a98ca82d0587e91/src/browser/renderer/shared/Constants.ts#LL14C1-L14C1
export const TEXT_BASELINE = "ideographic";

function createContext(document, width = 640, height = 480, dpi = null) {
  if (dpi == null) dpi = devicePixelRatio;
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
  span.style.display = "inline";
  span.style.left = "-1000px";
  span.style.top = "-1000px";

  // Font attributes.
  span.style.fontSize = `${styles.fontSize}px`;
  span.style.fontFamily = styles.fontFamily;
  span.style.fontWeight = styles.fontWeight;
  span.style.fontStyle = styles.fontStyle;
  span.style.fontVariant = styles.fontVariant;

  span.innerHTML = text;
  document.body.appendChild(span);
  return { width: span.clientWidth, height: span.clientHeight };
}

function dimensionOf(pixel, count, unit) {
  if (pixel === undefined) return count;
  return (pixel / unit) | 0;
}

// Default options from: https://github.com/xtermjs/xterm.js/blob/ac0207bf2e8a923d0cff95cc383f6f3e36a2e923/src/common/services/OptionsService.ts#LL12C1-L12C1
export class Canvas {
  constructor({
    document = window.document,
    cols = 80,
    rows = 24,
    fontFamily = "courier-new, courier, monospace",
    fontSize = 15,
    fontWeight = "normal",
    mode = "single",
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

    this._cols = dimensionOf(width, cols, tw);
    this._rows = dimensionOf(height, rows, th);
    this._cellWidth = tw;
    this._cellHeight = th;
    this._width = this._cols * tw;
    this._height = this._rows * th;
    this._context = createContext(document, this._width, this._height);
    this._context.canvas.classList.add("charming-canvas");
  }
  background(color) {
    this._context.fillStyle = color;
    this._context.fillRect(0, 0, this._width, this._height);
    return this;
  }
  char(char, i, j, fg, bg, wide = false) {
    const cols = this._mode === "single" ? 1 : 2;
    const x = this._cellWidth * i * cols;
    const y = this._cellHeight * j;
    if (bg) {
      this._context.fillStyle = bg;
      this._context.fillRect(x, y, this._cellWidth * cols, this._cellHeight);
    }
    this._context.fillStyle = fg;
    this._context.font = `${this._fontSize}px ${this._fontFamily}`;
    this._context.textBaseline = TEXT_BASELINE;
    this._context.fillText(char, x, y + this._cellHeight);
    if (this._mode === "double" && !wide) {
      this._context.fillText(char, x + this._cellWidth, y + this._cellHeight);
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
