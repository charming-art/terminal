export function after(hook) {
  return function (...params) {
    this._after.push([hook, ...params]);
    return this;
  };
}

export function before(hook) {
  return function (...params) {
    this._before.push([hook, ...params]);
    return this;
  };
}
