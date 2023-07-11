// TODO Set text baseline conditionally by browser.
// https://github.com/xtermjs/xterm.js/blob/096fe171356fc9519e0a6b737a98ca82d0587e91/src/browser/renderer/shared/Constants.ts#LL14C1-L14C1
export const TEXT_BASELINE = "ideographic";

export const CELL_SIZE = 3;

export const TERMINAL_CLASS = "charming-terminal";

// Default options from: https://github.com/xtermjs/xterm.js/blob/ac0207bf2e8a923d0cff95cc383f6f3e36a2e923/src/common/services/OptionsService.ts#LL12C1-L12C1
export function Terminal({
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
  const { width: tw, height: th } = measureText("W", {
    fontSize,
    fontFamily,
    fontWeight,
  });
  const cellWidth = mode === "double" ? tw * 2 : tw;
  const cellHeight = th;
  const computedCols = dimensionOf(width, cols, cellWidth);
  const computedRows = dimensionOf(height, rows, cellHeight);
  const computedWidth = computedCols * cellWidth;
  const computedHeight = computedRows * cellHeight;
  const context = createContext(document, computedWidth, computedHeight);
  const buffer = Array.from({ length: computedCols * computedRows }, () => null);
  context.canvas.classList.add(TERMINAL_CLASS);
  Object.defineProperties(this, {
    _mode: { value: mode },
    _fontSize: { value: fontSize },
    _fontFamily: { value: fontFamily },
    _fontWeight: { value: fontWeight },
    _cellWidth: { value: cellWidth },
    _cellHeight: { value: cellHeight },
    _cols: { value: computedCols },
    _rows: { value: computedRows },
    _width: { value: computedWidth },
    _height: { value: computedHeight },
    _context: { value: context },
    _buffer: { value: buffer },
  });
}

Object.defineProperties(Terminal.prototype, {
  background: { value: terminal$background, writable: true, configurable: true },
  char: { value: terminal$char, writable: true, configurable: true },
  toString: { value: terminal$toString, writable: true, configurable: true },
  node: { value: terminal$node, writable: true, configurable: true },
  cols: { value: terminal$cols, writable: true, configurable: true },
  rows: { value: terminal$rows, writable: true, configurable: true },
});

function terminal$background(color) {
  this._context.fillStyle = color;
  this._context.fillRect(0, 0, this._width, this._height);
  this._buffer.fill(null);
  return this;
}

function terminal$char(char, i, j, fg, bg, wide = false) {
  const x = this._cellWidth * i;
  const y = this._cellHeight * j;
  const index = (this._cols * j + i) * CELL_SIZE;

  if (bg) {
    this._context.fillStyle = bg;
    this._context.fillRect(x, y, this._cellWidth, this._cellHeight);
    this._buffer[index + 2] = bg;
  }

  if (fg) {
    this._context.fillStyle = fg;
    this._buffer[index + 1] = fg;
  }

  if (!char) return;
  this._context.font = `${this._fontSize}px ${this._fontFamily}`;
  this._context.textBaseline = TEXT_BASELINE;
  this._context.fillText(char, x, y + this._cellHeight);
  this._buffer[index] = char;

  if (this._mode !== "double" || wide) return;
  this._context.fillText(char, x + this._cellWidth / 2, y + this._cellHeight);
  this._buffer[index] += char;

  return this;
}

function terminal$toString() {
  let string = "";
  for (let j = 0; j < this._rows; j++) {
    if (j !== 0) string += "\n";
    for (let i = 0; i < this._cols; i++) {
      const index = (this._cols * j + i) * CELL_SIZE;
      const empty = this._mode === "double" ? "··" : "·";
      const char = this._buffer[index] || empty;
      string += char;
    }
  }
  return string;
}

function terminal$node() {
  return this._context.canvas;
}

function terminal$rows() {
  return this._rows;
}

function terminal$cols() {
  return this._cols;
}

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
  span.style.display = "inline-block";
  span.style.left = "-9999em";
  span.style.top = "0";
  span.style.lineHeight = "normal";
  span.setAttribute("aria-hidden", true);

  // Font attributes.
  span.style.fontSize = `${styles.fontSize}px`;
  span.style.fontFamily = styles.fontFamily;

  span.innerHTML = text;
  document.body.appendChild(span);

  const bbox = span.getBoundingClientRect();
  return { width: bbox.width, height: Math.ceil(bbox.height) };
}

function dimensionOf(pixel, count, unit) {
  if (pixel === undefined) return count;
  return (pixel / unit) | 0;
}
