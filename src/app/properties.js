export function app$node() {
  return this._terminal.node();
}

export function app$cols() {
  return this._terminal._cols;
}

export function app$rows() {
  return this._terminal._rows;
}

export function app$width() {
  return this._terminal._width;
}

export function app$height() {
  return this._terminal._height;
}

export function app$fontSize() {
  return this._terminal._fontSize;
}

export function app$fontWeight() {
  return this._terminal._fontWeight;
}

export function app$fontFamily() {
  return this._terminal._fontFamily;
}

export function app$cellWidth() {
  return this._terminal._cellWidth;
}

export function app$cellHeight() {
  return this._terminal._cellHeight;
}

export function app$frameCount() {
  return this._frameCount;
}

export function app$frameRate(frameRate) {
  return arguments.length ? ((this._frameRate = frameRate), (this._reschedule = true), this) : this._frameRate;
}
