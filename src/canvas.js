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

// TODO Set text baseline conditionally by browser.
// https://github.com/xtermjs/xterm.js/blob/096fe171356fc9519e0a6b737a98ca82d0587e91/src/browser/renderer/shared/Constants.ts#LL14C1-L14C1
export const TEXT_BASELINE = "ideographic";

function measureText(text, styles) {
  const span = document.createElement("span");

  // Out of window.
  span.style.visibility = "hidden";
  span.style.position = "absolute";
  span.style.display = "inline";
  span.style.left = "-1000px";
  span.style.top = "-1000px";

  // Specified styles.
  span.style.fontSize = `${styles.fontSize}px`;
  span.style.fontFamily = styles.fontFamily;
  span.style.fontWeight = styles.fontWeight;
  span.style.fontStyle = styles.fontStyle;
  span.style.fontVariant = styles.fontVariant;

  span.innerHTML = text;
  document.body.appendChild(span);
  return { width: span.clientWidth, height: span.clientHeight };
}

export class Canvas {
  constructor({
    cols = 30,
    rows = 10,
    document = window.document,
    background = "#000",
    fontSize = 12,
    fontFamily,
  } = {}) {
    const { width: tw, height: th } = measureText("W", { fontSize });
    this._fontSize = fontSize;
    this._fontFamily = fontFamily;
    this._cellWidth = tw;
    this._cellHeight = th;
    this._width = cols * tw;
    this._height = rows * th;
    this._context = createContext(document, this._width, this._height);
    this._context.fillStyle = background;
    this._context.fillRect(0, 0, this._width, this._height);
  }
  char(text, i, j, { color, background } = {}) {
    const x = this._cellWidth * i;
    const y = this._cellHeight * j;
    const ch = text[0];
    if (background) {
      this._context.fillStyle = background;
      this._context.fillRect(
        x,
        y,
        this._cellWidth,
        this._cellHeight,
        background
      );
    }
    this._context.fillStyle = color;
    this._context.font = `${this._fontSize}px ${this._fontFamily}`;
    this._context.textBaseline = TEXT_BASELINE;
    this._context.fillText(ch, x, y + this._cellHeight);
    return this;
  }
  node() {
    return this._context.canvas;
  }
}
